# SparseIterate(_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Performs a single iteration of the specified iterative method for double-precision matrices, applying a preconditioner.

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
func SparseIterate(_ method: SparseIterativeMethod, _ iteration: Int32, _ converged: UnsafePointer<Bool>, _ state: UnsafeMutableRawPointer, _ ApplyOperator: @escaping (Bool, CBLAS_TRANSPOSE, DenseMatrix_Double, DenseMatrix_Double) -> Void, _ B: DenseMatrix_Double, _ R: DenseMatrix_Double, _ X: DenseMatrix_Double, _ Preconditioner: SparseOpaquePreconditioner_Double)
```

#### Discussion

Use this function to solve a system of linear equations using a factored coefficient matrix. This function provides complete control over each iteration, and you’re responsible for convergence tests and the number of iterations.

The following figure shows two systems of equations where the coefficient matrix is sparse:

![A mathematical equation that has two stacked sets of three simultaneous equations on the left. Each equation has three unknowns. The same sets of simultaneous equations appear on the right as a single matrix equation, A x equals B. The single matrix equation consists of a three-by-three matrix multiplied by a three-by-two matrix that equals a three-by-two matrix.](/images/com.apple.accelerate/media-3703929@2x.png)

The following code solves this system by applying a diagonal scaling preconditioner and using the least squares minimum residual method:

```swift
/// Create the coefficient matrix _A_
let rowIndices: [Int32] =    [ 0,  1, 1,  2]
let columnIndices: [Int32] = [ 2,  0, 2,  1]
let aValues: [Double] =      [10, 20, 5, 50]

let rowCount = Int32(3)
let columnCount = Int32(3)

let A = SparseConvertFromCoordinate(rowCount, columnCount,
                                    aValues.count, 1,
                                    SparseAttributes_t(),
                                    rowIndices, columnIndices,
                                    aValues)
let preconditioner = SparseCreatePreconditioner(SparsePreconditionerDiagScaling,
                                                A)

defer {
    SparseCleanup(A)
    SparseCleanup(preconditioner)
}

/// Define the size of the right-hand-side matrix, residuals matrix, and solution vectors.
let rhsCount = Int32(2)
let count = Int(rowCount * rhsCount)

/// Create the constants matrix, _B_ data.
let bData = UnsafeMutablePointer<Double>.allocate(capacity: count)
bData.initialize(from: [30, 35, 100,
                        300, 350, 1000], count: count)

/// Create the residual estimate matrix, _R_ data.
let rData = UnsafeMutablePointer<Double>.allocate(capacity: count)
rData.initialize(from: bData, count: count)

/// Create the solution vectors, _X_ data.
let xData = UnsafeMutablePointer<Double>.allocate(capacity: count)
xData.initialize(repeating: 0, count: count)

/// Create the state space.
let method = SparseLSMR()
let stateSize = SparseGetStateSize_Double(method, true,
                                          rowCount, columnCount,
                                          rhsCount)
let state = UnsafeMutablePointer<Double>.allocate(capacity: stateSize)
state.initialize(repeating: 0, count: stateSize)

defer {
    bData.deallocate()
    rData.deallocate()
    xData.deallocate()
    state.deallocate()
}

/// Create the apply operator block.
func applyOperator(accumulate: Bool,
                   trans: CBLAS_TRANSPOSE,
                   X: DenseMatrix_Double,
                   Y: DenseMatrix_Double) {
    switch(accumulate, trans == CblasTrans) {
        case (false, false):
            SparseMultiply(A, X, Y)
        case (false, true):
            SparseMultiply(SparseGetTranspose(A), X, Y)
        case (true, false):
            SparseMultiplyAdd(A, X, Y)
        case (true, true):
            SparseMultiplyAdd(SparseGetTranspose(A), X, Y)
    }
}

var iteration = Int32(0)
var converged = [Bool](repeating: false,
                       count: Int(rhsCount))

while iteration >= 0 {
    /// If all right-hand-sides have converged, set `converge` 
    /// to a negative value to indicate the current iteration is final.
    if converged.allSatisfy({ $0 }) {
        iteration = -.max
    }
    
    print("Iteration:", iteration)
    let B = DenseMatrix_Double(rowCount: rowCount,
                               columnCount: rhsCount,
                               columnStride: rowCount,
                               attributes: SparseAttributes_t(),
                               data: bData)
    
    let R = DenseMatrix_Double(rowCount: rowCount,
                               columnCount: rhsCount,
                               columnStride: rowCount,
                               attributes: SparseAttributes_t(),
                               data: rData)
    
    let X = DenseMatrix_Double(rowCount: rowCount,
                               columnCount: rhsCount,
                               columnStride: rowCount,
                               attributes: SparseAttributes_t(),
                               data: xData)
    
    SparseIterate(method,
                  iteration, converged,
                  state,
                  applyOperator,
                  B, R, X,
                  preconditioner)
    
    /// Elements 1 and 4 of the residual estimate contain the least squares residual, _‖ b-Ax ‖₂_,
    /// for columns 0 and 1, respectively. Define a suitable tolerance for convergence testing.
    converged = [
        rData[1] < 1e-4,
        rData[4] < 1e-4
    ]
    
    iteration += 1
}
```

On return, x`Data` points to the values `[1.0, 2.0, 3.0, 10.0, 20.0, 30.0]`.

## Parameters

- `method`: The iterative method specification, such as the return value of [`SparseConjugateGradient()`](sparseconjugategradient().md). Note that this function ignores the options for convergence testing (for example, [`maxIterations`](sparselsmroptions/maxiterations.md), [`atol`](sparselsmroptions/atol.md), [`rtol`](sparselsmroptions/rtol.md)) because you’re responsible for convergence tests.
- `iteration`: The current iteration number, starting from `0`. If `iteration<0`, the function finalizes the current iteration, and updates the value of `X`. Note that this may force some methods to restart, and slow convergence.
- `converged`: The convergence status of each right-hand-side. Set `converged[j]` to `true` to indicate that the operation has converged the vector that it stores as column `j` of `X`, and the function must ignore it in this iteration.
- `state`: A pointer to a state space with a size that [`SparseGetStateSize_Double(_:_:_:_:_:)`](sparsegetstatesize_double(_:_:_:_:_:).md) defines. Don’t alter the state space between iterations, and deallocate it after the final call to `SparseIterate`.
- `ApplyOperator`: The apply operator block to run. The block takes the following parameters: - **accumulate**: Indicates whether to perform `y += op(A)x` (if `true`), or `y = op(A)x` (if `false`).
- **trans**: Indicates whether `op(A)` is the application of *A*  if `CblasNoTrans`, or *Aᵀ* if `CblasTrans`.
- **x**: The vector to multiply.
- **y**: The vector for accumulating or storing the result.
- `B`: The right-hand-sides to solve for.
- `R`: The residual estimate. For the first entry, that is, when `iteration = 0`, set this to the residuals *b-Ax* (equal to `B` if `X = 0`). On return from each call with `iteration >= 0`, the first entries of each vector contain various estimates of norms to use in convergence testing. For CG and GMRES: - `R(0,j)` holds an estimate of *‖ b-Ax ‖₂* for the `j`-th right-hand-side. For LSMR: - `R(0,j)` holds an estimate of *‖ Aᵀ(b-Ax) ‖₂* for the `j`-th right-hand-side.
- `R(1,j)` holds an estimate of *‖ b-Ax ‖₂* for the `j`-th right-hand-side.
- `R(2,j)` holds an estimate of *‖ A ‖ꜰ*, the Frobenius norm of *A*, which the operation estimates using calculations from the `j`-th right-hand-side.
- `R(3,j)` holds an estimate of *cond(A)*, the condition number of A, which the operation estimates using calculations from the `j`-th right-hand-side. The function may use other entries of `R` as a workspace. On return from a call with `iteration < 0`, the function returns the exact residual vector *b-Ax*.
- `X`: The current estimate of the solution vectors `X`. On entry with `iteration = 0`, this is an initial estimate for the solution. If no good estimate is available, use `X = 0.0`. Depending on the method, the function may not update `X` at each iteration. Make a call with `iteration < 0` after the function achieves convergence to update `X`.
- `Preconditioner`: The preconditioner to apply.

## See Also

- [func SparseIterate(SparseIterativeMethod, Int32, UnsafePointer<Bool>, UnsafeMutableRawPointer, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Float, DenseMatrix_Float) -> Void, DenseMatrix_Float, DenseMatrix_Float, DenseMatrix_Float, SparseOpaquePreconditioner_Float)](sparseiterate(_:_:_:_:_:_:_:_:_:)-1anay.md)
  Performs a single iteration of the specified iterative method for single-precision matrices, applying a preconditioner.
- [func SparseIterate(SparseIterativeMethod, Int32, UnsafePointer<Bool>, UnsafeMutableRawPointer, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double) -> Void, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double)](sparseiterate(_:_:_:_:_:_:_:_:)-315ym.md)
  Perform a single iteration of the specified iterative method for complex double values.
- [func SparseIterate(SparseIterativeMethod, Int32, UnsafePointer<Bool>, UnsafeMutableRawPointer, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float) -> Void, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float)](sparseiterate(_:_:_:_:_:_:_:_:)-9v7qh.md)
  Perform a single iteration of the specified iterative method for complex float values.
- [func SparseIterate(SparseIterativeMethod, Int32, UnsafePointer<Bool>, UnsafeMutableRawPointer, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double) -> Void, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double, SparseOpaquePreconditioner_Complex_Double)](sparseiterate(_:_:_:_:_:_:_:_:_:)-1wv28.md)
  Perform a single iteration of the specified iterative method for complex double values with preconditioner.
- [func SparseIterate(SparseIterativeMethod, Int32, UnsafePointer<Bool>, UnsafeMutableRawPointer, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float) -> Void, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float, SparseOpaquePreconditioner_Complex_Float)](sparseiterate(_:_:_:_:_:_:_:_:_:)-4td1l.md)
  Perform a single iteration of the specified iterative method for complex float values with preconditioner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseiterate(_:_:_:_:_:_:_:_:_:)-99ji7)*