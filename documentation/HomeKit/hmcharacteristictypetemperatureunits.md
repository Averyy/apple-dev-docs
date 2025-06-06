# HMCharacteristicTypeTemperatureUnits

**Framework**: HomeKit  
**Kind**: var

The units of temperature currently active on the accessory.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let HMCharacteristicTypeTemperatureUnits: String
```

#### Discussion

The corresponding value is one of the constants from the [`HMCharacteristicValueTemperatureUnit`](hmcharacteristicvaluetemperatureunit.md) enumeration.

HomeKit always reports temperature values in degrees Celsius, but your app should display the temperature in units chosen by the user.

## Topics

### Values
- [enum HMCharacteristicValueTemperatureUnit](hmcharacteristicvaluetemperatureunit.md)
  Possible values for the temperature units currently active on the accessory.

## See Also

- [let HMCharacteristicTypeCurrentTemperature: String](hmcharacteristictypecurrenttemperature.md)
  The current temperature measured by the accessory.
- [let HMCharacteristicTypeTargetTemperature: String](hmcharacteristictypetargettemperature.md)
  The target temperature for the accessory to achieve.
- [let HMCharacteristicTypeTargetHeatingCooling: String](hmcharacteristictypetargetheatingcooling.md)
  The target heating or cooling mode for a thermostat.
- [let HMCharacteristicTypeCurrentHeatingCooling: String](hmcharacteristictypecurrentheatingcooling.md)
  The current heating or cooling mode for a thermostat.
- [let HMCharacteristicTypeTargetHeaterCoolerState: String](hmcharacteristictypetargetheatercoolerstate.md)
  The target state for a device that heats or cools, like an oven or a refrigerator.
- [let HMCharacteristicTypeCurrentHeaterCoolerState: String](hmcharacteristictypecurrentheatercoolerstate.md)
  The current state for a device that heats or cools, like an oven or a refrigerator.
- [let HMCharacteristicTypeCoolingThreshold: String](hmcharacteristictypecoolingthreshold.md)
  The temperature above which cooling will be active.
- [let HMCharacteristicTypeHeatingThreshold: String](hmcharacteristictypeheatingthreshold.md)
  The temperature below which heating will be active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristictypetemperatureunits)*