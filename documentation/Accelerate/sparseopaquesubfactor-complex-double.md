# SparseOpaqueSubfactor_Complex_Double

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
struct SparseOpaqueSubfactor_Complex_Double
```

#### Overview

- **`attributes`**: Attributes of subfactor. Notably transpose indicates whether it should be considered as the transpose of its underlying contents (e.g. should it count as L or L^T if `.contents=SparseSubfactorL`).
- **`contents`**: Subfactor this represents, e.g. L or Q.
- **`factor`**: Underlying factorization this subfactor is part of.
- **`workspaceRequiredStatic`**: The size of the workspace, in bytes, required to perform `SparseMultiply` or `SparseSolve` with this subfactor is given by the expression: `workspaceRequiredStatic + nrhs*workspaceRequiredPerRhs` where `nrhs` is the number of right-hand side vectors.
- **`workspaceRequiredPerRHS`**: The size of the workspace, in bytes, required to perform SparseMultiply() or SparseSolve() with this subfactor is given by the expression: workspaceRequiredStatic + nrhs*workspaceRequiredPerRhs where nrhs is the number of right-hand side vectors.

## Topics

### Initializers
- [init()](sparseopaquesubfactor_complex_double/init.md)
- [init(attributes: SparseAttributesComplex_t, contents: SparseSubfactor_t, factor: SparseOpaqueFactorization_Complex_Double, workspaceRequiredStatic: Int, workspaceRequiredPerRHS: Int)](sparseopaquesubfactor_complex_double/init(attributes:contents:factor:workspacerequiredstatic:workspacerequiredperrhs:).md)
### Instance Properties
- [var attributes: SparseAttributesComplex_t](sparseopaquesubfactor_complex_double/attributes.md)
  A type representing the attributes of a matrix.
- [var contents: SparseSubfactor_t](sparseopaquesubfactor_complex_double/contents.md)
  Types of sub-factor object.
- [var factor: SparseOpaqueFactorization_Complex_Double](sparseopaquesubfactor_complex_double/factor.md)
  A semi-opaque type representing a matrix factorization in complex double.
- [var workspaceRequiredPerRHS: Int](sparseopaquesubfactor_complex_double/workspacerequiredperrhs.md)
- [var workspaceRequiredStatic: Int](sparseopaquesubfactor_complex_double/workspacerequiredstatic.md)

## See Also

- [struct SparseOpaqueSubfactor_Double](sparseopaquesubfactor_double.md)
  Represents a sub-factor of the factorization (for example,  `L` from `LDL^T`).
- [struct SparseOpaqueSubfactor_Float](sparseopaquesubfactor_float.md)
  Represents a sub-factor of the factorization (for example,  `L` from `LDL^T`).
- [struct SparseOpaqueSubfactor_Complex_Float](sparseopaquesubfactor_complex_float.md)
  Represents a sub-factor of the factorization (for example,  `L` from `LDL^T`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquesubfactor_complex_double)*