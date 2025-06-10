# LAError.Code

**Framework**: Local Authentication  
**Kind**: enum

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
enum Code
```

## Topics

### Cancellation
- [LAError.Code.appCancel](laerror-swift.struct/code/appcancel.md)
  The app canceled authentication.
- [LAError.Code.systemCancel](laerror-swift.struct/code/systemcancel.md)
  The system canceled authentication.
- [LAError.Code.userCancel](laerror-swift.struct/code/usercancel.md)
  The user tapped the cancel button in the authentication dialog.
### Biometry failure
- [LAError.Code.biometryDisconnected](laerror-swift.struct/code/biometrydisconnected.md)
  The device supports biometry only using a removable accessory, but the paired accessory isn’t connected.
- [static var biometryLockout: LAError.Code](laerror-swift.struct/code/biometrylockout.md)
  Biometry is locked because there were too many failed attempts.
- [static var biometryNotAvailable: LAError.Code](laerror-swift.struct/code/biometrynotavailable.md)
  Biometry is not available on the device.
- [static var biometryNotEnrolled: LAError.Code](laerror-swift.struct/code/biometrynotenrolled.md)
  The user has no enrolled biometric identities.
- [LAError.Code.biometryNotPaired](laerror-swift.struct/code/biometrynotpaired.md)
  The device supports biometry only using a removable accessory, but no accessory is paired.
- [LAError.Code.touchIDLockout](laerror-swift.struct/code/touchidlockout.md)
  Touch ID is locked because there were too many failed attempts.
- [LAError.Code.touchIDNotAvailable](laerror-swift.struct/code/touchidnotavailable.md)
  Touch ID is not available on the device.
- [LAError.Code.touchIDNotEnrolled](laerror-swift.struct/code/touchidnotenrolled.md)
  The user has no enrolled Touch ID fingers.
### Other errors
- [LAError.Code.authenticationFailed](laerror-swift.struct/code/authenticationfailed.md)
  The user failed to provide valid credentials.
- [LAError.Code.invalidContext](laerror-swift.struct/code/invalidcontext.md)
  The context was previously invalidated.
- [LAError.Code.invalidDimensions](laerror-swift.struct/code/invaliddimensions.md)
- [LAError.Code.notInteractive](laerror-swift.struct/code/notinteractive.md)
  Displaying the required authentication user interface is forbidden.
- [LAError.Code.passcodeNotSet](laerror-swift.struct/code/passcodenotset.md)
  A passcode isn’t set on the device.
- [LAError.Code.userFallback](laerror-swift.struct/code/userfallback.md)
  The user tapped the fallback button in the authentication dialog, but no fallback is available for the authentication policy.
- [LAError.Code.watchNotAvailable](laerror-swift.struct/code/watchnotavailable.md)
  An attempt to authenticate with Apple Watch failed.
### Supporting Constants
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
- [var kLAErrorBiometryNotPaired: Int32](klaerrorbiometrynotpaired.md)
  The device supports biometry only using a removable accessory, but no accessory is paired.
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
- [var kLAErrorPasscodeNotSet: Int32](klaerrorpasscodenotset.md)
  A passcode isn’t set on the device.
- [var kLAErrorUserFallback: Int32](klaerroruserfallback.md)
  The user tapped the fallback button in the authentication dialog, but no fallback is available for the authentication policy.
- [var kLAErrorWatchNotAvailable: Int32](klaerrorwatchnotavailable.md)
  An attempt to authenticate with Apple Watch failed.
### Enumeration Cases
- [LAError.Code.companionNotAvailable](laerror-swift.struct/code/companionnotavailable-swift.enum.case.md)
  Authentication could not start because there was no paired companion device nearby.
### Initializers
- [init?(rawValue: Int)](laerror-swift.struct/code/init(rawvalue:).md)
### Type Properties
- [static var companionNotAvailable: LAError.Code](laerror-swift.struct/code/companionnotavailable-swift.type.property.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct LAError](laerror-swift.struct.md)
  Errors issued by the LocalAuthentication framework.
- [let LAErrorDomain: String](laerrordomain.md)
  The error domain that the framework uses when issuing errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laerror-swift.struct/code)*