# SparseCreatePreconditioner(_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Creates a preconditioner for the specified matrix of single-precision values.

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
func SparseCreatePreconditioner(_ type: SparsePreconditioner_t, _ A: SparseMatrix_Float) -> SparseOpaquePreconditioner_Float
```

```c
static SparseOpaquePreconditioner_Float SparseCreatePreconditioner(SparsePreconditioner_t type, SparseMatrix_Float A);
```

## Return Value

A [`SparseOpaquePreconditioner_Float`](./sparseopaquepreconditioner_float.md) structure.  You must free the resource through a call to [`SparseCleanup(_:)`](./sparsecleanup%28_%29-45lq7.md) after you finish with the object.

## Parameters

- `type`: The type of preconditioner to create.
- `A`: The matrix to construct a preconditioner for.

## See Also

### Creating preconditioners
- [func SparseCreatePreconditioner(SparsePreconditioner_t, SparseMatrix_Double) -> SparseOpaquePreconditioner_Double](./sparsecreatepreconditioner%28_,_%29-4ysww.md)
  Creates a preconditioner for the specified matrix of double-precision values.
- [struct SparseOpaquePreconditioner_Double](./sparseopaquepreconditioner_double.md)
  A structure that represents a double-precision preconditioner.
- [struct SparseOpaquePreconditioner_Float](./sparseopaquepreconditioner_float.md)
  A structure that represents a single-precision preconditioner.
- [func SparseCreatePreconditioner(SparsePreconditioner_t, SparseMatrix_Complex_Double) -> SparseOpaquePreconditioner_Complex_Double](./sparsecreatepreconditioner%28_,_%29-1yp4n.md)
  Create a preconditioner for the given matrix of complex double values.
- [func SparseCreatePreconditioner(SparsePreconditioner_t, SparseMatrix_Complex_Float) -> SparseOpaquePreconditioner_Complex_Float](./sparsecreatepreconditioner%28_,_%29-95u9p.md)
  Create a preconditioner for the given matrix of complex float values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsecreatepreconditioner(_:_:)-59ql5)*