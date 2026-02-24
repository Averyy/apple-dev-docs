# SparseOpaquePreconditioner_Complex_Float

**Framework**: Accelerate  
**Kind**: struct

Represents a preconditioner for matrices of complex float values .

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
struct SparseOpaquePreconditioner_Complex_Float
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
- [init(type: SparsePreconditioner_t, mem: UnsafeMutableRawPointer, apply: (UnsafeMutableRawPointer, CBLAS_TRANSPOSE, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float) -> Void)](sparseopaquepreconditioner_complex_float/init(type:mem:apply:).md)
### Instance Properties
- [var apply: (UnsafeMutableRawPointer, CBLAS_TRANSPOSE, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float) -> Void](sparseopaquepreconditioner_complex_float/apply.md)
- [var mem: UnsafeMutableRawPointer](sparseopaquepreconditioner_complex_float/mem.md)
- [var type: SparsePreconditioner_t](sparseopaquepreconditioner_complex_float/type.md)
  Types of preconditioner.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct SparsePreconditioner_t](sparsepreconditioner_t.md)
  Constants that define the preconditioner type.
- [struct SparseOpaquePreconditioner_Complex_Double](sparseopaquepreconditioner_complex_double.md)
  Represents a preconditioner for matrices of complex double values .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquepreconditioner_complex_float)*