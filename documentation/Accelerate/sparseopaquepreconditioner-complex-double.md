# SparseOpaquePreconditioner_Complex_Double

**Framework**: Accelerate  
**Kind**: struct

Represents a preconditioner for matrices of complex double values .

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
struct SparseOpaquePreconditioner_Complex_Double
```

#### Overview

## Topics

### Initializers
- [init(type: SparsePreconditioner_t, mem: UnsafeMutableRawPointer, apply: (UnsafeMutableRawPointer, CBLAS_TRANSPOSE, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double) -> Void)](sparseopaquepreconditioner_complex_double/init(type:mem:apply:).md)
### Instance Properties
- [var apply: (UnsafeMutableRawPointer, CBLAS_TRANSPOSE, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double) -> Void](sparseopaquepreconditioner_complex_double/apply.md)
- [var mem: UnsafeMutableRawPointer](sparseopaquepreconditioner_complex_double/mem.md)
- [var type: SparsePreconditioner_t](sparseopaquepreconditioner_complex_double/type.md)
  Types of preconditioner.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquepreconditioner_complex_double)*