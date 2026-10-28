# JPKIPassContents.Error.incorrectUserAuthentication

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case  
**Role**: Case

The provided credential authentication request wasn’t accepted.

**Availability**:
- iOS 18.0+ - Deprecated in 18.4
- iPadOS 18.0+ - Deprecated in 18.4

> **Deprecated**: Use userAuthenticationFailed(remainingRetryAttempts: Int) instead

## Declaration

```swift
case incorrectUserAuthentication
```

## Discussion

For example, this error occurs if the PIN provided is incorrect.

## See Also

### Error cases
- [JPKIPassContents.Error.appNotForeground](./appnotforeground.md)
  The calling app isn’t in the foreground.
- [JPKIPassContents.Error.biometricUnavailable](./biometricunavailable.md)
  Biometric authorization isn’t available.
- [JPKIPassContents.Error.invalidInput](./invalidinput.md)
  The PIN or password doesn’t meet the specified conditions.
- [JPKIPassContents.Error.resourceNotAvailable](./resourcenotavailable.md)
  The system resouce is currently unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/jpkipasscontents/error/incorrectuserauthentication)*