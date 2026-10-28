# SparseSolve(_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Solves the system *AX = B* using the supplied double-precision factorization of *A*.

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
func SparseSolve(_ Factored: SparseOpaqueFactorization_Double, _ B: DenseMatrix_Double, _ X: DenseMatrix_Double)
```

```c
static void SparseSolve(SparseOpaqueFactorization_Double Factored, DenseMatrix_Double B, DenseMatrix_Double X);
```

## Discussion

Use this function to solve a system of linear equations using a factored coefficient matrix. The following figure shows two systems of equations where the coefficient matrix is sparse:

![A mathematical equation that has two stacked sets of three simultaneous equations on the left. Each equation has three unknowns. The same sets of simultaneous equations appear on the right as a single matrix equation, A x equals B. The single matrix equation consists of a three-by-three matrix multiplied by a three-by-two matrix that equals a three-by-two matrix.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3703887@2x.png)

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

// Create the right-hand-side matrix `B` (also holds the solution `X` on return).
var bValues: [Double] = [30, 35, 100,
                         300, 350, 1000]
let n = bValues.count

// Solve the system.
let xValues = [Double](unsafeUninitializedCapacity: n) {
    buffer, count in
    bValues.withUnsafeMutableBufferPointer { bPtr in
        let B = DenseMatrix_Double(rowCount: 3,
                                   columnCount: 2,
                                   columnStride: 3,
                                   attributes: SparseAttributes_t(),
                                   data: bPtr.baseAddress!)
        
        let X = DenseMatrix_Double(rowCount: 3,
                                   columnCount: 2,
                                   columnStride: 3,
                                   attributes: SparseAttributes_t(),
                                   data: buffer.baseAddress!)
        
        SparseSolve(factorization, B, X)
        
        count = n
    }
}
print(xValues) // Prints "[1.0, 2.0, 3.0, 10.0, 20.0, 30.0]".
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

// Create the right-hand-side matrix `B` and the solution matrix `X`.
double bValues[] = {30, 35, 100, 300, 350, 1000};
double xValues[6];

DenseMatrix_Double B = {
    .rowCount     = 3,
    .columnCount  = 2,
    .columnStride = 3,
    .attributes   = (SparseAttributes_t){0},
    .data         = bValues
};

DenseMatrix_Double X = {
    .rowCount     = 3,
    .columnCount  = 2,
    .columnStride = 3,
    .attributes   = (SparseAttributes_t){0},
    .data         = xValues
};

// Solve `AX = B`, writing the solution into `X`.
SparseSolve(factorization, B, X);

// Prints "[1, 2, 3, 10, 20, 30]".
printf("[%g, %g, %g, %g, %g, %g]\n",
      xValues[0], xValues[1], xValues[2],
      xValues[3], xValues[4], xValues[5]);

SparseCleanup(A);
SparseCleanup(factorization);
```

On return, `xValues` contains the values `[1.0, 2.0, 3.0, 10.0, 20.0, 30.0]`.

If the factorization is *A = QR*, the function returns the solution of minimum norm *‖ x ‖₂* for underdetermined systems.

If the factorization is *A = QR*, the function returns the least squares solution *minₓ ‖ AX - B ‖₂* for overdetermined systems.

If the factorization is [`SparseFactorizationCholeskyAtA`](./sparsefactorizationcholeskyata.md), the factorization is of *AᵀA*, and the solution that returns is for the system *AᵀAX = B*.

## Parameters

- `Factored`: The factorization of *A*.
- `B`: The right-hand-side, B.
- `X`: The matrix for returning solutions.

## See Also

### Out-of-place direct solving functions
- [func SparseSolve(SparseOpaqueFactorization_Float, DenseMatrix_Float, DenseMatrix_Float)](./sparsesolve%28_,_,_%29-2rxlq.md)
  Solves the system *AX = B* using the supplied single-precision factorization of *A*.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:_:)-3iav7)*