# INSetRadioStationIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for changing a radio station.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
protocol INSetRadioStationIntentHandling : NSObjectProtocol
```

```objc
@protocol INSetRadioStationIntentHandling <NSObject>
```

## Overview

Use the methods of the [`INSetRadioStationIntentHandling`](./insetradiostationintenthandling.md) protocol to resolve, confirm, and handle requests to change radio stations from your app. Your extension should be able to change the radio station based on the provided information. For example, automotive vendors should be able to use the information to update the settings of a vehicle’s entertainment system.

Siri delivers an [`INSetRadioStationIntent`](./insetradiostationintent.md) object to your handler when the user asks to change the current radio station. The provided intent object contains information that you use to determine the new station.

## Topics

### Resolving the Intent Parameters
- [func resolveRadioType(for: INSetRadioStationIntent, with: (INRadioTypeResolutionResult) -> Void)](./insetradiostationintenthandling/resolveradiotype%28for,with%29.md)
  Resolves the radio type.
- [func resolveFrequency(for: INSetRadioStationIntent, with: (INDoubleResolutionResult) -> Void)](./insetradiostationintenthandling/resolvefrequency%28for,with%29.md)
  Resolves the radio station frequency.
- [func resolveStationName(for: INSetRadioStationIntent, with: (INStringResolutionResult) -> Void)](./insetradiostationintenthandling/resolvestationname%28for,with%29.md)
  Resolves the name of the radio station.
- [func resolveChannel(for: INSetRadioStationIntent, with: (INStringResolutionResult) -> Void)](./insetradiostationintenthandling/resolvechannel%28for,with%29.md)
  Resolves the channel number for the radio station.
- [func resolvePresetNumber(for: INSetRadioStationIntent, with: (INIntegerResolutionResult) -> Void)](./insetradiostationintenthandling/resolvepresetnumber%28for,with%29.md)
  Resolves the preset number used to select the radio station.
### Confirming the Response
- [func confirm(intent: INSetRadioStationIntent, completion: (INSetRadioStationIntentResponse) -> Void)](./insetradiostationintenthandling/confirm%28intent,completion%29.md)
  Confirms whether you can change the radio station.
### Handling the Intent
- [func handle(intent: INSetRadioStationIntent, completion: (INSetRadioStationIntentResponse) -> Void)](./insetradiostationintenthandling/handle%28intent,completion%29.md)
  Handles changing the radio station.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INRadioDomainHandling](./inradiodomainhandling.md)

## See Also

### CarPlay Radio Station Settings
- [class INSetRadioStationIntent](./insetradiostationintent.md)
  A request to change the current radio station.
- [class INSetRadioStationIntentResponse](./insetradiostationintentresponse.md)
  Your app’s response to a set radio station intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetradiostationintenthandling)*