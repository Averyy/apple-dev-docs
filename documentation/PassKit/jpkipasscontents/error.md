# JPKIPassContents.Error

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum  
**Role**: Enumeration

Defines a set of possible errors.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
enum Error
```

## Topics

### Error cases
- [JPKIPassContents.Error.appNotForeground](./error/appnotforeground.md)
  The calling app isn’t in the foreground.
- [JPKIPassContents.Error.biometricUnavailable](./error/biometricunavailable.md)
  Biometric authorization isn’t available.
- [JPKIPassContents.Error.incorrectUserAuthentication](./error/incorrectuserauthentication.md)
  The provided credential authentication request wasn’t accepted.
- [JPKIPassContents.Error.invalidInput](./error/invalidinput.md)
  The PIN or password doesn’t meet the specified conditions.
- [JPKIPassContents.Error.resourceNotAvailable](./error/resourcenotavailable.md)
  The system resouce is currently unavailable.
### Enumeration Cases
- [JPKIPassContents.Error.biometricAuthenticationFailed(laError:)](./error/biometricauthenticationfailed%28laerror%29.md)
  Biometric authorization failed
- [JPKIPassContents.Error.unknownError](./error/unknownerror.md)
  Unknown error occurred
- [JPKIPassContents.Error.userAuthenticationFailed(remainingRetryAttempts:)](./error/userauthenticationfailed%28remainingretryattempts%29.md)
  Credential authentication request provided was rejected.

## Relationships

### Conforms To
- [Error](../../Swift/error.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/jpkipasscontents/error)*