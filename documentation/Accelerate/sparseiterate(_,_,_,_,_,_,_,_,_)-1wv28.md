# SparseIterate(_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Perform a single iteration of the specified iterative method for complex double values with preconditioner.

**Availability**:
- iOS 18.5+
- iPadOS 18.5+
- Mac Catalyst 18.5+
- macOS 15.5+
- tvOS 18.5+
- visionOS 2.5+
- watchOS 11.5+

## Declaration

```swift
func SparseIterate(_ method: SparseIterativeMethod, _ iteration: Int32, _ converged: UnsafePointer<Bool>, _ state: UnsafeMutableRawPointer, _ ApplyOperator: @escaping (Bool, CBLAS_TRANSPOSE, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double) -> Void, _ B: DenseMatrix_Complex_Double, _ R: DenseMatrix_Complex_Double, _ X: DenseMatrix_Complex_Double, _ Preconditioner: SparseOpaquePreconditioner_Complex_Double)
```

```c
static void SparseIterate(SparseIterativeMethod method, int iteration, const _Bool *converged, void *state, void (^ApplyOperator)(bool accumulate, enum CBLAS_TRANSPOSE trans, DenseMatrix_Complex_Double X, DenseMatrix_Complex_Double Y), DenseMatrix_Complex_Double B, DenseMatrix_Complex_Double R, DenseMatrix_Complex_Double X, SparseOpaquePreconditioner_Complex_Double Preconditioner);
```

## Parameters

- `method`: (Input) Iterative method specification, eg return value of `SparseConjugateGradient()`.

  ```
   Note that the options related to convergence testing (e.g.
   `maxIterations`, `atol`, `rtol`) are ignored as convergence tests must be
   performed by the user.
  ```
- `iteration`: (Input) The current iteration number, starting from 0. If `iteration<0`, then the current iterate is finalised, and the value of `X` is updated (note that this may force some methods to restart, slowing convergence).
- `converged`: (Input) Convergence status of each solution vector. `converged[j]=true` indicates that the vector stored as column `j` of `X` has converged, and it should be ignored in this iteration.
- `state`: (Input/Output) A pointer to a state-space of size returned by `SparseGetStateSize_Complex_Double()`. This memory must be 16-byte aligned (any allocation returned by `malloc()` has this property). It must not be altered by the user between iterations, but may be safely discarded after the final call to `SparseIterate()`.
- `ApplyOperator`: `ApplyOperator(accumulate, trans, X, Y)` should perform the operation `Y = op(A)X` if `accumulate` is `false`, or `Y += op(A)X` if `accumulate` is `true`.

  - **`accumulate`**: (input) Indicates whether to perform `Y += op(A)X` (if true) or `Y = op(A)X` (if false).
  - **`trans`**: (input) Indicates whether `op(A)` is the application of `A` (`trans=CblasNoTrans`) or `A^T` (`trans=CblasTrans`).
  - **`X`**: The matrix to multiply.
  - **`Y`**: The matrix in which to accumulate or store the result.
- `B`: (Input) The right-hand sides to solve for.
- `R`: (Output) Residual estimate. On entry with `iteration=0`, it must hold the residuals `b-Ax` (equal to `B` if `X=0`). On return from each call with `iteration>=0`, the first entry(s) of each vector contain various estimates of norms to be used in convergence testing.

  - **For CG and GMRES**: `R(0,j) `holds an estimate of` || b-Ax ||_2` for the j-th rhs.
  - **For LSMR - `R(0,j)`**: `R(0,j)` holds an estimate of` || A^T(b-Ax) ||_2` for the j-th rhs.
  - **For LSMR  - `R(1,j)`**: `R(1,j)` holds an estimate of` || b-Ax ||_2` for the j-th rhs.
  - **For LSMR - `R(2,j)`**: `R(2,j)` holds an estimate of `|| A ||_F`, the Frobenius norm of `A`, estimated using calculations related to the j-th rhs.
  - **For LSMR - `R(3,j)`**: `R(3,j) `holds an estimate of `cond(A)`, the condition number of `A`, estimated using calculations related to the j-th rhs.

    Other entries of `R` may be used by the routine as a workspace. On return from a call with `iteration<0`, the exact residual vector b-Ax is returned.
- `X`: (Input/Output) The current estimate of the solution vectors X. On entry with iteration=0, this should be an initial estimate for the solution. If no good estimate is available, use X = 0.0. Depending on the method used, X may not be updated at each iteration, or may be used to store some other vector. The user should make a call with iteration<0 once convergence has been achieved to bring X up to date.
- `Preconditioner`: (Input) Preconditioner to apply.

## See Also

### Sparse Iterate Functions with Preconditioner
- [func SparseIterate(SparseIterativeMethod, Int32, UnsafePointer<Bool>, UnsafeMutableRawPointer, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Double, DenseMatrix_Double) -> Void, DenseMatrix_Double, DenseMatrix_Double, DenseMatrix_Double, SparseOpaquePreconditioner_Double)](./sparseiterate%28_,_,_,_,_,_,_,_,_%29-99ji7.md)
  Performs a single iteration of the specified iterative method for double-precision matrices, applying a preconditioner.
- [func SparseIterate(SparseIterativeMethod, Int32, UnsafePointer<Bool>, UnsafeMutableRawPointer, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Float, DenseMatrix_Float) -> Void, DenseMatrix_Float, DenseMatrix_Float, DenseMatrix_Float, SparseOpaquePreconditioner_Float)](./sparseiterate%28_,_,_,_,_,_,_,_,_%29-1anay.md)
  Performs a single iteration of the specified iterative method for single-precision matrices, applying a preconditioner.
- [func SparseIterate(SparseIterativeMethod, Int32, UnsafePointer<Bool>, UnsafeMutableRawPointer, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double) -> Void, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double)](./sparseiterate%28_,_,_,_,_,_,_,_%29-315ym.md)
  Perform a single iteration of the specified iterative method for complex double values.
- [func SparseIterate(SparseIterativeMethod, Int32, UnsafePointer<Bool>, UnsafeMutableRawPointer, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float) -> Void, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float)](./sparseiterate%28_,_,_,_,_,_,_,_%29-9v7qh.md)
  Perform a single iteration of the specified iterative method for complex float values.
- [func SparseIterate(SparseIterativeMethod, Int32, UnsafePointer<Bool>, UnsafeMutableRawPointer, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float) -> Void, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float, SparseOpaquePreconditioner_Complex_Float)](./sparseiterate%28_,_,_,_,_,_,_,_,_%29-4td1l.md)
  Perform a single iteration of the specified iterative method for complex float values with preconditioner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseiterate(_:_:_:_:_:_:_:_:_:)-1wv28)*