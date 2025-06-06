# HMCharacteristicTypeLockManagementControlPoint

**Framework**: HomeKit  
**Kind**: var

A control that accepts vendor-specific actions for lock management.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let HMCharacteristicTypeLockManagementControlPoint: String
```

#### Discussion

The corresponding write-only value takes data in a format specified by the accessory’s manufacturer.

## See Also

- [let HMCharacteristicTypeLockManagementAutoSecureTimeout: String](hmcharacteristictypelockmanagementautosecuretimeout.md)
  The automatic timeout for a lockable accessory that supports automatic lockout.
- [let HMCharacteristicTypeLockMechanismLastKnownAction: String](hmcharacteristictypelockmechanismlastknownaction.md)
  The last known action of the locking mechanism.
- [let HMCharacteristicTypeLockPhysicalControls: String](hmcharacteristictypelockphysicalcontrols.md)
  The lock’s physical control state.
- [let HMCharacteristicTypeMotionDetected: String](hmcharacteristictypemotiondetected.md)
  An indicator of whether the accessory has detected motion.
- [let HMCharacteristicTypeCurrentLockMechanismState: String](hmcharacteristictypecurrentlockmechanismstate.md)
  The current state of the locking mechanism.
- [let HMCharacteristicTypeTargetLockMechanismState: String](hmcharacteristictypetargetlockmechanismstate.md)
  The target state for the locking mechanism.
- [let HMCharacteristicTypeRemoteKey: String](hmcharacteristictyperemotekey.md)
  The accessory remote control key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristictypelockmanagementcontrolpoint)*