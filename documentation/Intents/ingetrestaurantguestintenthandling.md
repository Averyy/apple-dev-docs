# INGetRestaurantGuestIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for fetching information about the person making a reservation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
protocol INGetRestaurantGuestIntentHandling : NSObjectProtocol
```

```objc
@protocol INGetRestaurantGuestIntentHandling <NSObject>
```

#### Overview

Use the methods of the [`INGetRestaurantGuestIntentHandling`](./ingetrestaurantguestintenthandling.md) protocol to confirm and handle requests to return information about the person making a reservation. The system delivers an [`INGetRestaurantGuestIntent`](./ingetrestaurantguestintent.md) object to your handler when the user begins the process of making a reservation. Your handler object should return information about the current user along with preferences about how the system should display that user’s information. Your handler is also responsible for specifying whether the user information displayed by the system is changable before assigning it to the reservation.

Maps does not require you to confirm the contents of a get restaurant guest intent before handling it. User interactions drive the selection of data in Maps, ensuring that the data Maps places into an intent object is already valid.

## Topics

### Confirming the Response
- [func confirm(getRestaurantGuest: INGetRestaurantGuestIntent, completion: (INGetRestaurantGuestIntentResponse) -> Void)](./ingetrestaurantguestintenthandling/confirm%28getrestaurantguest,completion%29.md)
  Confirms whether you can provide the guest information.
### Handling the Intent
- [func handle(getRestaurantGuest: INGetRestaurantGuestIntent, completion: (INGetRestaurantGuestIntentResponse) -> Void)](./ingetrestaurantguestintenthandling/handle%28getrestaurantguest,completion%29.md)
  Handles returning the information about the user making the reservation.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Get Restaurant Guest
- [class INGetRestaurantGuestIntent](./ingetrestaurantguestintent.md)
  A request for information about the guest who is making reservations.
- [class INGetRestaurantGuestIntentResponse](./ingetrestaurantguestintentresponse.md)
  Your app’s response to a get restaurant guest intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetrestaurantguestintenthandling)*