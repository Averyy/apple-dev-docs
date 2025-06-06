# JPKIPassContents.Error.incorrectUserAuthentication

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case

The provided credential authentication request wasn’t accepted.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
case incorrectUserAuthentication
```

#### Discussion

For example, this error occurs if the PIN provided is incorrect.

## See Also

- [JPKIPassContents.Error.appNotForeground](jpkipasscontents/error/appnotforeground.md)
  The calling app isn’t in the foreground.
- [JPKIPassContents.Error.biometricUnavailable](jpkipasscontents/error/biometricunavailable.md)
  Biometric authorization isn’t available.
- [JPKIPassContents.Error.invalidInput](jpkipasscontents/error/invalidinput.md)
  The PIN or password doesn’t meet the specified conditions.
- [JPKIPassContents.Error.resourceNotAvailable](jpkipasscontents/error/resourcenotavailable.md)
  The system resouce is currently unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/jpkipasscontents/error/incorrectuserauthentication)*