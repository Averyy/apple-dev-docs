# INSetCarLockStatusIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for requesting to lock or unlock a car.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
protocol INSetCarLockStatusIntentHandling : NSObjectProtocol
```

```objc
@protocol INSetCarLockStatusIntentHandling <NSObject>
```

#### Overview

Use the methods of the `INSetCarLockStatusIntentHandling` protocol to resolve, confirm, and handle requests to lock or unlock the user’s car. Adopt this protocol in an object of your Intents extension that is capable of locking or unlocking the car.

Siri delivers an [`INSetCarLockStatusIntent`](./insetcarlockstatusintent.md) object to your handler when the user asks to lock or unlock the car. The provided intent object can contain the car’s name (if specified), and the requested lock status (locked or unlocked).

## Topics

### Resolving the Intent Parameters
- [func resolveCarName(for: INSetCarLockStatusIntent, with: (INSpeakableStringResolutionResult) -> Void)](./insetcarlockstatusintenthandling/resolvecarname%28for,with%29.md)
  Resolves the name of the user’s car.
- [func resolveLocked(for: INSetCarLockStatusIntent, with: (INBooleanResolutionResult) -> Void)](./insetcarlockstatusintenthandling/resolvelocked%28for,with%29.md)
  Resolves the requested lock status (locked or unlocked).
### Confirming the Response
- [func confirm(intent: INSetCarLockStatusIntent, completion: (INSetCarLockStatusIntentResponse) -> Void)](./insetcarlockstatusintenthandling/confirm%28intent,completion%29.md)
  Confirms that your app can lock or unlock the car.
### Handling the Intent
- [func handle(intent: INSetCarLockStatusIntent, completion: (INSetCarLockStatusIntentResponse) -> Void)](./insetcarlockstatusintenthandling/handle%28intent,completion%29.md)
  Handles locking or unlocking the car.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INCarCommandsDomainHandling](./incarcommandsdomainhandling.md)

## See Also

### Set Car Lock Status
- [class INSetCarLockStatusIntent](./insetcarlockstatusintent.md)
  A request to lock or unlock the user’s car.
- [class INSetCarLockStatusIntentResponse](./insetcarlockstatusintentresponse.md)
  Your app’s response to a request to lock or unlock the car.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetcarlockstatusintenthandling)*