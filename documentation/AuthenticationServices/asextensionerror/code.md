# ASExtensionError.Code

**Framework**: Authentication Services  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum ASExtensionErrorCode : NSInteger;
```

## Topics

### Codes
- [ASExtensionError.Code.credentialIdentityNotFound](./code/credentialidentitynotfound.md)
  The credential identity was not found.
- [ASExtensionError.Code.failed](./code/failed.md)
  The operation failed.
- [ASExtensionError.Code.userCanceled](./code/usercanceled.md)
  The user canceled the operation.
- [ASExtensionError.Code.userInteractionRequired](./code/userinteractionrequired.md)
  User interaction is required.
### Enumeration Cases
- [ASExtensionError.Code.matchedExcludedCredential](./code/matchedexcludedcredential.md)
  This error should only be used for a passkey registration request, if the @c excludedCredentials property matches a known passkey.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Recognizing errors
- [struct ASExtensionError](../asextensionerror.md)
  A credential provider extension error.
- [let ASExtensionErrorDomain: String](../asextensionerrordomain.md)
  The domain for a credential provider extension error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asextensionerror/code)*