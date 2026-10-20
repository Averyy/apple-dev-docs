# init(_:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

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
init(_ rawValue: Int32)
```

## See Also

### Constants
- [init(rawValue: Int32)](./init%28rawvalue%29.md)
- [var rawValue: Int32](./rawvalue.md)
- [var SparseStatusOK: SparseStatus_t](../sparsestatusok.md)
  The factorization was successful.
- [var SparseFactorizationFailed: SparseStatus_t](../sparsefactorizationfailed.md)
  The factorization failed due to a numerical issue.
- [var SparseMatrixIsSingular: SparseStatus_t](../sparsematrixissingular.md)
  The factorization aborted because the matrix is singular.
- [var SparseInternalError: SparseStatus_t](../sparseinternalerror.md)
  The factorization encountered an internal error, such as failing to allocate memory.
- [var SparseParameterError: SparseStatus_t](../sparseparametererror.md)
  An error in a user-supplied parameter.
- [var SparseStatusReleased: SparseStatus_t](../sparsestatusreleased.md)
  The system freed the factorization object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsestatus_t/init(_:))*