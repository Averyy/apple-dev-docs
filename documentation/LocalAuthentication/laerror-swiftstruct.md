# LAError

**Framework**: Local Authentication  
**Kind**: struct

Errors issued by the LocalAuthentication framework.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct LAError
```

## Topics

### Error Characteristics
- [let LAErrorDomain: String](laerrordomain.md)
  The error domain that the framework uses when issuing errors.
### Error Codes
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
- [static var passcodeNotSet: LAError.Code](laerror-swift.struct/passcodenotset.md)
  A passcode isn’t set on the device.
- [static var userFallback: LAError.Code](laerror-swift.struct/userfallback.md)
  The user tapped the fallback button in the authentication dialog, but no fallback is available for the authentication policy.
- [static var watchNotAvailable: LAError.Code](laerror-swift.struct/watchnotavailable.md)
  An attempt to authenticate with Apple Watch failed.
- [LAError.Code](laerror-swift.struct/code.md)
  Errors issued by the LocalAuthentication framework.
### Type Properties
- [static var companionNotAvailable: LAError.Code](laerror-swift.struct/companionnotavailable.md)
- [static var errorDomain: String](laerror-swift.struct/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [LAError.Code](laerror-swift.struct/code.md)
  Errors issued by the LocalAuthentication framework.
- [let LAErrorDomain: String](laerrordomain.md)
  The error domain that the framework uses when issuing errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laerror-swift.struct)*