# INListCarsIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for requesting a list of the user’s electric vehicles.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
protocol INListCarsIntentHandling : NSObjectProtocol
```

```objc
@protocol INListCarsIntentHandling <NSObject>
```

#### Overview

Use the methods of the `INListCarsIntentHandling` protocol to confirm and handle requests from Maps for a list of the user’s electric vehicles. Adopt this protocol in an object of your Intents extension that can provide information about each of the user’s vehicles.

Maps delivers an [`INListCarsIntent`](./inlistcarsintent.md) object to your handler when it needs to present a list of vehicles to the user. The  intent is a placeholder object and doesn’t provide any contextual information pertaining to the request.

## Topics

### Confirming the Intent
- [func confirm(intent: INListCarsIntent, completion: (INListCarsIntentResponse) -> Void)](./inlistcarsintenthandling/confirm%28intent,completion%29.md)
  Confirms that you can provide a list of the user’s electric vehicles.
### Handling the Intent
- [func handle(intent: INListCarsIntent, completion: (INListCarsIntentResponse) -> Void)](./inlistcarsintenthandling/handle%28intent,completion%29.md)
  Provides a list of the user’s electric vehicles.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### List Cars
- [class INListCarsIntent](./inlistcarsintent.md)
  An intent for retrieving a list of the user’s electric vehicles.
- [class INListCarsIntentResponse](./inlistcarsintentresponse.md)
  Your app’s response to a request to list the user’s electric vehicles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlistcarsintenthandling)*