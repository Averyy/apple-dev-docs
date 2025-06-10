# SparseOpaqueFactorization_Complex_Double

**Framework**: Accelerate  
**Kind**: struct

A semi-opaque type representing a matrix factorization in complex double.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct SparseOpaqueFactorization_Complex_Double
```

#### Overview

Use the `SparseCleanup` function to free resources held by these objects.

The object can be in one of the following states:

1. Something went wrong with symbolic factorization, nothing is valid. - indicated by `.symbolicFactorization.status < 0`
2. Symbolic factorization was good, but failed in numeric factorization initialization. - indicated by `.symbolicFactorization.status >= 0 && .status < 0 && .numericFactorization == NULL`
- symbolic factorization may be used for future calls.
3. Symbolic factorization was good, factor allocated/initialized correctly, but numeric factorization failed e.g. a Cholesky factorization of an indefinite matrix was attempted. - indicated by `.symbolicFactorization.status >= 0 && .status < 0 && .numericFactorization not NULL`
- user may pass this object to `SparseRefactor_Double` with a modified matrix
4. Symbolic and numeric factorizations are both good - indicated by `.status >= 0`

## Topics

### Initializers
- [init()](sparseopaquefactorization_complex_double/init.md)
- [init(status: SparseStatus_t, attributes: SparseAttributesComplex_t, symbolicFactorization: SparseOpaqueSymbolicFactorization, userFactorStorage: Bool, numericFactorization: UnsafeMutableRawPointer?, solveWorkspaceRequiredStatic: Int, solveWorkspaceRequiredPerRHS: Int)](sparseopaquefactorization_complex_double/init(status:attributes:symbolicfactorization:userfactorstorage:numericfactorization:solveworkspacerequiredstatic:solveworkspacerequiredperrhs:).md)
### Instance Properties
- [var attributes: SparseAttributesComplex_t](sparseopaquefactorization_complex_double/attributes.md)
  A type representing the attributes of a matrix.
- [var numericFactorization: UnsafeMutableRawPointer?](sparseopaquefactorization_complex_double/numericfactorization.md)
- [var solveWorkspaceRequiredPerRHS: Int](sparseopaquefactorization_complex_double/solveworkspacerequiredperrhs.md)
- [var solveWorkspaceRequiredStatic: Int](sparseopaquefactorization_complex_double/solveworkspacerequiredstatic.md)
- [var status: SparseStatus_t](sparseopaquefactorization_complex_double/status.md)
  Status field for a factorization.
- [var symbolicFactorization: SparseOpaqueSymbolicFactorization](sparseopaquefactorization_complex_double/symbolicfactorization.md)
  A semi-opaque type representing symbolic matrix factorization.
- [var userFactorStorage: Bool](sparseopaquefactorization_complex_double/userfactorstorage.md)

## See Also

- [Solving systems using direct methods](solving-systems-using-direct-methods.md)
  Use direct methods to solve systems of equations where the coefficient matrix is sparse.
- [struct SparseOpaqueFactorization_Double](sparseopaquefactorization_double.md)
  A structure that represents the factorization of a matrix of double-precision, floating-point values.
- [struct SparseOpaqueFactorization_Float](sparseopaquefactorization_float.md)
  A structure that represents the factorization of a matrix of single-precision, floating-point values.
- [struct SparseOpaqueFactorization_Complex_Float](sparseopaquefactorization_complex_float.md)
  A semi-opaque type representing a matrix factorization in complex float.
- [Sparse Matrix Factor Functions](sparse-matrix-factor-functions.md)
  Compute the factorization of a matrix.
- [Sparse Direct Solving Functions (Matrix RHS)](sparse-direct-solving-functions-matrix-rhs.md)
  Solve a system with a right-hand-side dense matrix using a factored sparse coefficient matrix.
- [Sparse Direct Solving Functions (Vector RHS)](sparse-direct-solving-functions-vector-rhs.md)
  Solve a system with a right-hand-side dense vector using a factored sparse coefficient matrix.
- [Sparse Symbolic Factorization Functions](sparse-symbolic-factorization-functions.md)
  Calculate the symbolic factorization of a matrix, and solve systems using precalculated symbolic factorizations.
- [Sparse Refactor Functions](sparse-refactor-functions.md)
  Recompute a factorization using the numerical data from a matrix.
- [Subfactor Functions](subfactor-functions.md)
  Extract and work with subfactors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquefactorization_complex_double)*