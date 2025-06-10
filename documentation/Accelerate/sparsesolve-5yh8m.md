# SparseSolve(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Solves the equation  for matrices of double-precision values using the specified iterative method and opaque preconditioner.

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
func SparseSolve(_ method: SparseIterativeMethod, _ A: SparseMatrix_Double, _ B: DenseMatrix_Double, _ X: DenseMatrix_Double, _ Preconditioner: SparseOpaquePreconditioner_Double) -> SparseIterativeStatus_t
```

#### Return Value

A [`SparseIterativeStatus_t`](sparseiterativestatus_t.md) enumeration that represents the status of the iterative solve.

#### Discussion

Use this function to solve a system of linear equations using a factored coefficient matrix. Preconditioning the coefficient matrix can reduce the number of iterations the function requires to converge the system.

The following figure shows two systems of equations where the coefficient matrix is sparse:

![A mathematical equation that has two stacked sets of three simultaneous equations on the left. Each equation has three unknowns. The same sets of simultaneous equations appear on the right as a single matrix equation, A x equals B. The single matrix equation consists of a three-by-three matrix multiplied by a three-by-two matrix that equals a three-by-two matrix. ](https://docs-assets.developer.apple.com/published/f418105a3665a60546bc23d6a8dd3f50/media-3743131%402x.png)

The following code solves this system by applying a diagonal scaling preconditioner and using the least squares minimum residual method:

```swift
/// Create the coefficient matrix _A_.
let rowIndices: [Int32] =    [ 0,  1, 1,  2]
let columnIndices: [Int32] = [ 2,  0, 2,  1]
let aValues: [Double] =      [10, 20, 5, 50]

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

/// Create the right-hand-side matrix, _B_.
var bValues: [Double] = [30, 35, 100,
                         300, 350, 1000]
let n = bValues.count

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
        
        SparseSolve(SparseLSMR(),
                    A, B, X,
                    preconditioner)
        count = n
    }
}
```

On return, x`Values` contains the values `[1.0, 2.0, 3.0, 10.0, 20.0, 30.0]`.

## Parameters

- `method`: The iterative method.
- `A`: The matrix  .
- `B`: The matrix  .
- `X`: The matrix  .
- `Preconditioner`: The preconditioner to apply.

## See Also

- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Float, DenseMatrix_Float, DenseMatrix_Float, SparseOpaquePreconditioner_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-7vrh0.md)
  Solves the equation  for matrices of single-precision values using the specified iterative method and opaque preconditioner.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Double, DenseMatrix_Double, DenseMatrix_Double, SparsePreconditioner_t) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-5d7vf.md)
  Solves the equation  for matrices of double-precision values using the specified iterative method and preconditioner type.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Float, DenseMatrix_Float, DenseMatrix_Float, SparsePreconditioner_t) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-7apig.md)
  Solves the equation  for matrices of single-precision values using the specified iterative method and preconditioner type.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Double, DenseMatrix_Double) -> Void, DenseMatrix_Double, DenseMatrix_Double, SparseOpaquePreconditioner_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-8nfbc.md)
  Solves the equation  for matrices of double-precision values, treating  as an operator and using the specified iterative method.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Float, DenseMatrix_Float) -> Void, DenseMatrix_Float, DenseMatrix_Float, SparseOpaquePreconditioner_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-80ri4.md)
  Solves the equation  for matrices of single-precision values, treating  as an operator and using the specified iterative method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:_:_:_:)-5yh8m)*