# SparseOpaqueSubfactor_Complex_Float

**Framework**: Accelerate  
**Kind**: struct

Represents a sub-factor of the factorization (for example,  `L` from `LDL^T`).

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
struct SparseOpaqueSubfactor_Complex_Float
```

#### Overview

## Topics

### Initializers
- [init()](sparseopaquesubfactor_complex_float/init.md)
- [init(attributes: SparseAttributesComplex_t, contents: SparseSubfactor_t, factor: SparseOpaqueFactorization_Complex_Float, workspaceRequiredStatic: Int, workspaceRequiredPerRHS: Int)](sparseopaquesubfactor_complex_float/init(attributes:contents:factor:workspacerequiredstatic:workspacerequiredperrhs:).md)
### Instance Properties
- [var attributes: SparseAttributesComplex_t](sparseopaquesubfactor_complex_float/attributes.md)
  A type representing the attributes of a matrix.
- [var contents: SparseSubfactor_t](sparseopaquesubfactor_complex_float/contents.md)
  Types of sub-factor object.
- [var factor: SparseOpaqueFactorization_Complex_Float](sparseopaquesubfactor_complex_float/factor.md)
  A semi-opaque type representing a matrix factorization in complex float.
- [var workspaceRequiredPerRHS: Int](sparseopaquesubfactor_complex_float/workspacerequiredperrhs.md)
- [var workspaceRequiredStatic: Int](sparseopaquesubfactor_complex_float/workspacerequiredstatic.md)

## See Also

- [struct SparseOpaqueSubfactor_Double](sparseopaquesubfactor_double.md)
  Represents a sub-factor of the factorization (for example,  `L` from `LDL^T`).
- [struct SparseOpaqueSubfactor_Float](sparseopaquesubfactor_float.md)
  Represents a sub-factor of the factorization (for example,  `L` from `LDL^T`).
- [struct SparseOpaqueSubfactor_Complex_Double](sparseopaquesubfactor_complex_double.md)
  Represents a sub-factor of the factorization (for example,  `L` from `LDL^T`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquesubfactor_complex_float)*