# LAError.Code.biometryNotPaired

**Framework**: Local Authentication  
**Kind**: case  
**Role**: Case

The device supports biometry only using a removable accessory, but no accessory is paired.

**Availability**:
- macOS 11.2+

## Declaration

```swift
case biometryNotPaired
```

```c
LAErrorBiometryNotPaired
```

## See Also

### Biometry failure
- [LAError.Code.biometryDisconnected](./biometrydisconnected.md)
  The device supports biometry only using a removable accessory, but the paired accessory isn’t connected.
- [static var biometryLockout: LAError.Code](./biometrylockout.md)
  Biometry is locked because there were too many failed attempts.
- [static var biometryNotAvailable: LAError.Code](./biometrynotavailable.md)
  Biometry is not available on the device.
- [static var biometryNotEnrolled: LAError.Code](./biometrynotenrolled.md)
  The user has no enrolled biometric identities.
- [LAError.Code.touchIDLockout](./touchidlockout.md)
  Touch ID is locked because there were too many failed attempts.
- [LAError.Code.touchIDNotAvailable](./touchidnotavailable.md)
  Touch ID is not available on the device.
- [LAError.Code.touchIDNotEnrolled](./touchidnotenrolled.md)
  The user has no enrolled Touch ID fingers.
- [LAErrorBiometryLockout](../../laerror-c.enum/laerrorbiometrylockout.md)
  Biometry is locked because there were too many failed attempts.
- [LAErrorBiometryNotAvailable](../../laerror-c.enum/laerrorbiometrynotavailable.md)
  Biometry is not available on the device.
- [LAErrorBiometryNotEnrolled](../../laerror-c.enum/laerrorbiometrynotenrolled.md)
  The user has no enrolled biometric identities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laerror-swift.struct/code/biometrynotpaired)*