# ASExtensionError.Code

**Framework**: Authentication Services  
**Kind**: enum

The codes for a credential provider extension error.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

## Topics

### Codes
- [ASExtensionError.Code.credentialIdentityNotFound](asextensionerror/code/credentialidentitynotfound.md)
  The credential identity was not found.
- [ASExtensionError.Code.failed](asextensionerror/code/failed.md)
  The operation failed.
- [ASExtensionError.Code.userCanceled](asextensionerror/code/usercanceled.md)
  The user canceled the operation.
- [ASExtensionError.Code.userInteractionRequired](asextensionerror/code/userinteractionrequired.md)
  User interaction is required.
### Enumeration Cases
- [ASExtensionError.Code.matchedExcludedCredential](asextensionerror/code/matchedexcludedcredential.md)
  This error should only be used for a passkey registration request, if the @c excludedCredentials property matches a known passkey.
### Initializers
- [init?(rawValue: Int)](asextensionerror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ASExtensionError](asextensionerror.md)
  A credential provider extension error.
- [let ASExtensionErrorDomain: String](asextensionerrordomain.md)
  The domain for a credential provider extension error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asextensionerror/code)*