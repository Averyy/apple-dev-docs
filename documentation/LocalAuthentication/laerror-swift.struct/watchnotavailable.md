# watchNotAvailable

**Framework**: Local Authentication  
**Kind**: property  
**Role**: Type Property

An attempt to authenticate with Apple Watch failed.

**Availability**:
- macOS 10.15+ - Deprecated in 15.0 (renamed: LAError.companionNotAvailable)

## Declaration

```swift
static var watchNotAvailable: LAError.Code { get }
```

## Discussion

You receive this error when the system fails to locate a nearby, paired Apple Watch running watchOS 6 or later while trying to authenticate using one of the watch authentication policies like [`deviceOwnerAuthenticationWithWatch`](../lapolicy/deviceownerauthenticationwithwatch.md).

## See Also

### Error Codes
- [static var appCancel: LAError.Code](./appcancel.md)
  The app canceled authentication.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laerror-swift.struct/watchnotavailable)*