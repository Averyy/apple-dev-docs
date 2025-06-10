# IdentityDocumentWebPresentmentError

**Framework**: IdentityDocumentServices  
**Kind**: enum

An error type thrown from the identity document web presentment controller.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
enum IdentityDocumentWebPresentmentError
```

## Topics

### Types of errors
- [IdentityDocumentWebPresentmentError.cancelled](identitydocumentwebpresentmenterror/cancelled.md)
  An error that indicates the current request was canceled.
- [IdentityDocumentWebPresentmentError.invalidRequest](identitydocumentwebpresentmenterror/invalidrequest.md)
  An error that indicates the framework received an invalid request.
- [IdentityDocumentWebPresentmentError.notEntitled](identitydocumentwebpresentmenterror/notentitled.md)
  An error that indicates the caller isn’t entitled.
- [IdentityDocumentWebPresentmentError.requestInProgress](identitydocumentwebpresentmenterror/requestinprogress.md)
  An error that indicates an in-progress request.
- [IdentityDocumentWebPresentmentError.unknown](identitydocumentwebpresentmenterror/unknown.md)
  An error that indicates the framework encountered an unknown problem.
### Hash values
- [func hash(into: inout Hasher)](identitydocumentwebpresentmenterror/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](identitydocumentwebpresentmenterror/hashvalue.md)
  The hash value.
- [static func == (IdentityDocumentWebPresentmentError, IdentityDocumentWebPresentmentError) -> Bool](identitydocumentwebpresentmenterror/==(_:_:).md)
  Returns a Boolean value that indicates whether two values are equal.
### Default Implementations
- [Equatable Implementations](identitydocumentwebpresentmenterror/equatable-implementations.md)
- [Error Implementations](identitydocumentwebpresentmenterror/error-implementations.md)
- [LocalizedError Implementations](identitydocumentwebpresentmenterror/localizederror-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentwebpresentmenterror)*