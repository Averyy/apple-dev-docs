# LAError.Code.touchIDNotEnrolled

**Framework**: Local Authentication  
**Kind**: case

The user has no enrolled Touch ID fingers.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case touchIDNotEnrolled
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laerror-swift.struct/code/touchidnotenrolled)*