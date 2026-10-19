# SparseSolve(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Solves the equation *Ax = b* for vectors of double-precision values using the specified iterative method.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func SparseSolve(_ method: SparseIterativeMethod, _ A: SparseMatrix_Double, _ b: DenseVector_Double, _ x: DenseVector_Double) -> SparseIterativeStatus_t
```

#### Return Value

A [`SparseIterativeStatus_t`](sparseiterativestatus_t.md) enumeration that represents the status of the iterative solve.

#### Discussion

Use this function to solve a system of linear equations using a factored coefficient matrix. The following figure shows a system of equations where the coefficient matrix is sparse:

![A mathematical equation that has one set of three simultaneous equations on the left. Each equation has three unknowns. The same set of simultaneous equations appears on the right as a single matrix equation, A x equals B. The single matrix equation consists of a three-by-three matrix multiplied by a three-element column matrix that equals a three-element column matrix.](/images/com.apple.accelerate/media-3703938@2x.png)

The following code solves this system using the least squares minimum residual method:

**Swift**:

```swift
// Create the coefficient matrix `A` from coordinate (COO) arrays.
let rowIndices: [Int32] =    [ 0,  1, 1,  2]
let columnIndices: [Int32] = [ 2,  0, 2,  1]
let aValues: [Double] =      [10, 20, 5, 50]

let A = SparseConvertFromCoordinate(3, 3,
                                    4, 1,
                                    SparseAttributes_t(),
                                    rowIndices, columnIndices,
                                    aValues)
defer {
    SparseCleanup(A)
}

// Create the right-hand-side vector `b` (also holds the solution on return).
var bValues: [Double] = [30, 35, 100]
var xValues = [Double](repeating: .nan, count: bValues.count)

bValues.withUnsafeMutableBufferPointer { bPtr in
    xValues.withUnsafeMutableBufferPointer { xPtr in
        
        let b = DenseVector_Double(count: 3,
                                   data: bPtr.baseAddress!)
        
        let x = DenseVector_Double(count: 3,
                                   data: xPtr.baseAddress!)
        
        SparseSolve(SparseLSMR(), A, b, x)
    }
}
print(xValues) // Prints "[1.0, 2.0, 3.0]".
```

**Objective-C**:

```objc
// Create the coefficient matrix `A` from coordinate (COO) arrays.
int rowIndices[]    = {0, 1, 1, 2};
int columnIndices[] = {2, 0, 2, 1};
double aValues[]    = {10, 20, 5, 50};

SparseMatrix_Double A = SparseConvertFromCoordinate(3, 3,
                                                    4, 1,
                                                    (SparseAttributes_t){0},
                                                    rowIndices, columnIndices,
                                                    aValues);

// Create the right-hand-side vector `b` and solution vector `x`.
double bValues[] = {30, 35, 100};
double xData[3]  = {0};

DenseVector_Double b = {
    .count = 3,
    .data  = bValues
};

DenseVector_Double x = {
    .count = 3,
    .data  = xData
};

// Solve `Ax = b` using the LSMR iterative method.
SparseSolve(SparseLSMR(), A, b, x);

// Prints "[1, 2, 3]".
printf("[%g, %g, %g]\n", xData[0], xData[1], xData[2]);

SparseCleanup(A);
```

On return, x`Values` contains the values `[1.0, 2.0, 3.0]`.

## Parameters

- `method`: The iterative method.
- `A`: The matrix *A*.
- `b`: The vector *b*.
- `x`: The vector *x*.

## See Also

- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Float, DenseVector_Float, DenseVector_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-97k3a.md)
  Solves the equation *Ax = b* for vectors of single-precision values using the specified iterative method.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseVector_Double, DenseVector_Double) -> Void, DenseVector_Double, DenseVector_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-26fae.md)
  Solves the equation *Ax = b* for vectors of double-precision values, treating *A* as an operator and using the specified iterative method.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseVector_Float, DenseVector_Float) -> Void, DenseVector_Float, DenseVector_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-9yhgp.md)
  Solves the equation *Ax = b* for vectors of single-precision values, treating *A* as an operator and using the specified iterative method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:_:_:)-7f1sp)*