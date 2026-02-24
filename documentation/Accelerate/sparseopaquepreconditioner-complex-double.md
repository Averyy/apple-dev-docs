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

- **`type`**: The type of preconditioner represented.
- **`mem`**: Block of memory that will be passed unaltered as the first argument of the `apply()` callback.
- **`apply(mem, trans, X, Y)`**: Function to call to apply the preconditioner as `Y = PX` (`trans=false`) or `Y = P^TX` (`trans`=`true`). - `mem` : The unaltered pointer mem from this struct.
- `trans` : Flags whether to apply the preconditioner or its transpose.
- `X`: The right-hand side vectors X.
- `Y`: The result vectors Y.

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

## See Also

- [struct SparsePreconditioner_t](sparsepreconditioner_t.md)
  Constants that define the preconditioner type.
- [struct SparseOpaquePreconditioner_Complex_Float](sparseopaquepreconditioner_complex_float.md)
  Represents a preconditioner for matrices of complex float values .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquepreconditioner_complex_double)*