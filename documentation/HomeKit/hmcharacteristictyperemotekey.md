# HMCharacteristicTypeRemoteKey

**Framework**: HomeKit  
**Kind**: var

The accessory remote control key.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
let HMCharacteristicTypeRemoteKey: String
```

#### Overview

`HMCharacteristicTypeRemoteKey` describes a mechanism to send control key presses to televisions. The handling of the key presses depend on the current active input source, or the application that is running. The corresponding value is one of the constants in the [`HMCharacteristicValueRemoteKey`](hmcharacteristicvalueremotekey.md) enumeration.

## Topics

### Values
- [enum HMCharacteristicValueRemoteKey](hmcharacteristicvalueremotekey.md)
  Values for the state of the remote.

## See Also

- [let HMCharacteristicTypeLockManagementAutoSecureTimeout: String](hmcharacteristictypelockmanagementautosecuretimeout.md)
  The automatic timeout for a lockable accessory that supports automatic lockout.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristictyperemotekey)*