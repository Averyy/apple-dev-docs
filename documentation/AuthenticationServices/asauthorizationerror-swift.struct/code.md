# ASAuthorizationError.Code

**Framework**: Authentication Services  
**Kind**: enum  
**Role**: Enumeration

Codes that authorization errors can have.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum Code
```

```c
enum ASAuthorizationError : NSInteger;
```

## Topics

### Codes
- [ASAuthorizationError.Code.canceled](./code/canceled.md)
  The user canceled the authorization attempt.
- [ASAuthorizationError.Code.failed](./code/failed.md)
  The authorization attempt failed.
- [ASAuthorizationError.Code.invalidResponse](./code/invalidresponse.md)
  The authorization request received an invalid response.
- [ASAuthorizationError.Code.notHandled](./code/nothandled.md)
  The authorization request wasn’t handled.
- [ASAuthorizationError.Code.unknown](./code/unknown.md)
  The authorization attempt failed for an unknown reason.
- [ASAuthorizationError.Code.notInteractive](./code/notinteractive.md)
  The authorization request isn’t interactive.
- [ASAuthorizationError.Code.credentialExport](./code/credentialexport.md)
  The credential export request failed.
- [ASAuthorizationError.Code.credentialImport](./code/credentialimport.md)
  The credential import request failed.
### Enumeration Cases
- [ASAuthorizationError.Code.deviceNotConfiguredForPasskeyCreation](./code/devicenotconfiguredforpasskeycreation.md)
  This error signals that the device is not currently set up to create passkeys.
- [ASAuthorizationError.Code.matchedExcludedCredential](./code/matchedexcludedcredential.md)
  This error should only be returned when specifying @c excludedCredentials on a public key credential registration request.
- [ASAuthorizationError.Code.preferSignInWithApple](./code/prefersigninwithapple.md)
  This error signals the user has an existing Sign in with Apple account that they would prefer to use instead of continuing the current request.
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

### Error Codes
- [static var canceled: ASAuthorizationError.Code](./canceled.md)
  The user canceled the authorization attempt.
- [static var failed: ASAuthorizationError.Code](./failed.md)
  The authorization attempt failed.
- [static var invalidResponse: ASAuthorizationError.Code](./invalidresponse.md)
  The authorization request received an invalid response.
- [static var notHandled: ASAuthorizationError.Code](./nothandled.md)
  The authorization request wasn’t handled.
- [static var unknown: ASAuthorizationError.Code](./unknown.md)
  The authorization attempt failed for an unknown reason.
- [static var credentialExport: ASAuthorizationError.Code](./credentialexport.md)
  The credential export request failed.
- [static var credentialImport: ASAuthorizationError.Code](./credentialimport.md)
  The credential import request failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationerror-swift.struct/code)*