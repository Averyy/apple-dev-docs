# SparseOpaqueFactorization_Complex_Float

**Framework**: Accelerate  
**Kind**: struct

A semi-opaque type representing a matrix factorization in complex float.

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
struct SparseOpaqueFactorization_Complex_Float
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
- [init()](sparseopaquefactorization_complex_float/init.md)
- [init(status: SparseStatus_t, attributes: SparseAttributesComplex_t, symbolicFactorization: SparseOpaqueSymbolicFactorization, userFactorStorage: Bool, numericFactorization: UnsafeMutableRawPointer?, solveWorkspaceRequiredStatic: Int, solveWorkspaceRequiredPerRHS: Int)](sparseopaquefactorization_complex_float/init(status:attributes:symbolicfactorization:userfactorstorage:numericfactorization:solveworkspacerequiredstatic:solveworkspacerequiredperrhs:).md)
### Instance Properties
- [var attributes: SparseAttributesComplex_t](sparseopaquefactorization_complex_float/attributes.md)
  A type representing the attributes of a matrix.
- [var numericFactorization: UnsafeMutableRawPointer?](sparseopaquefactorization_complex_float/numericfactorization.md)
- [var solveWorkspaceRequiredPerRHS: Int](sparseopaquefactorization_complex_float/solveworkspacerequiredperrhs.md)
- [var solveWorkspaceRequiredStatic: Int](sparseopaquefactorization_complex_float/solveworkspacerequiredstatic.md)
- [var status: SparseStatus_t](sparseopaquefactorization_complex_float/status.md)
  Status field for a factorization.
- [var symbolicFactorization: SparseOpaqueSymbolicFactorization](sparseopaquefactorization_complex_float/symbolicfactorization.md)
  A semi-opaque type representing symbolic matrix factorization.
- [var userFactorStorage: Bool](sparseopaquefactorization_complex_float/userfactorstorage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquefactorization_complex_float)*