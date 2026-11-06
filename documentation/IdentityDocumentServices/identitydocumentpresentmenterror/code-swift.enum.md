# IdentityDocumentPresentmentError.Code

**Framework**: IdentityDocumentServices  
**Kind**: enum  
**Role**: Enumeration

Error codes for identity document web presentment errors.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst
- macOS 26.0+

## Declaration

```swift
enum Code
```

## Topics

### Operators
- [static func ~= (IdentityDocumentPresentmentError.Code, any Error) -> Bool](./code-swift.enum/tildeeq%28_,_%29.md)
  A pattern-matching operator for matching error codes directly. This operator enables traditional switch/case pattern matching on error codes.
### Enumeration Cases
- [IdentityDocumentPresentmentError.Code.cancelled](./code-swift.enum/cancelled.md)
  An error that indicates that the current request was canceled.
- [IdentityDocumentPresentmentError.Code.invalidRequest](./code-swift.enum/invalidrequest.md)
  An error that indicates an invalid request.
- [IdentityDocumentPresentmentError.Code.notEntitled](./code-swift.enum/notentitled.md)
  An error that indicates the caller isn’t entitled.
- [IdentityDocumentPresentmentError.Code.requestInProgress](./code-swift.enum/requestinprogress.md)
  An error that indicates a request is in progress.
- [IdentityDocumentPresentmentError.Code.unknown](./code-swift.enum/unknown.md)
  An error that indicates that the framework encountered an unknown problem.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Matching error codes
- [static let cancelled: IdentityDocumentPresentmentError.Code](./cancelled.md)
  An error that indicates the current request was canceled.
- [static let invalidRequest: IdentityDocumentPresentmentError.Code](./invalidrequest.md)
  An error thrown when a request is invalid.
- [static let notEntitled: IdentityDocumentPresentmentError.Code](./notentitled.md)
  An error that indicates the caller is not entitled.
- [static let requestInProgress: IdentityDocumentPresentmentError.Code](./requestinprogress.md)
  An error that indicates a request in progress.
- [static let unknown: IdentityDocumentPresentmentError.Code](./unknown.md)
  An error that indicates the framework encountered an unknown problem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentpresentmenterror/code-swift.enum)*