# INSetClimateSettingsInCarIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for changing a vehicle’s climate control settings.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
protocol INSetClimateSettingsInCarIntentHandling : NSObjectProtocol
```

```objc
@protocol INSetClimateSettingsInCarIntentHandling <NSObject>
```

#### Overview

Automotive vendors can support the [`INSetClimateSettingsInCarIntentHandling`](./insetclimatesettingsincarintenthandling.md) protocol in an Intents extension that they ship with their automotive apps. Use the methods of this protocol to resolve, confirm, and handle requests to change the vehicle’s current climate control settings. Your extension should be able to communicate with the vehicle and make the necessary changes.

Siri delivers an [`INSetClimateSettingsInCarIntent`](./insetclimatesettingsincarintent.md) object to your handler when the user asks to change any climate settings. The provided intent object contains information that you use to determine which settings changed and what the new settings should be.

## Topics

### Resolving the Intent Parameters
- [func resolveEnableFan(for: INSetClimateSettingsInCarIntent, with: (INBooleanResolutionResult) -> Void)](./insetclimatesettingsincarintenthandling/resolveenablefan%28for,with%29.md)
  Resolves whether you can enable the car’s fan.
- [func resolveEnableAirConditioner(for: INSetClimateSettingsInCarIntent, with: (INBooleanResolutionResult) -> Void)](./insetclimatesettingsincarintenthandling/resolveenableairconditioner%28for,with%29.md)
  Resolves whether you can enable the air conditioner.
- [func resolveEnableClimateControl(for: INSetClimateSettingsInCarIntent, with: (INBooleanResolutionResult) -> Void)](./insetclimatesettingsincarintenthandling/resolveenableclimatecontrol%28for,with%29.md)
  Resolves whether you can enable the climate control system.
- [func resolveEnableAutoMode(for: INSetClimateSettingsInCarIntent, with: (INBooleanResolutionResult) -> Void)](./insetclimatesettingsincarintenthandling/resolveenableautomode%28for,with%29.md)
  Resolves whether you can enable automatic mode for the car’s climate control.
- [func resolveAirCirculationMode(for: INSetClimateSettingsInCarIntent, with: (INCarAirCirculationModeResolutionResult) -> Void)](./insetclimatesettingsincarintenthandling/resolveaircirculationmode%28for,with%29.md)
  Resolves the requested air circulation mode.
- [func resolveFanSpeedIndex(for: INSetClimateSettingsInCarIntent, with: (INIntegerResolutionResult) -> Void)](./insetclimatesettingsincarintenthandling/resolvefanspeedindex%28for,with%29.md)
  Resolves the requested fan speed index.
- [func resolveFanSpeedPercentage(for: INSetClimateSettingsInCarIntent, with: (INDoubleResolutionResult) -> Void)](./insetclimatesettingsincarintenthandling/resolvefanspeedpercentage%28for,with%29.md)
  Resolves the requested fan speed percentage.
- [func resolveRelativeFanSpeedSetting(for: INSetClimateSettingsInCarIntent, with: (INRelativeSettingResolutionResult) -> Void)](./insetclimatesettingsincarintenthandling/resolverelativefanspeedsetting%28for,with%29.md)
  Resolves the requested relative qualifier for the fan speed.
- [func resolveTemperature(for: INSetClimateSettingsInCarIntent, with: (INTemperatureResolutionResult) -> Void)](./insetclimatesettingsincarintenthandling/resolvetemperature%28for,with%29.md)
  Resolves the requested temperature value.
- [func resolveRelativeTemperatureSetting(for: INSetClimateSettingsInCarIntent, with: (INRelativeSettingResolutionResult) -> Void)](./insetclimatesettingsincarintenthandling/resolverelativetemperaturesetting%28for,with%29.md)
  Resolves the requested relative qualifier for the temperature change.
- [func resolveClimateZone(for: INSetClimateSettingsInCarIntent, with: (INCarSeatResolutionResult) -> Void)](./insetclimatesettingsincarintenthandling/resolveclimatezone%28for,with%29.md)
  Resolves the requested climate zone.
- [func resolveCarName(for: INSetClimateSettingsInCarIntent, with: (INSpeakableStringResolutionResult) -> Void)](./insetclimatesettingsincarintenthandling/resolvecarname%28for,with%29.md)
  Resolves the car name.
### Confirming the Response
- [func confirm(intent: INSetClimateSettingsInCarIntent, completion: (INSetClimateSettingsInCarIntentResponse) -> Void)](./insetclimatesettingsincarintenthandling/confirm%28intent,completion%29.md)
  Confirms whether you can change the climate settings.
### Handling the Intent
- [func handle(intent: INSetClimateSettingsInCarIntent, completion: (INSetClimateSettingsInCarIntentResponse) -> Void)](./insetclimatesettingsincarintenthandling/handle%28intent,completion%29.md)
  Handles changing the climate control settings.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INCarPlayDomainHandling](./incarplaydomainhandling.md)

## See Also

### CarPlay Climate Settings
- [class INSetClimateSettingsInCarIntent](./insetclimatesettingsincarintent.md)
  A request to change the climate settings in a CarPlay-enabled vehicle.
- [class INSetClimateSettingsInCarIntentResponse](./insetclimatesettingsincarintentresponse.md)
  Your app’s response to a set climate settings in car intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetclimatesettingsincarintenthandling)*