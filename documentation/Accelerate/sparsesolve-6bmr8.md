# SparseSolve(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Solves the system *Ax = b* using the supplied single-precision factorization of *A*, without any internal memory allocations.

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
func SparseSolve(_ Factored: SparseOpaqueFactorization_Float, _ b: DenseVector_Float, _ x: DenseVector_Float, _ workspace: UnsafeMutableRawPointer)
```

#### Discussion

Use this function to solve a system of linear equations using a factored coefficient matrix. In cases where your code calls the function frequently, create and manage the workspace that the Sparse Solvers library uses and reuse it across function calls. Reusing a workspace prevents the Sparse Solvers library from allocating the temporary storage with each call.

The following figure shows two systems of equations where the coefficient matrix is sparse:

![A mathematical equation that has one set of three simultaneous equations on the left. Each equation has three unknowns. The same set of simultaneous equations appears on the right as a single matrix equation, A x equals B. The single matrix equation consists of a three-by-three matrix multiplied by a three-element column matrix that equals a three-element column matrix.](/images/com.apple.accelerate/media-3703896@2x.png)

The following code solves this system with a QR factorization of the coefficient matrix:

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

// Compute the factors of `A` using a QR decomposition.
let factorization = SparseFactor(SparseFactorizationQR, A)

defer {
    SparseCleanup(A)
    SparseCleanup(factorization)
}

// Allocate the workspace.
let byteCount = factorization.solveWorkspaceRequiredStatic +
                    factorization.solveWorkspaceRequiredPerRHS
let workspace = UnsafeMutableRawPointer.allocate(
    byteCount: byteCount,
    alignment: MemoryLayout<Float>.alignment)
defer {
    workspace.deallocate()
}

// Create the right-hand-side vector `b` (also holds the solution on return).
var bValues: [Float] = [30, 35, 100]
let n = bValues.count

// Solve the system.
let xValues = [Float](unsafeUninitializedCapacity: n) {
    buffer, count in
    
    bValues.withUnsafeMutableBufferPointer { bPtr in
        
        let b = DenseVector_Float(count: 3,
                                  data: bPtr.baseAddress!)
        let x = DenseVector_Float(count: 3,
                                  data: buffer.baseAddress!)
        
        SparseSolve(factorization, b, x,
                    workspace)
        
        count = n
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

// Compute the factors of `A` using a QR decomposition.
SparseOpaqueFactorization_Float factorization = SparseFactor(SparseFactorizationQR, A);

// Allocate workspace.
size_t byteCount = factorization.solveWorkspaceRequiredStatic +
                   factorization.solveWorkspaceRequiredPerRHS;
void *workspace = malloc(byteCount > 0 ? byteCount : 1);

// Create the right-hand-side vector `b` and solution vector `x`.
float bValues[] = {30, 35, 100};
float xData[3]  = {0};

DenseVector_Float b = {
    .count = 3,
    .data  = bValues
};

DenseVector_Float x = {
    .count = 3,
    .data  = xData
};

// Solve `Ax = b`, writing the result into `x`.
SparseSolve(factorization, b, x, workspace);

// Prints "[1, 2, 3]".
printf("[%g, %g, %g]\n", xData[0], xData[1], xData[2]);

free(workspace);
SparseCleanup(A);
SparseCleanup(factorization);
```

On return, x`Values` contains the values `[1.0, 2.0, 3.0]`.

If the factorization is *A = QR*, the function returns the solution of minimum norm *‖ x ‖₂* for underdetermined systems.

If the factorization is *A = QR*, the function returns the least squares solution *minₓ ‖ AX - B ‖₂* for overdetermined systems.

If the factorization is [`SparseFactorizationCholeskyAtA`](sparsefactorizationcholeskyata.md), the factorization is of *AᵀA*, and the solution that returns is for the system *AᵀAX = B*.

## Parameters

- `Factored`: The factored matrix to solve.
- `b`: The vector *b*.
- `x`: The vector *x*.
- `workspace`: The scratch space of size [`solveWorkspaceRequiredStatic`](sparseopaquefactorization_float/solveworkspacerequiredstatic.md) `+ nrhs *` [`solveWorkspaceRequiredPerRHS`](sparseopaquefactorization_float/solveworkspacerequiredperrhs.md).

## See Also

- [func SparseSolve(SparseOpaqueFactorization_Double, DenseVector_Double, DenseVector_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-7k9ll.md)
  Solves the system *Ax = b* using the supplied double-precision factorization of *A*, without any internal memory allocations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:_:_:)-6bmr8)*