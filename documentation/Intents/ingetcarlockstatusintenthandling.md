# INGetCarLockStatusIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for requesting the current status of the car’s locks.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
protocol INGetCarLockStatusIntentHandling : NSObjectProtocol
```

```objc
@protocol INGetCarLockStatusIntentHandling <NSObject>
```

## Overview

Use the methods of the `INGetCarLockStatusIntentHandling` protocol to resolve, confirm, and handle requests for the current status of the car’s locks. Adopt this protocol in an object of your Intents extension that’s capable of accessing the status of the car’s locks.

Siri delivers an [`INGetCarLockStatusIntent`](./ingetcarlockstatusintent.md) object to your handler when the user asks whether the car is locked or unlocked. The provided intent object can contain the car’s name (if specified).

## Topics

### Resolving the Intent Parameters
- [func resolveCarName(for: INGetCarLockStatusIntent, with: (INSpeakableStringResolutionResult) -> Void)](./ingetcarlockstatusintenthandling/resolvecarname%28for,with%29.md)
  Resolves the name of the user’s car.
### Confirming the Response
- [func confirm(intent: INGetCarLockStatusIntent, completion: (INGetCarLockStatusIntentResponse) -> Void)](./ingetcarlockstatusintenthandling/confirm%28intent,completion%29.md)
  Confirms that you can access the status of the car’s locks.
### Handling the Intent
- [func handle(intent: INGetCarLockStatusIntent, completion: (INGetCarLockStatusIntentResponse) -> Void)](./ingetcarlockstatusintenthandling/handle%28intent,completion%29.md)
  Accesses and returns the current status of the car’s locks.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INCarCommandsDomainHandling](./incarcommandsdomainhandling.md)

## See Also

### Get Car Lock Status
- [class INGetCarLockStatusIntent](./ingetcarlockstatusintent.md)
  A request to get the lock status of the user’s car.
- [class INGetCarLockStatusIntentResponse](./ingetcarlockstatusintentresponse.md)
  Your app’s response to a request to get the car’s lock status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarlockstatusintenthandling)*