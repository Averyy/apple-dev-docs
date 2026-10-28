# init(enableFan:enableAirConditioner:enableClimateControl:enableAutoMode:airCirculationMode:fanSpeedIndex:fanSpeedPercentage:relativeFanSpeedSetting:temperature:relativeTemperatureSetting:climateZone:carName:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates the intent object with the specified climate settings information.

**Availability**:
- iOS 12.0+ - Deprecated in 15.0
- iPadOS 12.0+ - Deprecated in 15.0
- Mac Catalyst 12.0+ - Deprecated in 15.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
@nonobjc
convenience init(enableFan: Bool? = nil, enableAirConditioner: Bool? = nil, enableClimateControl: Bool? = nil, enableAutoMode: Bool? = nil, airCirculationMode: INCarAirCirculationMode = .unknown, fanSpeedIndex: Int? = nil, fanSpeedPercentage: Double? = nil, relativeFanSpeedSetting: INRelativeSetting = .unknown, temperature: Measurement<UnitTemperature>? = nil, relativeTemperatureSetting: INRelativeSetting = .unknown, climateZone: INCarSeat = .unknown, carName: INSpeakableString? = nil)
```

## Return Value

An initialized intent object or `nil` if the object could not be created.

## Discussion

Normally, you don’t create instances of this class yourself. Instead, Siri creates instances when the user asks to change the vehicle’s climate control settings. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths. Your test code should modify the settings for only one system at a time.

## Parameters

- `enableFan`: A Boolean value indicating whether to turn on the cabin fan system. Specify `nil` if you don’t want to modify this setting.
- `enableAirConditioner`: A Boolean value indicating whether to turn on the air conditioner system. Specify `nil` if you don’t want to modify this setting.
- `enableClimateControl`: A Boolean value indicating whether to turn on the climate control system. Specify `nil` if you don’t want to modify this setting.
- `enableAutoMode`: A Boolean value indicating whether to turn on automatic mode for the climate control system. Specify `nil` if you don’t want to modify this setting.
- `airCirculationMode`: The air circulation mode to apply. Specify [`INCarAirCirculationMode.unknown`](../incaraircirculationmode/unknown.md) if you don’t want to modify this setting.
- `fanSpeedIndex`: The fan speed, specified as an integer indicating the position of the corresponding controls. Specify `nil` if you don’t want to modify this setting.
- `fanSpeedPercentage`: The fan speed, specified as a percentage of the maximum fan speed. Specify `nil` if you don’t want to modify this setting.
- `relativeFanSpeedSetting`: The fan speed, specified as a change relative to the current fan speed. Specify [`INRelativeSetting.unknown`](../inrelativesetting/unknown.md) if you don’t want to modify this setting.
- `temperature`: The desired temperature, specified as a specific number of degrees. Specify `nil` if you don’t want to modify this setting.
- `relativeTemperatureSetting`: The desired temperature, specified as a change relative to the current temperature. Specify [`INRelativeSetting.unknown`](../inrelativesetting/unknown.md) if you don’t want to modify this setting.
- `climateZone`: The climate zone whose settings are changing. Specify [`INCarSeat.unknown`](../incarseat/unknown.md) if you don’t want to modify this setting.
- `carName`: The name of the car to apply the settings to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetclimatesettingsincarintent/init(enablefan:enableairconditioner:enableclimatecontrol:enableautomode:aircirculationmode:fanspeedindex:fanspeedpercentage:relativefanspeedsetting:temperature:relativetemperaturesetting:climatezone:carname:))*