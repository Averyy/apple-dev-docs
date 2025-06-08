# SparseCreatePreconditioner(_:_:)

**Framework**: Accelerate  
**Kind**: func

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

#### Return Value

The constructed preconditioner object. Resource must be freed through a call to `SparseCleanup()` once the user is finished with the preconditioner.

## Parameters

- `type`: (Input) The type of preconditioner to create.
- `A`: (Input) The matrix to construct a preconditioner for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsecreatepreconditioner(_:_:)-95u9p)*