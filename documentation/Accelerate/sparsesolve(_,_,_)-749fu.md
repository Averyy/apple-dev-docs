# SparseSolve(_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Solves the system *AX = B* using the supplied single-precision factorization of *A*, in place and without any internal memory allocations.

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
func SparseSolve(_ Factored: SparseOpaqueFactorization_Float, _ XB: DenseMatrix_Float, _ workspace: UnsafeMutableRawPointer)
```

```c
static void SparseSolve(SparseOpaqueFactorization_Float Factored, DenseMatrix_Float XB, void *workspace);
```

## Discussion

Use this function to solve a system of linear equations using a factored coefficient matrix. In cases where your code calls the function frequently, create and manage the workspace that the Sparse Solvers library uses and reuse it across function calls. Reusing a workspace prevents the Sparse Solvers library from allocating the temporary storage with each call.

The following figure shows two systems of equations where the coefficient matrix is sparse:

![A mathematical equation that has two stacked sets of three simultaneous equations on the left. Each equation has three unknowns. The same sets of simultaneous equations appear on the right as a single matrix equation, A x equals B. The single matrix equation consists of a three-by-three matrix multiplied by a three-by-two matrix that equals a three-by-two matrix.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3703890@2x.png)

The following code solves this system with a QR factorization of the coefficient matrix:

**Swift**:

```swift
// Create the coefficient matrix `A` from coordinate (COO) arrays.
let rowIndices: [Int32] =    [ 0,  1, 1,  2]
let columnIndices: [Int32] = [ 2,  0, 2,  1]
let aValues: [Float] =      [10, 20, 5, 50]

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

// Allocate the workspace.
let nrhs = Int(A.structure.columnCount)
let byteCount = factorization.solveWorkspaceRequiredStatic +
                    nrhs * factorization.solveWorkspaceRequiredPerRHS
let workspace = UnsafeMutableRawPointer.allocate(
    byteCount: byteCount,
    alignment: MemoryLayout<Float>.alignment)
defer {
    workspace.deallocate()
}

// Create the right-hand-side matrix `B` (also holds the solution `X` on return).
var bValues: [Float] = [30, 35, 100,
                        300, 350, 1000]

// Solve the system.
bValues.withUnsafeMutableBufferPointer { bPtr in
    let XB = DenseMatrix_Float(rowCount: 3,
                               columnCount: 2,
                               columnStride: 3,
                               attributes: SparseAttributes_t(),
                               data: bPtr.baseAddress!)
    
    SparseSolve(factorization, XB,
                workspace)
}
print(bValues) // Prints "[1.0, 2.0, 3.0, 10.0, 20.0, 30.0]".
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

// Compute the factors of `A` using a QR decomposition.
SparseOpaqueFactorization_Float factorization = SparseFactor(SparseFactorizationQR, A);

// Allocate workspace.
size_t byteCount = factorization.solveWorkspaceRequiredStatic +
                   2 * factorization.solveWorkspaceRequiredPerRHS;
void *workspace = malloc(byteCount);

// Create the right-hand-side matrix `B` (also holds the solution `X` on return).
float bValues[] = {30, 35, 100, 300, 350, 1000};

DenseMatrix_Float XB = {
    .rowCount     = 3,
    .columnCount  = 2,
    .columnStride = 3,
    .attributes   = (SparseAttributes_t){0},
    .data         = bValues
};

// Solve `AX = B` in place using the supplied workspace.
SparseSolve(factorization, XB, workspace);

// Prints "[1, 2, 3, 10, 20, 30]".
printf("[%g, %g, %g, %g, %g, %g]\n",
      bValues[0], bValues[1], bValues[2],
      bValues[3], bValues[4], bValues[5]);

free(workspace);
SparseCleanup(A);
SparseCleanup(factorization);
```

On return, `bValues` contains the values `[1.0, 2.0, 3.0, 10.0, 20.0, 30.0]`.

If the factorization is *A = QR*, the function returns the solution of minimum norm *‖ x ‖₂* for underdetermined systems.

If the factorization is *A = QR*, the function returns the least squares solution *minₓ ‖ AX - B ‖₂* for overdetermined systems.

If the factorization is [`SparseFactorizationCholeskyAtA`](./sparsefactorizationcholeskyata.md), the factorization is of *AᵀA*, and the solution that returns is for the system *AᵀAX = B*.

## Parameters

- `Factored`: The factorization of *A*.
- `XB`: On entry, the right-hand-side, *B*. On return, the solution vectors *X*. If *A* has dimension *m x n*, *XB* must have dimension *k x nrhs*, where *k = max(m,n)* and *nrhs* is the number of right-hand-sides to find solutions for.
- `workspace`: The scratch space of size [`solveWorkspaceRequiredStatic`](./sparseopaquefactorization_float/solveworkspacerequiredstatic.md) `+` `nrhs` `*` [`solveWorkspaceRequiredPerRHS`](./sparseopaquefactorization_float/solveworkspacerequiredperrhs.md).

## See Also

### In-place direct solving functions with user-defined workspace
- [func SparseSolve(SparseOpaqueFactorization_Double, DenseMatrix_Double, UnsafeMutableRawPointer)](./sparsesolve%28_,_,_%29-l2kw.md)
  Solves the system *AX = B* using the supplied double-precision factorization of *A*, in place and without any internal memory allocations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:_:)-749fu)*