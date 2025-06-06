# HMCharacteristicTypeCurrentRelativeHumidity

**Framework**: HomeKit  
**Kind**: var

The current relative humidity measured by the accessory.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let HMCharacteristicTypeCurrentRelativeHumidity: String
```

#### Discussion

The corresponding value is a floating point percentage representing the current relative humidity. This is a measure of the amount of water in the air relative to the maximum it can hold at the current temperature.

## See Also

- [let HMCharacteristicTypeTargetRelativeHumidity: String](hmcharacteristictypetargetrelativehumidity.md)
  The target relative humidity for the accessory to achieve.
- [let HMCharacteristicTypeCurrentHumidifierDehumidifierState: String](hmcharacteristictypecurrenthumidifierdehumidifierstate.md)
  The current state of a humidifier or dehumidifier accessory.
- [let HMCharacteristicTypeTargetHumidifierDehumidifierState: String](hmcharacteristictypetargethumidifierdehumidifierstate.md)
  The state that a humidifier or dehumidifier accessory should try to achieve.
- [let HMCharacteristicTypeHumidifierThreshold: String](hmcharacteristictypehumidifierthreshold.md)
  The humidity below which a humidifier should begin to work.
- [let HMCharacteristicTypeDehumidifierThreshold: String](hmcharacteristictypedehumidifierthreshold.md)
  The humidity above which a dehumidifier should begin to work.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristictypecurrentrelativehumidity)*