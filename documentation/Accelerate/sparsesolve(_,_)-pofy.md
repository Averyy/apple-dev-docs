# SparseSolve(_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Solves the system *Ax = x* using the supplied double-precision factorization of *A*.

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
func SparseSolve(_ Factored: SparseOpaqueFactorization_Double, _ xb: DenseVector_Double)
```

```c
static void SparseSolve(SparseOpaqueFactorization_Double Factored, DenseVector_Double xb);
```

## Discussion

Use this function to solve a system of linear equations using a factored coefficient matrix. The following figure shows a system of equations where the coefficient matrix is sparse:

![A mathematical equation that has one set of three simultaneous equations on the left. Each equation has three unknowns. The same set of simultaneous equations appears on the right as a single matrix equation, A x equals B. The single matrix equation consists of a three-by-three matrix multiplied by a three-element column matrix that equals a three-element column matrix.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3703893@2x.png)

The following code solves this system with a QR factorization of the coefficient matrix:

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

// Compute the factors of `A` using a QR decomposition.
let factorization = SparseFactor(SparseFactorizationQR, A)

defer {
    SparseCleanup(A)
    SparseCleanup(factorization)
}

// Create the right-hand-side vector `b` (also holds the solution on return).
var bValues: [Double] = [30, 35, 100]

// Solve the system.
bValues.withUnsafeMutableBufferPointer { bPtr in
    let xb = DenseVector_Double(count: 3,
                               data: bPtr.baseAddress!)
    
    SparseSolve(factorization, xb)
}
print(bValues) // Prints "[1.0, 2.0, 3.0]".
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

// Compute the factors of `A` using a QR decomposition.
SparseOpaqueFactorization_Double factorization = SparseFactor(SparseFactorizationQR, A);

// Create the right-hand-side vector `b` (also holds the solution on return).
double bValues[] = {30, 35, 100};

DenseVector_Double xb = {
    .count = 3,
    .data  = bValues
};

// Solve `Ax = b` in place.
SparseSolve(factorization, xb);

// Prints "[1, 2, 3]".
printf("[%g, %g, %g]\n", bValues[0], bValues[1], bValues[2]);

SparseCleanup(A);
SparseCleanup(factorization);
```

On return, `bValues` contains the values `[1.0, 2.0, 3.0]`.

If the factorization is *A = QR*, the function returns the solution of minimum norm *‖ x ‖₂* for underdetermined systems.

If the factorization is *A = QR*, the function returns the least squares solution *minₓ ‖ AX - B ‖₂* for overdetermined systems.

If the factorization is [`SparseFactorizationCholeskyAtA`](./sparsefactorizationcholeskyata.md), the factorization is of *AᵀA*, and the solution that returns is for the system *AᵀAX = B*.

## Parameters

- `Factored`: The factored matrix to solve.
- `xb`: On input, the vector *b*. On return, the function overwrites with the vector *x*. If *A* has dimension *m x n*, this parameter must have length *k*, where *k = max(m,n)*.

## See Also

### In-place direct solving functions
- [func SparseSolve(SparseOpaqueFactorization_Float, DenseVector_Float)](./sparsesolve%28_,_%29-60ngw.md)
  Solves the system *Ax = b* using the supplied single-precision factorization of *A*, in place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:)-pofy)*