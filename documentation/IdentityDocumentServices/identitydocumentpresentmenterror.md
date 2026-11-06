# IdentityDocumentPresentmentError

**Framework**: IdentityDocumentServices  
**Kind**: struct  
**Role**: Structure

An error type the identity document web presentment controller throws.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst
- macOS 26.0+

## Declaration

```swift
struct IdentityDocumentPresentmentError
```

## Topics

### Inspecting an error
- [let code: IdentityDocumentPresentmentError.Code](./identitydocumentpresentmenterror/code-swift.property.md)
  The code of the current error.
- [let debugDescription: String](./identitydocumentpresentmenterror/debugdescription.md)
  A debug description that provides additional context about the current error.
### Matching error codes
- [IdentityDocumentPresentmentError.Code](./identitydocumentpresentmenterror/code-swift.enum.md)
  Error codes for identity document web presentment errors.
- [static let cancelled: IdentityDocumentPresentmentError.Code](./identitydocumentpresentmenterror/cancelled.md)
  An error that indicates the current request was canceled.
- [static let invalidRequest: IdentityDocumentPresentmentError.Code](./identitydocumentpresentmenterror/invalidrequest.md)
  An error thrown when a request is invalid.
- [static let notEntitled: IdentityDocumentPresentmentError.Code](./identitydocumentpresentmenterror/notentitled.md)
  An error that indicates the caller is not entitled.
- [static let requestInProgress: IdentityDocumentPresentmentError.Code](./identitydocumentpresentmenterror/requestinprogress.md)
  An error that indicates a request in progress.
- [static let unknown: IdentityDocumentPresentmentError.Code](./identitydocumentpresentmenterror/unknown.md)
  An error that indicates the framework encountered an unknown problem.

## Relationships

### Conforms To
- [Error](../Swift/error.md)
- [LocalizedError](../Foundation/localizederror.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentpresentmenterror)*