# passcodeNotSet

**Framework**: Local Authentication  
**Kind**: property

A passcode isn’t set on the device.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
static var passcodeNotSet: LAError.Code { get }
```

## See Also

- [static var appCancel: LAError.Code](laerror-swift.struct/appcancel.md)
  The app canceled authentication.
- [static var systemCancel: LAError.Code](laerror-swift.struct/systemcancel.md)
  The system canceled authentication.
- [static var userCancel: LAError.Code](laerror-swift.struct/usercancel.md)
  The user tapped the cancel button in the authentication dialog.
- [static var biometryDisconnected: LAError.Code](laerror-swift.struct/biometrydisconnected.md)
  The device supports biometry only using a removable accessory, but the paired accessory isn’t connected.
- [static var biometryLockout: LAError.Code](laerror-swift.struct/biometrylockout.md)
  Biometry is locked because there were too many failed attempts.
- [static var biometryNotAvailable: LAError.Code](laerror-swift.struct/biometrynotavailable.md)
  Biometry is not available on the device.
- [static var biometryNotEnrolled: LAError.Code](laerror-swift.struct/biometrynotenrolled.md)
  The user has no enrolled biometric identities.
- [static var biometryNotPaired: LAError.Code](laerror-swift.struct/biometrynotpaired.md)
  The device supports biometry only using a removable accessory, but no accessory is paired.
- [static var touchIDLockout: LAError.Code](laerror-swift.struct/touchidlockout.md)
  Touch ID is locked because there were too many failed attempts.
- [static var touchIDNotAvailable: LAError.Code](laerror-swift.struct/touchidnotavailable.md)
  Touch ID is not available on the device.
- [static var touchIDNotEnrolled: LAError.Code](laerror-swift.struct/touchidnotenrolled.md)
  The user has no enrolled Touch ID fingers.
- [static var authenticationFailed: LAError.Code](laerror-swift.struct/authenticationfailed.md)
  The user failed to provide valid credentials.
- [static var invalidContext: LAError.Code](laerror-swift.struct/invalidcontext.md)
  The context was previously invalidated.
- [static var invalidDimensions: LAError.Code](laerror-swift.struct/invaliddimensions.md)
- [static var notInteractive: LAError.Code](laerror-swift.struct/notinteractive.md)
  Displaying the required authentication user interface is forbidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laerror-swift.struct/passcodenotset)*