# INGetUserCurrentRestaurantReservationBookingsIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for fetching and delivering the user’s current reservations.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
protocol INGetUserCurrentRestaurantReservationBookingsIntentHandling : NSObjectProtocol
```

```objc
@protocol INGetUserCurrentRestaurantReservationBookingsIntentHandling <NSObject>
```

#### Overview

Use the methods of the [`INGetUserCurrentRestaurantReservationBookingsIntentHandling`](./ingetusercurrentrestaurantreservationbookingsintenthandling.md) protocol to resolve, confirm, and handle requests to get the reservations associated with the current user. The system delivers an [`INGetUserCurrentRestaurantReservationBookingsIntent`](./ingetusercurrentrestaurantreservationbookingsintent.md) object to your handler when it needs the user’s reservations. Use that intent object to determine whether to retrieve all of the user’s reservations or only some of them. Your Intents extension must be able to fetch the user’s reservations from your systems.

Maps does not require you to resolve or confirm the contents of a get user current restaurant reservation bookings intent before handling it. User interactions drive the selection of data in Maps, ensuring that the data Maps places into an intent object is already valid.

## Topics

### Resolving the Intent Parameters
- [func resolveRestaurant(for: INGetUserCurrentRestaurantReservationBookingsIntent, completion: (INRestaurantResolutionResult) -> Void)](./ingetusercurrentrestaurantreservationbookingsintenthandling/resolverestaurant%28for,completion%29.md)
  Resolves the restaurant to use when searching for reservations.
### Confirming the Response
- [func confirm(getUserCurrentRestaurantReservationBookings: INGetUserCurrentRestaurantReservationBookingsIntent, completion: (INGetUserCurrentRestaurantReservationBookingsIntentResponse) -> Void)](./ingetusercurrentrestaurantreservationbookingsintenthandling/confirm%28getusercurrentrestaurantreservationbookings,completion%29.md)
  Confirms whether you can get the user’s current reservations.
### Handling the Intent
- [func handle(getUserCurrentRestaurantReservationBookings: INGetUserCurrentRestaurantReservationBookingsIntent, completion: (INGetUserCurrentRestaurantReservationBookingsIntentResponse) -> Void)](./ingetusercurrentrestaurantreservationbookingsintenthandling/handle%28getusercurrentrestaurantreservationbookings,completion%29.md)
  Handles fetching the user’s current reservations.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Get User Current Restaurant Reservation Bookings
- [class INGetUserCurrentRestaurantReservationBookingsIntent](./ingetusercurrentrestaurantreservationbookingsintent.md)
  A request for the list of the user’s current reservations.
- [class INGetUserCurrentRestaurantReservationBookingsIntentResponse](./ingetusercurrentrestaurantreservationbookingsintentresponse.md)
  Your app’s response to a get user current restaurant reservation bookings intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetusercurrentrestaurantreservationbookingsintenthandling)*