# SparseCreatePreconditioner(_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Create a preconditioner for the given matrix of complex float values.

**Availability**:
- iOS 18.5+
- iPadOS 18.5+
- Mac Catalyst 18.5+
- macOS 15.5+
- tvOS 18.5+
- visionOS 2.5+
- watchOS 11.5+

## Declaration

```swift
func SparseCreatePreconditioner(_ type: SparsePreconditioner_t, _ A: SparseMatrix_Complex_Float) -> SparseOpaquePreconditioner_Complex_Float
```

```c
static SparseOpaquePreconditioner_Complex_Float SparseCreatePreconditioner(SparsePreconditioner_t type, SparseMatrix_Complex_Float A);
```

## Return Value

The constructed preconditioner object. Resource must be freed through a call to `SparseCleanup()` once the user is finished with the preconditioner.

## Parameters

- `type`: (Input) The type of preconditioner to create.
- `A`: (Input) The matrix to construct a preconditioner for.

## See Also

### Creating preconditioners
- [func SparseCreatePreconditioner(SparsePreconditioner_t, SparseMatrix_Double) -> SparseOpaquePreconditioner_Double](./sparsecreatepreconditioner%28_,_%29-4ysww.md)
  Creates a preconditioner for the specified matrix of double-precision values.
- [func SparseCreatePreconditioner(SparsePreconditioner_t, SparseMatrix_Float) -> SparseOpaquePreconditioner_Float](./sparsecreatepreconditioner%28_,_%29-59ql5.md)
  Creates a preconditioner for the specified matrix of single-precision values.
- [struct SparseOpaquePreconditioner_Double](./sparseopaquepreconditioner_double.md)
  A structure that represents a double-precision preconditioner.
- [struct SparseOpaquePreconditioner_Float](./sparseopaquepreconditioner_float.md)
  A structure that represents a single-precision preconditioner.
- [func SparseCreatePreconditioner(SparsePreconditioner_t, SparseMatrix_Complex_Double) -> SparseOpaquePreconditioner_Complex_Double](./sparsecreatepreconditioner%28_,_%29-1yp4n.md)
  Create a preconditioner for the given matrix of complex double values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsecreatepreconditioner(_:_:)-95u9p)*