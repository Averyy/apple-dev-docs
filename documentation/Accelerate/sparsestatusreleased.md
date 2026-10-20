# SparseStatusReleased

**Framework**: Accelerate  
**Kind**: var  
**Role**: Global Variable

The system freed the factorization object.

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
var SparseStatusReleased: SparseStatus_t { get }
```

```c
SparseStatusReleased
```

## See Also

### Constants
- [init(Int32)](./sparsestatus_t/init%28_%29.md)
- [init(rawValue: Int32)](./sparsestatus_t/init%28rawvalue%29.md)
- [var rawValue: Int32](./sparsestatus_t/rawvalue.md)
- [var SparseStatusOK: SparseStatus_t](./sparsestatusok.md)
  The factorization was successful.
- [var SparseFactorizationFailed: SparseStatus_t](./sparsefactorizationfailed.md)
  The factorization failed due to a numerical issue.
- [var SparseMatrixIsSingular: SparseStatus_t](./sparsematrixissingular.md)
  The factorization aborted because the matrix is singular.
- [var SparseInternalError: SparseStatus_t](./sparseinternalerror.md)
  The factorization encountered an internal error, such as failing to allocate memory.
- [var SparseParameterError: SparseStatus_t](./sparseparametererror.md)
  An error in a user-supplied parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsestatusreleased)*