# appCancel

**Framework**: Local Authentication  
**Kind**: property  
**Role**: Type Property

The app canceled authentication.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var appCancel: LAError.Code { get }
```

#### Discussion

You receive this error if you call the [`invalidate()`](../lacontext/invalidate%28%29.md) method while authentication is in process.

## See Also

### Error Codes
- [static var systemCancel: LAError.Code](./systemcancel.md)
  The system canceled authentication.
- [static var userCancel: LAError.Code](./usercancel.md)
  The user tapped the cancel button in the authentication dialog.
- [static var biometryDisconnected: LAError.Code](./biometrydisconnected.md)
  The device supports biometry only using a removable accessory, but the paired accessory isn’t connected.
- [static var biometryLockout: LAError.Code](./biometrylockout.md)
  Biometry is locked because there were too many failed attempts.
- [static var biometryNotAvailable: LAError.Code](./biometrynotavailable.md)
  Biometry is not available on the device.
- [static var biometryNotEnrolled: LAError.Code](./biometrynotenrolled.md)
  The user has no enrolled biometric identities.
- [static var biometryNotPaired: LAError.Code](./biometrynotpaired.md)
  The device supports biometry only using a removable accessory, but no accessory is paired.
- [static var touchIDLockout: LAError.Code](./touchidlockout.md)
  Touch ID is locked because there were too many failed attempts.
- [static var touchIDNotAvailable: LAError.Code](./touchidnotavailable.md)
  Touch ID is not available on the device.
- [static var touchIDNotEnrolled: LAError.Code](./touchidnotenrolled.md)
  The user has no enrolled Touch ID fingers.
- [static var authenticationFailed: LAError.Code](./authenticationfailed.md)
  The user failed to provide valid credentials.
- [static var invalidContext: LAError.Code](./invalidcontext.md)
  The context was previously invalidated.
- [static var invalidDimensions: LAError.Code](./invaliddimensions.md)
- [static var notInteractive: LAError.Code](./notinteractive.md)
  Displaying the required authentication user interface is forbidden.
- [static var passcodeNotSet: LAError.Code](./passcodenotset.md)
  A passcode isn’t set on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laerror-swift.struct/appcancel)*