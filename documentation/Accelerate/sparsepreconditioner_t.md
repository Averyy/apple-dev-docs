# SparsePreconditioner_t

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

Constants that define the preconditioner type.

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
struct SparsePreconditioner_t
```

```c
typedef enum { ... } SparsePreconditioner_t;
```

## Topics

### Constants
- [var SparsePreconditionerDiagScaling: SparsePreconditioner_t](./sparsepreconditionerdiagscaling.md)
  A diagonal scaling preconditioner.
- [var SparsePreconditionerDiagonal: SparsePreconditioner_t](./sparsepreconditionerdiagonal.md)
  A Jacobi preconditioner.
- [var SparsePreconditionerNone: SparsePreconditioner_t](./sparsepreconditionernone.md)
  No preconditioner.
- [var SparsePreconditionerUser: SparsePreconditioner_t](./sparsepreconditioneruser.md)
  A user-provided preconditioner.
### Raw Values
- [init(Int32)](./sparsepreconditioner_t/init%28_%29.md)
- [init(rawValue: Int32)](./sparsepreconditioner_t/init%28rawvalue%29.md)
- [var rawValue: Int32](./sparsepreconditioner_t/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Preconditioners
- [struct SparseOpaquePreconditioner_Complex_Double](./sparseopaquepreconditioner_complex_double.md)
  Represents a preconditioner for matrices of complex double values .
- [struct SparseOpaquePreconditioner_Complex_Float](./sparseopaquepreconditioner_complex_float.md)
  Represents a preconditioner for matrices of complex float values .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsepreconditioner_t)*