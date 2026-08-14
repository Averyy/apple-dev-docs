# SparseIterate(_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Performs a single iteration of the specified iterative method for single-precision matrices.

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
func SparseIterate(_ method: SparseIterativeMethod, _ iteration: Int32, _ converged: UnsafePointer<Bool>, _ state: UnsafeMutableRawPointer, _ ApplyOperator: @escaping (Bool, CBLAS_TRANSPOSE, DenseMatrix_Float, DenseMatrix_Float) -> Void, _ B: DenseMatrix_Float, _ R: DenseMatrix_Float, _ X: DenseMatrix_Float)
```

#### Discussion

Use this function to solve a system of linear equations using a factored coefficient matrix. This function provides complete control over each iteration, and you’re responsible for convergence tests and the number of iterations.

The following figure shows two systems of equations where the coefficient matrix is sparse:

![A mathematical equation that has two stacked sets of three simultaneous equations on the left. Each equation has three unknowns. The same sets of simultaneous equations appear on the right as a single matrix equation, A x equals B. The single matrix equation consists of a three-by-three matrix multiplied by a three-by-two matrix that equals a three-by-two matrix.](/images/com.apple.accelerate/media-3703928@2x.png)

The following code solves this system using the least squares minimum residual method:

```swift
/// Create the coefficient matrix _A_
let rowIndices: [Int32] =    [ 0,  1, 1,  2]
let columnIndices: [Int32] = [ 2,  0, 2,  1]
let aValues: [Float] =      [10, 20, 5, 50]

let rowCount = Int32(3)
let columnCount = Int32(3)

let A = SparseConvertFromCoordinate(rowCount, columnCount,
                                    aValues.count, 1,
                                    SparseAttributes_t(),
                                    rowIndices, columnIndices,
                                    aValues)

defer {
    SparseCleanup(A)
}

/// Define the size of the constants matrix, residuals matrix, and solution vectors.
let rhsCount = Int32(2)
let count = Int(rowCount * rhsCount)

/// Create the constants matrix, _B_ data.
let bData = UnsafeMutablePointer<Float>.allocate(capacity: count)
bData.initialize(from: [30, 35, 100,
                        300, 350, 1000], count: count)

/// Create the residual estimate matrix, _R_ data.
let rData = UnsafeMutablePointer<Float>.allocate(capacity: count)
rData.initialize(from: bData, count: count)

/// Create the solution vectors, _X_ data.
let xData = UnsafeMutablePointer<Float>.allocate(capacity: count)
xData.initialize(repeating: 0, count: count)

/// Create the state space.
let method = SparseLSMR()
let stateSize = SparseGetStateSize_Float(method, false,
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
                   X: DenseMatrix_Float,
                   Y: DenseMatrix_Float) {
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
    let B = DenseMatrix_Float(rowCount: rowCount,
                              columnCount: rhsCount,
                              columnStride: rowCount,
                              attributes: SparseAttributes_t(),
                              data: bData)
    
    let R = DenseMatrix_Float(rowCount: rowCount,
                              columnCount: rhsCount,
                              columnStride: rowCount,
                              attributes: SparseAttributes_t(),
                              data: rData)
    
    let X = DenseMatrix_Float(rowCount: rowCount,
                              columnCount: rhsCount,
                              columnStride: rowCount,
                              attributes: SparseAttributes_t(),
                              data: xData)
    
    SparseIterate(method,
                  iteration, converged,
                  state,
                  applyOperator,
                  B, R, X)
    
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
- `state`: A pointer to a state space with a size that [`SparseGetStateSize_Float(_:_:_:_:_:)`](sparsegetstatesize_float(_:_:_:_:_:).md) defines. Don’t alter the state space between iterations, and deallocate it after the final call to `SparseIterate`.
- `ApplyOperator`: The apply operator block to run. The block takes the following parameters: - **accumulate**: Indicates whether to perform `y += op(A)x` (if `true`), or `y = op(A)x` (if `false`).
- **trans**: Indicates whether `op(A)` is the application of *A*  if `CblasNoTrans`, or *Aᵀ* if `CblasTrans`.
- **x**: The vector to multiply.
- **y**: The vector for accumulating or storing the result.
- `B`: The right-hand-sides to solve for.
- `R`: The residual estimate. For the first entry, that is, when `iteration = 0`, set this to the residuals *b-Ax* (equal to `B` if `X = 0`). On return from each call with `iteration >= 0`, the first entries of each vector contain various estimates of norms to use in convergence testing. For CG and GMRES: - `R(0,j)` holds an estimate of *‖ b-Ax ‖₂* for the `j`-th right-hand-side. For LSMR: - `R(0,j)` holds an estimate of *‖ Aᵀ(b-Ax) ‖₂* for the `j`-th right-hand-side.
- `R(1,j)` holds an estimate of *‖ b-Ax ‖₂* for the `j`-th right-hand-side.
- `R(2,j)` holds an estimate of *‖ A ‖ꜰ*, the Frobenius norm of *A*, that the operation estimates using calculations from to the `j`-th right-hand-side.
- `R(3,j)` holds an estimate of *cond(A)*, the condition number of A, that the operation estimates using calculations from the `j`-th right-hand-side. The function may use other entries of `R` as a workspace. On return from a call with `iteration < 0`, the function returns the exact residual vector *b-Ax*.
- `X`: The current estimate of the solution vectors `X`. On entry with `iteration = 0`, this is an initial estimate for the solution. If no good estimate is available, use `X = 0.0`. Depending on the method, the function may not update `X` at each iteration. Make a call with `iteration < 0` after the function achieves convergence to update `X`.

## See Also

- [func SparseIterate(SparseIterativeMethod, Int32, UnsafePointer<Bool>, UnsafeMutableRawPointer, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Double, DenseMatrix_Double) -> Void, DenseMatrix_Double, DenseMatrix_Double, DenseMatrix_Double)](sparseiterate(_:_:_:_:_:_:_:_:)-c54n.md)
  Performs a single iteration of the specified iterative method for double-precision matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseiterate(_:_:_:_:_:_:_:_:)-1el7r)*