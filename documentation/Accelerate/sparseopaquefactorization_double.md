# SparseOpaqueFactorization_Double

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A structure that represents the factorization of a matrix of double-precision, floating-point values.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct SparseOpaqueFactorization_Double
```

```c
typedef struct { ... } SparseOpaqueFactorization_Double;
```

## Mentions

- [Solving systems using direct methods](./solving-systems-using-direct-methods.md)

#### Overview

Use the [`SparseCleanup(_:)`](./sparsecleanup%28_%29-3cnxt.md) function to free resources that these objects hold.

An object can be in one of the following states:

| **Something is wrong with symbolic factorization, nothing is valid.** | Indication: [`symbolicFactorization`](./sparseopaquefactorization_float/symbolicfactorization.md).[`status`](./sparseopaquesymbolicfactorization/status.md) `< 0` |
| --- | --- |
| **Symbolic factorization is good, but fails in numeric factorization initialization.** | Indication: [`symbolicFactorization`](./sparseopaquefactorization_float/symbolicfactorization.md).[`status`](./sparseopaquesymbolicfactorization/status.md) `>= 0 &&` [`status`](./sparseopaquefactorization_double/status.md) `< 0 &&` [`numericFactorization`](./sparseopaquefactorization_double/numericfactorization.md) `== NULL` ![](https://developer.apple.com/tutorials/images/com.apple.accelerate/spacer.png) You can use symbolic factorization for future calls. |
| **Symbolic factorization is good, factor allocation and initialization are correct, but numeric factorization fails.** ![](https://developer.apple.com/tutorials/images/com.apple.accelerate/spacer.png) For example, the system attempts a Cholesky factorization of an indefinite matrix. | Indication: [`symbolicFactorization`](./sparseopaquefactorization_float/symbolicfactorization.md).[`status`](./sparseopaquesymbolicfactorization/status.md) `>= 0 &&` [`status`](./sparseopaquefactorization_double/status.md) `< 0 &&` [`numericFactorization`](./sparseopaquefactorization_double/numericfactorization.md) `not NULL`  ![](https://developer.apple.com/tutorials/images/com.apple.accelerate/spacer.png) You may pass this object to [`SparseRefactor(_:_:)`](./sparserefactor%28_,_%29-8vrf5.md) with a modified matrix. |
| **Symbolic and numeric factorizations are both good.** | Indication: [`status`](./sparseopaquefactorization_double/status.md) `>= 0` |

## Topics

### Creating an Opaque Factorization
- [init()](./sparseopaquefactorization_double/init%28%29.md)
  Creates a new opaque factorization.
- [init(status: SparseStatus_t, attributes: SparseAttributes_t, symbolicFactorization: SparseOpaqueSymbolicFactorization, userFactorStorage: Bool, numericFactorization: UnsafeMutableRawPointer?, solveWorkspaceRequiredStatic: Int, solveWorkspaceRequiredPerRHS: Int)](./sparseopaquefactorization_double/init%28status,attributes,symbolicfactorization,userfactorstorage,numericfactorization,solveworkspacerequiredstatic,solveworkspacerequiredperrhs%29.md)
  Creates a new opaque factorization with the specified parameters.
### Instance Properties
- [var attributes: SparseAttributes_t](./sparseopaquefactorization_double/attributes.md)
  The attributes of a factorization object.
- [var numericFactorization: UnsafeMutableRawPointer?](./sparseopaquefactorization_double/numericfactorization.md)
  The pointer to a private internal representation of a numeric factor.
- [var solveWorkspaceRequiredPerRHS: Int](./sparseopaquefactorization_double/solveworkspacerequiredperrhs.md)
  The required size of the per-right-hand-side workspace for a call to a sparse solve function.
- [var solveWorkspaceRequiredStatic: Int](./sparseopaquefactorization_double/solveworkspacerequiredstatic.md)
  The required size of the static workspace for a call to a sparse solve function.
- [var status: SparseStatus_t](./sparseopaquefactorization_double/status.md)
  The status of the factorization object.
- [var symbolicFactorization: SparseOpaqueSymbolicFactorization](./sparseopaquefactorization_double/symbolicfactorization.md)
  The symbolic factorization that this numeric factorization depends on.
- [var userFactorStorage: Bool](./sparseopaquefactorization_double/userfactorstorage.md)
  A Boolean value that indicates whether user-provided storage backs this object.

## See Also

### Solving systems with direct sparse methods
- [Solving systems using direct methods](./solving-systems-using-direct-methods.md)
  Use direct methods to solve systems of equations where the coefficient matrix is sparse.
- [struct SparseOpaqueFactorization_Float](./sparseopaquefactorization_float.md)
  A structure that represents the factorization of a matrix of single-precision, floating-point values.
- [struct SparseOpaqueFactorization_Complex_Double](./sparseopaquefactorization_complex_double.md)
  A semi-opaque type representing a matrix factorization in complex double.
- [struct SparseOpaqueFactorization_Complex_Float](./sparseopaquefactorization_complex_float.md)
  A semi-opaque type representing a matrix factorization in complex float.
- [Sparse Matrix Factor Functions](./sparse-matrix-factor-functions.md)
  Compute the factorization of a matrix.
- [Sparse Direct Solving Functions (Matrix RHS)](./sparse-direct-solving-functions-matrix-rhs.md)
  Solve a system with a right-hand-side dense matrix using a factored sparse coefficient matrix.
- [Sparse Direct Solving Functions (Vector RHS)](./sparse-direct-solving-functions-vector-rhs.md)
  Solve a system with a right-hand-side dense vector using a factored sparse coefficient matrix.
- [Sparse Symbolic Factorization Functions](./sparse-symbolic-factorization-functions.md)
  Calculate the symbolic factorization of a matrix, and solve systems using precalculated symbolic factorizations.
- [Sparse Refactor Functions](./sparse-refactor-functions.md)
  Recompute a factorization using the numerical data from a matrix.
- [Subfactor Functions](./subfactor-functions.md)
  Extract and work with subfactors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquefactorization_double)*