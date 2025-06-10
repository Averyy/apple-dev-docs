# SparseCreatePreconditioner(_:_:)

**Framework**: Accelerate  
**Kind**: func

Creates a preconditioner for the specified matrix of double-precision values.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func SparseCreatePreconditioner(_ type: SparsePreconditioner_t, _ A: SparseMatrix_Double) -> SparseOpaquePreconditioner_Double
```

#### Return Value

A [`SparseOpaquePreconditioner_Double`](sparseopaquepreconditioner_double.md) structure. You must free the resource through a call to [`SparseCleanup(_:)`](sparsecleanup(_:)-45lq7.md) after you finish with the object.

## Parameters

- `type`: The type of preconditioner to create.
- `A`: The matrix to construct a preconditioner for.

## See Also

- [func SparseCreatePreconditioner(SparsePreconditioner_t, SparseMatrix_Float) -> SparseOpaquePreconditioner_Float](sparsecreatepreconditioner(_:_:)-59ql5.md)
  Creates a preconditioner for the specified matrix of single-precision values.
- [struct SparseOpaquePreconditioner_Double](sparseopaquepreconditioner_double.md)
  A structure that represents a double-precision preconditioner.
- [struct SparseOpaquePreconditioner_Float](sparseopaquepreconditioner_float.md)
  A structure that represents a single-precision preconditioner.
- [func SparseCreatePreconditioner(SparsePreconditioner_t, SparseMatrix_Complex_Double) -> SparseOpaquePreconditioner_Complex_Double](sparsecreatepreconditioner(_:_:)-1yp4n.md)
  Create a preconditioner for the given matrix of complex double values.
- [func SparseCreatePreconditioner(SparsePreconditioner_t, SparseMatrix_Complex_Float) -> SparseOpaquePreconditioner_Complex_Float](sparsecreatepreconditioner(_:_:)-95u9p.md)
  Create a preconditioner for the given matrix of complex float values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsecreatepreconditioner(_:_:)-4ysww)*