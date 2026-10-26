# INActivateCarSignalIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for requesting to activate the car’s signals.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
protocol INActivateCarSignalIntentHandling : NSObjectProtocol
```

```objc
@protocol INActivateCarSignalIntentHandling <NSObject>
```

#### Overview

Use the methods of the `INActivateCarSignalIntentHandling` protocol to resolve, confirm, and handle requests to activate signals on the user’s car. Adopt this protocol in an object of your Intents extension that is capable of activating the car’s signals.

Siri delivers an [`INActivateCarSignalIntent`](./inactivatecarsignalintent.md) object to your handler when the user asks to activate a signal. The provided intent object can contain the car’s name (if specified), and the types of signals (audible or visual).

## Topics

### Resolving the Intent Parameters
- [func resolveCarName(for: INActivateCarSignalIntent, with: (INSpeakableStringResolutionResult) -> Void)](./inactivatecarsignalintenthandling/resolvecarname%28for,with%29.md)
  Resolves the name of the user’s car.
- [func resolveSignals(for: INActivateCarSignalIntent, with: (INCarSignalOptionsResolutionResult) -> Void)](./inactivatecarsignalintenthandling/resolvesignals%28for,with%29.md)
  Resolves the type of signal (audible or visual).
### Confirming the Response
- [func confirm(intent: INActivateCarSignalIntent, completion: (INActivateCarSignalIntentResponse) -> Void)](./inactivatecarsignalintenthandling/confirm%28intent,completion%29.md)
  Confirms that you can activate the car’s signals.
### Handling the Intent
- [func handle(intent: INActivateCarSignalIntent, completion: (INActivateCarSignalIntentResponse) -> Void)](./inactivatecarsignalintenthandling/handle%28intent,completion%29.md)
  Activates the car’s signals.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INCarCommandsDomainHandling](./incarcommandsdomainhandling.md)

## See Also

### Activate Car Signal
- [class INActivateCarSignalIntent](./inactivatecarsignalintent.md)
  A request to activate the signals on the user’s car.
- [class INActivateCarSignalIntentResponse](./inactivatecarsignalintentresponse.md)
  Your app’s response to a request to activate a car’s signals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inactivatecarsignalintenthandling)*