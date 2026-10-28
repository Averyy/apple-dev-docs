# HMCharacteristicTypeCurrentSecuritySystemState

**Framework**: HomeKit  
**Kind**: var  
**Role**: Global Variable

The current security system state.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let HMCharacteristicTypeCurrentSecuritySystemState: String
```

```c
extern NSString * const HMCharacteristicTypeCurrentSecuritySystemState;
```

## Discussion

The corresponding value is one of the constants in the [`HMCharacteristicValueCurrentSecuritySystemState`](./hmcharacteristicvaluecurrentsecuritysystemstate.md) enumeration.

## Topics

### Values
- [enum HMCharacteristicValueCurrentSecuritySystemState](./hmcharacteristicvaluecurrentsecuritysystemstate.md)
  Possible values for the current security system state.

## See Also

### Safety and security
- [let HMCharacteristicTypeTargetSecuritySystemState: String](./hmcharacteristictypetargetsecuritysystemstate.md)
  The target security system state.
- [let HMCharacteristicTypeObstructionDetected: String](./hmcharacteristictypeobstructiondetected.md)
  An indicator of whether an obstruction is detected, as when something prevents a garage door from closing.
- [let HMCharacteristicTypeOccupancyDetected: String](./hmcharacteristictypeoccupancydetected.md)
  An indicator of whether the home is occupied.
- [let HMCharacteristicTypeSecuritySystemAlarmType: String](./hmcharacteristictypesecuritysystemalarmtype.md)
  The alarm trigger state.
- [let HMCharacteristicPropertyRequiresAuthorizationData: String](./hmcharacteristicpropertyrequiresauthorizationdata.md)
  A variable that specifies that the characteristic requires authorization data to write.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristictypecurrentsecuritysystemstate)*