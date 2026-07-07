# JPKIPassContents.Error

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum

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
- [JPKIPassContents.Error.appNotForeground](jpkipasscontents/error/appnotforeground.md)
  The calling app isn’t in the foreground.
- [JPKIPassContents.Error.biometricUnavailable](jpkipasscontents/error/biometricunavailable.md)
  Biometric authorization isn’t available.
- [JPKIPassContents.Error.incorrectUserAuthentication](jpkipasscontents/error/incorrectuserauthentication.md)
  The provided credential authentication request wasn’t accepted.
- [JPKIPassContents.Error.invalidInput](jpkipasscontents/error/invalidinput.md)
  The PIN or password doesn’t meet the specified conditions.
- [JPKIPassContents.Error.resourceNotAvailable](jpkipasscontents/error/resourcenotavailable.md)
  The system resouce is currently unavailable.
### Enumeration Cases
- [JPKIPassContents.Error.biometricAuthenticationFailed(laError:)](jpkipasscontents/error/biometricauthenticationfailed(laerror:).md)
  Biometric authorization failed
- [JPKIPassContents.Error.unknownError](jpkipasscontents/error/unknownerror.md)
  Unknown error occurred
- [JPKIPassContents.Error.userAuthenticationFailed(remainingRetryAttempts:)](jpkipasscontents/error/userauthenticationfailed(remainingretryattempts:).md)
  Credential authentication request provided was rejected.

## Relationships

### Conforms To
- [Error](../Swift/Error.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/jpkipasscontents/error)*