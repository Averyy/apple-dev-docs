# JPKIPassContents.Error.invalidInput

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case

The PIN or password doesn’t meet the specified conditions.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
case invalidInput
```

#### Discussion

This error occurs when there’s an attempt to update the PIN or password for a digitial identity and the provided information doesn’t meet the defined requirements.

## See Also

- [JPKIPassContents.Error.appNotForeground](jpkipasscontents/error/appnotforeground.md)
  The calling app isn’t in the foreground.
- [JPKIPassContents.Error.biometricUnavailable](jpkipasscontents/error/biometricunavailable.md)
  Biometric authorization isn’t available.
- [JPKIPassContents.Error.incorrectUserAuthentication](jpkipasscontents/error/incorrectuserauthentication.md)
  The provided credential authentication request wasn’t accepted.
- [JPKIPassContents.Error.resourceNotAvailable](jpkipasscontents/error/resourcenotavailable.md)
  The system resouce is currently unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/jpkipasscontents/error/invalidinput)*