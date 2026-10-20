# IdentityDocumentPresentmentError.Code

**Framework**: IdentityDocumentServices  
**Kind**: enum  
**Role**: Enumeration

Specific error codes for identity document web presentment errors.

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
  Pattern matching operator for matching error codes directly. This enables traditional switch/case pattern matching on error codes.
### Enumeration Cases
- [IdentityDocumentPresentmentError.Code.cancelled](./code-swift.enum/cancelled.md)
  An error that indicates that the current request has been cancelled.
- [IdentityDocumentPresentmentError.Code.invalidRequest](./code-swift.enum/invalidrequest.md)
  An error that is thrown when an invalid request is provided.
- [IdentityDocumentPresentmentError.Code.notEntitled](./code-swift.enum/notentitled.md)
  An error that indicates the caller is not entitled.
- [IdentityDocumentPresentmentError.Code.requestInProgress](./code-swift.enum/requestinprogress.md)
  An error that indicates that there is currently a request in progress.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentpresentmenterror/code-swift.enum)*