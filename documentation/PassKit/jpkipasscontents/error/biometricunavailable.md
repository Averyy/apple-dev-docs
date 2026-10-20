# JPKIPassContents.Error.biometricUnavailable

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case  
**Role**: Case

Biometric authorization isn’t available.

**Availability**:
- iOS 18.0+ - Deprecated in 18.4
- iPadOS 18.0+ - Deprecated in 18.4

> **Deprecated**: Use biometricAuthenticationFailed(laError: LocalAuthentication.LAError) instead

## Declaration

```swift
case biometricUnavailable
```

## See Also

### Error cases
- [JPKIPassContents.Error.appNotForeground](./appnotforeground.md)
  The calling app isn’t in the foreground.
- [JPKIPassContents.Error.incorrectUserAuthentication](./incorrectuserauthentication.md)
  The provided credential authentication request wasn’t accepted.
- [JPKIPassContents.Error.invalidInput](./invalidinput.md)
  The PIN or password doesn’t meet the specified conditions.
- [JPKIPassContents.Error.resourceNotAvailable](./resourcenotavailable.md)
  The system resouce is currently unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/jpkipasscontents/error/biometricunavailable)*