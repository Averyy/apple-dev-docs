# initWithEnableFan:enableAirConditioner:enableClimateControl:enableAutoMode:airCirculationMode:fanSpeedIndex:fanSpeedPercentage:relativeFanSpeedSetting:temperature:relativeTemperatureSetting:climateZone:

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Initializes the intent object with the specified climate settings information.

**Availability**:
- iOS 10.0+ - Deprecated in 12.0
- iPadOS 10.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 10.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 5.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```objc
- (instancetype) initWithEnableFan:(NSNumber *) enableFan enableAirConditioner:(NSNumber *) enableAirConditioner enableClimateControl:(NSNumber *) enableClimateControl enableAutoMode:(NSNumber *) enableAutoMode airCirculationMode:(INCarAirCirculationMode) airCirculationMode fanSpeedIndex:(NSNumber *) fanSpeedIndex fanSpeedPercentage:(NSNumber *) fanSpeedPercentage relativeFanSpeedSetting:(INRelativeSetting) relativeFanSpeedSetting temperature:(NSMeasurement<NSUnitTemperature *> *) temperature relativeTemperatureSetting:(INRelativeSetting) relativeTemperatureSetting climateZone:(INCarSeat) climateZone;
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

## See Also

### Initializing the Intent Object
- [- initWithEnableFan:enableAirConditioner:enableClimateControl:enableAutoMode:airCirculationMode:fanSpeedIndex:fanSpeedPercentage:relativeFanSpeedSetting:temperature:relativeTemperatureSetting:climateZone:carName:](./initwithenablefan_enableairconditioner_enableclimatecontrol_enableautomode_aircirculationmode_fanspeedindex_fanspeedpercentage_relativefanspeedsetting_temperature_relativetemperaturesetting_climatezone_carname_.md)
  Initializes the intent object with the specified climate settings information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetclimatesettingsincarintent/initwithenablefan:enableairconditioner:enableclimatecontrol:enableautomode:aircirculationmode:fanspeedindex:fanspeedpercentage:relativefanspeedsetting:temperature:relativetemperaturesetting:climatezone:)*