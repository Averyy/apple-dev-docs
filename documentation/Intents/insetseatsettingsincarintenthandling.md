# INSetSeatSettingsInCarIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for changing a vehicle’s seat-related settings.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
protocol INSetSeatSettingsInCarIntentHandling : NSObjectProtocol
```

```objc
@protocol INSetSeatSettingsInCarIntentHandling <NSObject>
```

## Overview

Automotive venders can support the [`INSetSeatSettingsInCarIntentHandling`](./insetseatsettingsincarintenthandling.md) protocol in an Intents extension that they ship with their automotive apps. Use the methods of this protocol to resolve, confirm, and handle requests to change the vehicle’s seat-related settings. Your extension should be able to communicate with the vehicle and make the necessary changes.

Siri delivers an [`INSetSeatSettingsInCarIntent`](./insetseatsettingsincarintent.md) object to your handler when the user asks to change any seat settings. The provided intent object contains information that you use to determine which settings changed and what the new settings should be.

## Topics

### Resolving the Intent Parameters
- [func resolveEnableCooling(for: INSetSeatSettingsInCarIntent, with: (INBooleanResolutionResult) -> Void)](./insetseatsettingsincarintenthandling/resolveenablecooling%28for,with%29.md)
  Resolves whether you can enable the seat cooling system.
- [func resolveEnableHeating(for: INSetSeatSettingsInCarIntent, with: (INBooleanResolutionResult) -> Void)](./insetseatsettingsincarintenthandling/resolveenableheating%28for,with%29.md)
  Resolves whether you can enable the seat heating system.
- [func resolveEnableMassage(for: INSetSeatSettingsInCarIntent, with: (INBooleanResolutionResult) -> Void)](./insetseatsettingsincarintenthandling/resolveenablemassage%28for,with%29.md)
  Resolves whether you can enable the seat massage system.
- [func resolveSeat(for: INSetSeatSettingsInCarIntent, with: (INCarSeatResolutionResult) -> Void)](./insetseatsettingsincarintenthandling/resolveseat%28for,with%29.md)
  Resolves the requested seat position.
- [func resolveLevel(for: INSetSeatSettingsInCarIntent, with: (INIntegerResolutionResult) -> Void)](./insetseatsettingsincarintenthandling/resolvelevel%28for,with%29.md)
  Resolves the intensity level of the requested system.
- [func resolveRelativeLevelSetting(for: INSetSeatSettingsInCarIntent, with: (INRelativeSettingResolutionResult) -> Void)](./insetseatsettingsincarintenthandling/resolverelativelevelsetting%28for,with%29.md)
  Resolves the requested relative qualifier for the intensity level.
- [func resolveCarName(for: INSetSeatSettingsInCarIntent, with: (INSpeakableStringResolutionResult) -> Void)](./insetseatsettingsincarintenthandling/resolvecarname%28for,with%29.md)
  Resolves the car name.
### Confirming the Response
- [func confirm(intent: INSetSeatSettingsInCarIntent, completion: (INSetSeatSettingsInCarIntentResponse) -> Void)](./insetseatsettingsincarintenthandling/confirm%28intent,completion%29.md)
  Confirms whether you can change the seat settings.
### Handling the Intent
- [func handle(intent: INSetSeatSettingsInCarIntent, completion: (INSetSeatSettingsInCarIntentResponse) -> Void)](./insetseatsettingsincarintenthandling/handle%28intent,completion%29.md)
  Handles changing the seat settings.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INCarPlayDomainHandling](./incarplaydomainhandling.md)

## See Also

### CarPlay Seat Settings
- [class INSetSeatSettingsInCarIntent](./insetseatsettingsincarintent.md)
  A request to change the seat-related settings in a CarPlay-enabled vehicle.
- [class INSetSeatSettingsInCarIntentResponse](./insetseatsettingsincarintentresponse.md)
  Your app’s response to a set seat settings in car intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetseatsettingsincarintenthandling)*