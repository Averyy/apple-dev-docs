# IdentityDocumentPresentmentError

**Framework**: IdentityDocumentServices  
**Kind**: struct

An error type that is thrown from the identity document web presentment controller.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
struct IdentityDocumentPresentmentError
```

## Topics

### Instance Properties
- [let code: IdentityDocumentPresentmentError.Code](identitydocumentpresentmenterror/code-swift.property.md)
  The code of the current error.
- [let debugDescription: String](identitydocumentpresentmenterror/debugdescription.md)
  A debug description that provides additional context about the current error.
### Type Properties
- [static let cancelled: IdentityDocumentPresentmentError.Code](identitydocumentpresentmenterror/cancelled.md)
  An error that indicates that the current request has been cancelled.
- [static let invalidRequest: IdentityDocumentPresentmentError.Code](identitydocumentpresentmenterror/invalidrequest.md)
  An error that is thrown when an invalid request is provided.
- [static let notEntitled: IdentityDocumentPresentmentError.Code](identitydocumentpresentmenterror/notentitled.md)
  An error that indicates the caller is not entitled.
- [static let requestInProgress: IdentityDocumentPresentmentError.Code](identitydocumentpresentmenterror/requestinprogress.md)
  An error that indicates that there is currently a request in progress.
- [static let unknown: IdentityDocumentPresentmentError.Code](identitydocumentpresentmenterror/unknown.md)
  An error that indicates that the framework encountered an unknown problem.
### Enumerations
- [IdentityDocumentPresentmentError.Code](identitydocumentpresentmenterror/code-swift.enum.md)
  Specific error codes for identity document web presentment errors.

## Relationships

### Conforms To
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentpresentmenterror)*