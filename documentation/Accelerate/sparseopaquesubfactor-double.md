# SparseOpaqueSubfactor_Double

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
struct SparseOpaqueSubfactor_Double
```

#### Overview

## Topics

### Initializers
- [init()](sparseopaquesubfactor_double/init.md)
- [init(attributes: SparseAttributes_t, contents: SparseSubfactor_t, factor: SparseOpaqueFactorization_Double, workspaceRequiredStatic: Int, workspaceRequiredPerRHS: Int)](sparseopaquesubfactor_double/init(attributes:contents:factor:workspacerequiredstatic:workspacerequiredperrhs:).md)
### Instance Properties
- [var attributes: SparseAttributes_t](sparseopaquesubfactor_double/attributes.md)
  A type representing the attributes of a matrix.
- [var contents: SparseSubfactor_t](sparseopaquesubfactor_double/contents.md)
  Types of sub-factor object.
- [var factor: SparseOpaqueFactorization_Double](sparseopaquesubfactor_double/factor.md)
  A semi-opaque type representing a matrix factorization in double.
- [var workspaceRequiredPerRHS: Int](sparseopaquesubfactor_double/workspacerequiredperrhs.md)
- [var workspaceRequiredStatic: Int](sparseopaquesubfactor_double/workspacerequiredstatic.md)

## See Also

- [struct SparseOpaqueSubfactor_Float](sparseopaquesubfactor_float.md)
  Represents a sub-factor of the factorization (for example,  `L` from `LDL^T`).
- [struct SparseOpaqueSubfactor_Complex_Double](sparseopaquesubfactor_complex_double.md)
  Represents a sub-factor of the factorization (for example,  `L` from `LDL^T`).
- [struct SparseOpaqueSubfactor_Complex_Float](sparseopaquesubfactor_complex_float.md)
  Represents a sub-factor of the factorization (for example,  `L` from `LDL^T`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquesubfactor_double)*