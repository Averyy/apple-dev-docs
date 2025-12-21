# IdentityDocumentPresentmentError.Code

**Framework**: IdentityDocumentServices  
**Kind**: enum

Specific error codes for identity document web presentment errors.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
enum Code
```

## Topics

### Operators
- [static func ~= (IdentityDocumentPresentmentError.Code, any Error) -> Bool](identitydocumentpresentmenterror/code-swift.enum/~=(_:_:).md)
  Pattern matching operator for matching error codes directly. This enables traditional switch/case pattern matching on error codes.
### Enumeration Cases
- [IdentityDocumentPresentmentError.Code.cancelled](identitydocumentpresentmenterror/code-swift.enum/cancelled.md)
  An error that indicates that the current request has been cancelled.
- [IdentityDocumentPresentmentError.Code.invalidRequest](identitydocumentpresentmenterror/code-swift.enum/invalidrequest.md)
  An error that is thrown when an invalid request is provided.
- [IdentityDocumentPresentmentError.Code.notEntitled](identitydocumentpresentmenterror/code-swift.enum/notentitled.md)
  An error that indicates the caller is not entitled.
- [IdentityDocumentPresentmentError.Code.requestInProgress](identitydocumentpresentmenterror/code-swift.enum/requestinprogress.md)
  An error that indicates that there is currently a request in progress.
- [IdentityDocumentPresentmentError.Code.unknown](identitydocumentpresentmenterror/code-swift.enum/unknown.md)
  An error that indicates that the framework encountered an unknown problem.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentpresentmenterror/code-swift.enum)*