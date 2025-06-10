# SparseOpaquePreconditioner_Double

**Framework**: Accelerate  
**Kind**: struct

A structure that represents a double-precision preconditioner.

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
struct SparseOpaquePreconditioner_Double
```

## Topics

### Creating a Preconditioner
- [init(type: SparsePreconditioner_t, mem: UnsafeMutableRawPointer, apply: (UnsafeMutableRawPointer, CBLAS_TRANSPOSE, DenseMatrix_Double, DenseMatrix_Double) -> Void)](sparseopaquepreconditioner_double/init(type:mem:apply:).md)
  Creates a new double-precision preconditioner.
### Inspecting Preconditioner Properties
- [var apply: (UnsafeMutableRawPointer, CBLAS_TRANSPOSE, DenseMatrix_Double, DenseMatrix_Double) -> Void](sparseopaquepreconditioner_double/apply.md)
  A function that calculates , where  is the preconditioner.
- [var mem: UnsafeMutableRawPointer](sparseopaquepreconditioner_double/mem.md)
  The unaltered memory pointer that passes as the first parameter of the apply function.
- [var type: SparsePreconditioner_t](sparseopaquepreconditioner_double/type.md)
  The preconditioner type.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [func SparseCreatePreconditioner(SparsePreconditioner_t, SparseMatrix_Double) -> SparseOpaquePreconditioner_Double](sparsecreatepreconditioner(_:_:)-4ysww.md)
  Creates a preconditioner for the specified matrix of double-precision values.
- [func SparseCreatePreconditioner(SparsePreconditioner_t, SparseMatrix_Float) -> SparseOpaquePreconditioner_Float](sparsecreatepreconditioner(_:_:)-59ql5.md)
  Creates a preconditioner for the specified matrix of single-precision values.
- [struct SparseOpaquePreconditioner_Float](sparseopaquepreconditioner_float.md)
  A structure that represents a single-precision preconditioner.
- [func SparseCreatePreconditioner(SparsePreconditioner_t, SparseMatrix_Complex_Double) -> SparseOpaquePreconditioner_Complex_Double](sparsecreatepreconditioner(_:_:)-1yp4n.md)
  Create a preconditioner for the given matrix of complex double values.
- [func SparseCreatePreconditioner(SparsePreconditioner_t, SparseMatrix_Complex_Float) -> SparseOpaquePreconditioner_Complex_Float](sparsecreatepreconditioner(_:_:)-95u9p.md)
  Create a preconditioner for the given matrix of complex float values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquepreconditioner_double)*