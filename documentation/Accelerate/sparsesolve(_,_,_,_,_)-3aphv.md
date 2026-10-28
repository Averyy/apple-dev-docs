# SparseSolve(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Solves the equation *Ax = b* for vectors of single-precision values using the specified iterative method and opaque preconditioner.

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
func SparseSolve(_ method: SparseIterativeMethod, _ A: SparseMatrix_Float, _ b: DenseVector_Float, _ x: DenseVector_Float, _ Preconditioner: SparseOpaquePreconditioner_Float) -> SparseIterativeStatus_t
```

```c
static SparseIterativeStatus_t SparseSolve(SparseIterativeMethod method, SparseMatrix_Float A, DenseVector_Float b, DenseVector_Float x, SparseOpaquePreconditioner_Float Preconditioner);
```

## Return Value

A [`SparseIterativeStatus_t`](./sparseiterativestatus_t.md) enumeration that represents the status of the iterative solve.

## Discussion

Use this function to solve a system of linear equations using a factored coefficient matrix. Preconditioning the coefficient matrix can reduce the number of iterations the function requires to converge the system.

The following figure shows two systems of equations where the coefficient matrix is sparse:

![A mathematical equation that has one set of three simultaneous equations on the left. Each equation has three unknowns. The same set of simultaneous equations appears on the right as a single matrix equation, A x equals B. The single matrix equation consists of a three-by-three matrix multiplied by a three-element column matrix that equals a three-element column matrix.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3703931@2x.png)

The following code solves this system by applying a diagonal scaling preconditioner and using the least squares minimum residual method:

**Swift**:

```swift
// Create the coefficient matrix `A` from coordinate (COO) arrays.
let rowIndices: [Int32] =    [ 0,  1, 1,  2]
let columnIndices: [Int32] = [ 2,  0, 2,  1]
let aValues: [Float] =       [10, 20, 5, 50]

let A = SparseConvertFromCoordinate(3, 3,
                                    4, 1,
                                    SparseAttributes_t(),
                                    rowIndices, columnIndices,
                                    aValues)
let preconditioner = SparseCreatePreconditioner(SparsePreconditionerDiagScaling,
                                                A)

defer {
    SparseCleanup(A)
    SparseCleanup(preconditioner)
}

// Create the right-hand-side vector `b` (also holds the solution on return).
var bValues: [Float] = [30, 35, 100]
var xValues = [Float](repeating: .nan, count: bValues.count)

bValues.withUnsafeMutableBufferPointer { bPtr in
    xValues.withUnsafeMutableBufferPointer { xPtr in
        
        let b = DenseVector_Float(count: 3,
                                   data: bPtr.baseAddress!)
        
        let x = DenseVector_Float(count: 3,
                                   data: xPtr.baseAddress!)
        
        SparseSolve(SparseLSMR(),
                    A, b, x,
                    preconditioner)
    }
}
print(xValues) // Prints "[1.0, 2.0, 3.0]".
```

**Objective-C**:

```objc
// Create the coefficient matrix `A` from coordinate (COO) arrays.
int rowIndices[]    = {0, 1, 1, 2};
int columnIndices[] = {2, 0, 2, 1};
float aValues[]     = {10, 20, 5, 50};

SparseMatrix_Float A = SparseConvertFromCoordinate(3, 3,
                                                   4, 1,
                                                   (SparseAttributes_t){0},
                                                   rowIndices, columnIndices,
                                                   aValues);

SparseOpaquePreconditioner_Float preconditioner =
    SparseCreatePreconditioner(SparsePreconditionerDiagScaling, A);

// Create the right-hand-side vector `b` and output vector `x`.
float bValues[] = {30, 35, 100};
float xValues[] = {0, 0, 0};

DenseVector_Float b = { .count = 3, .data = bValues };
DenseVector_Float x = { .count = 3, .data = xValues };

// Solve `Ax = b` using the LSMR iterative method with opaque preconditioner.
SparseSolve(SparseLSMR(), A, b, x, preconditioner);

// Prints "[1, 2, 3]".
printf("[%g, %g, %g]\n", xValues[0], xValues[1], xValues[2]);

SparseCleanup(A);
SparseCleanup(preconditioner);
```

On return, x`Values` contains the values `[1.0, 2.0, 3.0]`.

## Parameters

- `method`: The iterative method.
- `A`: The matrix *A*.
- `b`: The vector *b*.
- `x`: The vector *x*.
- `Preconditioner`: The preconditioner to apply.

## See Also

### Iterative sparse solve functions with preconditioner
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Double, DenseVector_Double, DenseVector_Double, SparseOpaquePreconditioner_Double) -> SparseIterativeStatus_t](./sparsesolve%28_,_,_,_,_%29-1qwax.md)
  Solves the equation *Ax = b* for vectors of double-precision values using the specified iterative method and opaque preconditioner.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Double, DenseVector_Double, DenseVector_Double, SparsePreconditioner_t) -> SparseIterativeStatus_t](./sparsesolve%28_,_,_,_,_%29-5vs11.md)
  Solves the equation *Ax = b* for vectors of double-precision values using the specified iterative method and preconditioner type.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Float, DenseVector_Float, DenseVector_Float, SparsePreconditioner_t) -> SparseIterativeStatus_t](./sparsesolve%28_,_,_,_,_%29-9nzvm.md)
  Solves the equation *Ax = b* for vectors of single-precision values using the specified iterative method and preconditioner type.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseVector_Double, DenseVector_Double) -> Void, DenseVector_Double, DenseVector_Double, SparseOpaquePreconditioner_Double) -> SparseIterativeStatus_t](./sparsesolve%28_,_,_,_,_%29-6i1nx.md)
  Solves the equation *Ax = b* for vectors of double-precision values, treating *A* as an operator and using the specified iterative method and preconditioner.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseVector_Float, DenseVector_Float) -> Void, DenseVector_Float, DenseVector_Float, SparseOpaquePreconditioner_Float) -> SparseIterativeStatus_t](./sparsesolve%28_,_,_,_,_%29-7wnum.md)
  Solves the equation *Ax = b* for vectors of single-precision values, treating *A* as an operator and using the specified iterative method and preconditioner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:_:_:_:)-3aphv)*