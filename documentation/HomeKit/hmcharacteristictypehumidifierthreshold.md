# HMCharacteristicTypeHumidifierThreshold

**Framework**: HomeKit  
**Kind**: var

The humidity below which a humidifier should begin to work.

**Availability**:
- iOS 10.2+
- iPadOS 10.2+
- Mac Catalyst 10.2+
- tvOS 10.1+
- visionOS 1.0+
- watchOS 3.1.1+

## Declaration

```swift
let HMCharacteristicTypeHumidifierThreshold: String
```

#### Discussion

The corresponding value is a floating point percentage representing the relative humidity threshold. Relative humidity is a measure of the amount of water in the air relative to the maximum it can hold at the current temperature.

## See Also

- [let HMCharacteristicTypeCurrentRelativeHumidity: String](hmcharacteristictypecurrentrelativehumidity.md)
  The current relative humidity measured by the accessory.
- [let HMCharacteristicTypeTargetRelativeHumidity: String](hmcharacteristictypetargetrelativehumidity.md)
  The target relative humidity for the accessory to achieve.
- [let HMCharacteristicTypeCurrentHumidifierDehumidifierState: String](hmcharacteristictypecurrenthumidifierdehumidifierstate.md)
  The current state of a humidifier or dehumidifier accessory.
- [let HMCharacteristicTypeTargetHumidifierDehumidifierState: String](hmcharacteristictypetargethumidifierdehumidifierstate.md)
  The state that a humidifier or dehumidifier accessory should try to achieve.
- [let HMCharacteristicTypeDehumidifierThreshold: String](hmcharacteristictypedehumidifierthreshold.md)
  The humidity above which a dehumidifier should begin to work.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristictypehumidifierthreshold)*