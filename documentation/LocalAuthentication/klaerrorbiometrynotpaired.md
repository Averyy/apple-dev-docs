# kLAErrorBiometryNotPaired

**Framework**: Local Authentication  
**Kind**: var

The device supports biometry only using a removable accessory, but no accessory is paired.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var kLAErrorBiometryNotPaired: Int32 { get }
```

## See Also

- [var kLAErrorDomain: String](klaerrordomain.md)
  The error domain used by LocalAuthentication.
- [var kLAErrorAppCancel: Int32](klaerrorappcancel.md)
  The app canceled authentication.
- [var kLAErrorSystemCancel: Int32](klaerrorsystemcancel.md)
  The system canceled authentication.
- [var kLAErrorUserCancel: Int32](klaerrorusercancel.md)
  The user tapped the cancel button in the authentication dialog.
- [var kLAErrorBiometryDisconnected: Int32](klaerrorbiometrydisconnected.md)
  The device supports biometry only using a removable accessory, but the paired accessory isn’t connected.
- [var kLAErrorBiometryLockout: Int32](klaerrorbiometrylockout.md)
  Biometry is locked because there were too many failed attempts.
- [var kLAErrorBiometryNotAvailable: Int32](klaerrorbiometrynotavailable.md)
  Biometry is not available on the device.
- [var kLAErrorBiometryNotEnrolled: Int32](klaerrorbiometrynotenrolled.md)
  The user has no enrolled biometric identities.
- [var kLAErrorTouchIDLockout: Int32](klaerrortouchidlockout.md)
  Touch ID is locked because there were too many failed attempts.
- [var kLAErrorTouchIDNotAvailable: Int32](klaerrortouchidnotavailable.md)
  Touch ID is not available on the device.
- [var kLAErrorTouchIDNotEnrolled: Int32](klaerrortouchidnotenrolled.md)
  The user has no enrolled Touch ID fingers.
- [var kLAErrorAuthenticationFailed: Int32](klaerrorauthenticationfailed.md)
  The user failed to provide valid credentials.
- [var kLAErrorInvalidContext: Int32](klaerrorinvalidcontext.md)
  The context was previously invalidated.
- [var kLAErrorInvalidDimensions: Int32](klaerrorinvaliddimensions.md)
- [var kLAErrorNotInteractive: Int32](klaerrornotinteractive.md)
  Displaying the required authentication user interface is forbidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/klaerrorbiometrynotpaired)*