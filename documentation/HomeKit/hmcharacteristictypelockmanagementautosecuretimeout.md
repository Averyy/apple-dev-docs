# HMCharacteristicTypeLockManagementAutoSecureTimeout

**Framework**: HomeKit  
**Kind**: var

The automatic timeout for a lockable accessory that supports automatic lockout.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let HMCharacteristicTypeLockManagementAutoSecureTimeout: String
```

#### Discussion

The corresponding value is the number of seconds the accessory waits after entering the [`HMCharacteristicValueLockMechanismState.unsecured`](hmcharacteristicvaluelockmechanismstate/unsecured.md) state until it attempts to enter the [`HMCharacteristicValueLockMechanismState.secured`](hmcharacteristicvaluelockmechanismstate/secured.md) state. Write a value of `0` to disable this feature.

## See Also

- [let HMCharacteristicTypeLockManagementControlPoint: String](hmcharacteristictypelockmanagementcontrolpoint.md)
  A control that accepts vendor-specific actions for lock management.
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

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristictypelockmanagementautosecuretimeout)*