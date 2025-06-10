# ASExtensionError

**Framework**: Authentication Services  
**Kind**: struct

A credential provider extension error.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct ASExtensionError
```

## Topics

### Identifying the error domain
- [let ASExtensionErrorDomain: String](asextensionerrordomain.md)
  The domain for a credential provider extension error.
### Error codes
- [static var credentialIdentityNotFound: ASExtensionError.Code](asextensionerror/credentialidentitynotfound.md)
  The credential identity was not found.
- [static var failed: ASExtensionError.Code](asextensionerror/failed.md)
  The operation failed.
- [static var userCanceled: ASExtensionError.Code](asextensionerror/usercanceled.md)
  The user canceled the operation.
- [static var userInteractionRequired: ASExtensionError.Code](asextensionerror/userinteractionrequired.md)
  User interaction is required.
- [ASExtensionError.Code](asextensionerror/code.md)
  The codes for a credential provider extension error.
### Type Properties
- [static var errorDomain: String](asextensionerror/errordomain.md)
- [static var matchedExcludedCredential: ASExtensionError.Code](asextensionerror/matchedexcludedcredential.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let ASExtensionErrorDomain: String](asextensionerrordomain.md)
  The domain for a credential provider extension error.
- [ASExtensionError.Code](asextensionerror/code.md)
  The codes for a credential provider extension error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asextensionerror)*