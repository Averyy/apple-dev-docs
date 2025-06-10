# SparseFactorizationFailed

**Framework**: Accelerate  
**Kind**: var

The factorization failed due to a numerical issue.

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
var SparseFactorizationFailed: SparseStatus_t { get }
```

## See Also

- [init(Int32)](sparsestatus_t/init(_:).md)
- [init(rawValue: Int32)](sparsestatus_t/init(rawvalue:).md)
- [var rawValue: Int32](sparsestatus_t/rawvalue.md)
- [var SparseStatusOK: SparseStatus_t](sparsestatusok.md)
  The factorization was successful.
- [var SparseMatrixIsSingular: SparseStatus_t](sparsematrixissingular.md)
  The factorization aborted because the matrix is singular.
- [var SparseInternalError: SparseStatus_t](sparseinternalerror.md)
  The factorization encountered an internal error, such as failing to allocate memory.
- [var SparseParameterError: SparseStatus_t](sparseparametererror.md)
  An error in a user-supplied parameter.
- [var SparseStatusReleased: SparseStatus_t](sparsestatusreleased.md)
  The system freed the factorization object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsefactorizationfailed)*