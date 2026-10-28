# resolveEnableAirConditioner(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves whether you can enable the air conditioner.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveEnableAirConditioner(for intent: INSetClimateSettingsInCarIntent, with completion: @escaping @Sendable (INBooleanResolutionResult) -> Void)
```

```swift
optional func resolveEnableAirConditioner(for intent: INSetClimateSettingsInCarIntent) async -> INBooleanResolutionResult
```

```objc
- (void) resolveEnableAirConditionerForSetClimateSettingsInCar:(INSetClimateSettingsInCarIntent *) intent withCompletion:(void (^)(INBooleanResolutionResult *resolutionResult)) completion;
```

## Discussion

Implement this method to resolve the user’s request. The intent object passed to this method a Boolean value that indicates whether you can enable the car’s air conditioner.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object with the originally requested value. If the intent doesn’t apply to this setting, return a result that indicates the value isn’t required.

## See Also

### Resolving the Intent Parameters
- [func resolveEnableFan(for: INSetClimateSettingsInCarIntent, with: (INBooleanResolutionResult) -> Void)](./resolveenablefan%28for,with%29.md)
  Resolves whether you can enable the car’s fan.
- [func resolveEnableClimateControl(for: INSetClimateSettingsInCarIntent, with: (INBooleanResolutionResult) -> Void)](./resolveenableclimatecontrol%28for,with%29.md)
  Resolves whether you can enable the climate control system.
- [func resolveEnableAutoMode(for: INSetClimateSettingsInCarIntent, with: (INBooleanResolutionResult) -> Void)](./resolveenableautomode%28for,with%29.md)
  Resolves whether you can enable automatic mode for the car’s climate control.
- [func resolveAirCirculationMode(for: INSetClimateSettingsInCarIntent, with: (INCarAirCirculationModeResolutionResult) -> Void)](./resolveaircirculationmode%28for,with%29.md)
  Resolves the requested air circulation mode.
- [func resolveFanSpeedIndex(for: INSetClimateSettingsInCarIntent, with: (INIntegerResolutionResult) -> Void)](./resolvefanspeedindex%28for,with%29.md)
  Resolves the requested fan speed index.
- [func resolveFanSpeedPercentage(for: INSetClimateSettingsInCarIntent, with: (INDoubleResolutionResult) -> Void)](./resolvefanspeedpercentage%28for,with%29.md)
  Resolves the requested fan speed percentage.
- [func resolveRelativeFanSpeedSetting(for: INSetClimateSettingsInCarIntent, with: (INRelativeSettingResolutionResult) -> Void)](./resolverelativefanspeedsetting%28for,with%29.md)
  Resolves the requested relative qualifier for the fan speed.
- [func resolveTemperature(for: INSetClimateSettingsInCarIntent, with: (INTemperatureResolutionResult) -> Void)](./resolvetemperature%28for,with%29.md)
  Resolves the requested temperature value.
- [func resolveRelativeTemperatureSetting(for: INSetClimateSettingsInCarIntent, with: (INRelativeSettingResolutionResult) -> Void)](./resolverelativetemperaturesetting%28for,with%29.md)
  Resolves the requested relative qualifier for the temperature change.
- [func resolveClimateZone(for: INSetClimateSettingsInCarIntent, with: (INCarSeatResolutionResult) -> Void)](./resolveclimatezone%28for,with%29.md)
  Resolves the requested climate zone.
- [func resolveCarName(for: INSetClimateSettingsInCarIntent, with: (INSpeakableStringResolutionResult) -> Void)](./resolvecarname%28for,with%29.md)
  Resolves the car name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetclimatesettingsincarintenthandling/resolveenableairconditioner(for:with:))*