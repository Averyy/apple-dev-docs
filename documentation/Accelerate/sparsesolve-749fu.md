# SparseSolve(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Solves the system  using the supplied single-precision factorization of , in place and without any internal memory allocations.

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

#### Discussion

Use this function to solve a system of linear equations using a factored coefficient matrix. In cases where your code calls the function frequently, create and manage the workspace that the Sparse Solvers library uses and reuse it across function calls. Reusing a workspace prevents the Sparse Solvers library from allocating the temporary storage with each call.

The following figure shows two systems of equations where the coefficient matrix is sparse:

![A mathematical equation that has two stacked sets of three simultaneous equations on the left. Each equation has three unknowns. The same sets of simultaneous equations appear on the right as a single matrix equation, A x equals B. The single matrix equation consists of a three-by-three matrix multiplied by a three-by-two matrix that equals a three-by-two matrix.](https://docs-assets.developer.apple.com/published/f418105a3665a60546bc23d6a8dd3f50/media-3703890%402x.png)

The following code solves this system with a QR factorization of the coefficient matrix:

```swift
/// Create the coefficient matrix _A_.
let rowIndices: [Int32] =    [ 0,  1, 1,  2]
let columnIndices: [Int32] = [ 2,  0, 2,  1]
let aValues: [Float] =      [10, 20, 5, 50]

let A = SparseConvertFromCoordinate(3, 3,
                                    4, 1,
                                    SparseAttributes_t(),
                                    rowIndices, columnIndices,
                                    aValues)

/// Factorize _A_.
let factorization = SparseFactor(SparseFactorizationQR, A)

defer {
    SparseCleanup(A)
    SparseCleanup(factorization)
}

/// Create the workspace.
let nrhs = Int(A.structure.columnCount)
let byteCount = factorization.solveWorkspaceRequiredStatic +
                    nrhs * factorization.solveWorkspaceRequiredPerRHS
let workspace = UnsafeMutableRawPointer.allocate(
    byteCount: byteCount,
    alignment: MemoryLayout<Float>.alignment)
defer {
    workspace.deallocate()
}

/// Create the right-hand-side matrix, _B_.
var bValues: [Float] = [30, 35, 100,
                        300, 350, 1000]

/// Solve the system.
bValues.withUnsafeMutableBufferPointer { bPtr in
    let XB = DenseMatrix_Float(rowCount: 3,
                               columnCount: 2,
                               columnStride: 3,
                               attributes: SparseAttributes_t(),
                               data: bPtr.baseAddress!)
    
    SparseSolve(factorization, XB,
                workspace)
}
```

On return, `bValues` contains the values `[1.0, 2.0, 3.0, 10.0, 20.0, 30.0]`.

If the factorization is , the function returns the solution of minimum norm  for underdetermined systems.

If the factorization is , the function returns the least squares solution  for overdetermined systems.

If the factorization is [`SparseFactorizationCholeskyAtA`](sparsefactorizationcholeskyata.md), the factorization is of , and the solution that returns is for the system .

## Parameters

- `Factored`: The factorization of  .
- `XB`: On entry, the right-hand-side,  . On return, the solution vectors  . If   has dimension  ,   must have dimension  , where   and   is the number of right-hand-sides to find solutions for.
- `workspace`: The scratch space of size          .

## See Also

- [func SparseSolve(SparseOpaqueFactorization_Double, DenseMatrix_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-l2kw.md)
  Solves the system  using the supplied double-precision factorization of , in place and without any internal memory allocations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:_:)-749fu)*