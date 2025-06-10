# SparseStatus_t

**Framework**: Accelerate  
**Kind**: struct

Constants that describe the status of a factorization.

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
struct SparseStatus_t
```

## Topics

### Constants
- [init(Int32)](sparsestatus_t/init(_:).md)
- [init(rawValue: Int32)](sparsestatus_t/init(rawvalue:).md)
- [var rawValue: Int32](sparsestatus_t/rawvalue.md)
- [var SparseStatusOK: SparseStatus_t](sparsestatusok.md)
  The factorization was successful.
- [var SparseFactorizationFailed: SparseStatus_t](sparsefactorizationfailed.md)
  The factorization failed due to a numerical issue.
- [var SparseMatrixIsSingular: SparseStatus_t](sparsematrixissingular.md)
  The factorization aborted because the matrix is singular.
- [var SparseInternalError: SparseStatus_t](sparseinternalerror.md)
  The factorization encountered an internal error, such as failing to allocate memory.
- [var SparseParameterError: SparseStatus_t](sparseparametererror.md)
  An error in a user-supplied parameter.
- [var SparseStatusReleased: SparseStatus_t](sparsestatusreleased.md)
  The system freed the factorization object.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var status: SparseStatus_t](sparseopaquesymbolicfactorization/status.md)
  The status of the factorization.
- [var type: SparseFactorization_t](sparseopaquesymbolicfactorization/type.md)
  The factorization type.
- [var factorization: UnsafeMutableRawPointer?](sparseopaquesymbolicfactorization/factorization.md)
  A pointer to a private internal representation of the symbolic factor.
- [struct SparseFactorization_t](sparsefactorization_t.md)
  Constants that define the factorization type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsestatus_t)*