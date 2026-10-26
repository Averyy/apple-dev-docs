# INSetDefrosterSettingsInCarIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for changing a vehicle’s defroster settings.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
protocol INSetDefrosterSettingsInCarIntentHandling : NSObjectProtocol
```

```objc
@protocol INSetDefrosterSettingsInCarIntentHandling <NSObject>
```

#### Overview

Automotive vendors can support the [`INSetDefrosterSettingsInCarIntentHandling`](./insetdefrostersettingsincarintenthandling.md) protocol in an Intents extension that they ship with their automotive apps. Use the methods of this protocol to resolve, confirm, and handle requests to change the vehicle’s defroster settings. Your extension should be able to communicate with the vehicle and make the necessary climate control changes.

Siri delivers an [`INSetDefrosterSettingsInCarIntent`](./insetdefrostersettingsincarintent.md) object to your handler when the user asks to change the defroster change. The intent object contains information that you use to determine the new defroster settings and to make the change.

## Topics

### Resolving the Intent Parameters
- [func resolveEnable(for: INSetDefrosterSettingsInCarIntent, with: (INBooleanResolutionResult) -> Void)](./insetdefrostersettingsincarintenthandling/resolveenable%28for,with%29.md)
  Resolves whether you can enable or disable the defroster setting.
- [func resolveDefroster(for: INSetDefrosterSettingsInCarIntent, with: (INCarDefrosterResolutionResult) -> Void)](./insetdefrostersettingsincarintenthandling/resolvedefroster%28for,with%29.md)
  Resolves which defroster to change.
- [func resolveCarName(for: INSetDefrosterSettingsInCarIntent, with: (INSpeakableStringResolutionResult) -> Void)](./insetdefrostersettingsincarintenthandling/resolvecarname%28for,with%29.md)
  Resolves the car name.
### Confirming the Response
- [func confirm(intent: INSetDefrosterSettingsInCarIntent, completion: (INSetDefrosterSettingsInCarIntentResponse) -> Void)](./insetdefrostersettingsincarintenthandling/confirm%28intent,completion%29.md)
  Confirms whether you can change the defroster settings.
### Handling the Intent
- [func handle(intent: INSetDefrosterSettingsInCarIntent, completion: (INSetDefrosterSettingsInCarIntentResponse) -> Void)](./insetdefrostersettingsincarintenthandling/handle%28intent,completion%29.md)
  Handles changing the defroster settings.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INCarPlayDomainHandling](./incarplaydomainhandling.md)

## See Also

### CarPlay Defroster Settings
- [class INSetDefrosterSettingsInCarIntent](./insetdefrostersettingsincarintent.md)
  A request to change the defroster settings in a CarPlay-enabled vehicle.
- [class INSetDefrosterSettingsInCarIntentResponse](./insetdefrostersettingsincarintentresponse.md)
  Your app’s response to a set defroster settings in car intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetdefrostersettingsincarintenthandling)*