# INGetAvailableRestaurantReservationBookingsIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for generating a list of potential reservation times from which the user can select.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
protocol INGetAvailableRestaurantReservationBookingsIntentHandling : NSObjectProtocol
```

```objc
@protocol INGetAvailableRestaurantReservationBookingsIntentHandling <NSObject>
```

## Overview

Use the methods of the [`INGetAvailableRestaurantReservationBookingsIntentHandling`](./ingetavailablerestaurantreservationbookingsintenthandling.md) protocol to resolve, confirm, and handle requests for an initial set of reservation times from which to select. The system delivers an [`INGetAvailableRestaurantReservationBookingsIntent`](./ingetavailablerestaurantreservationbookingsintent.md) object to your handler with information about the user’s party and preferred reservation time. Use that intent object to generate a list of potential reservation times from which the user can select.

Maps does not require you to resolve or confirm the contents of a get available restaurant reservation bookings intent before handling it. User interactions drive the selection of data in Maps, ensuring that the data Maps places into an intent object is already valid.

## Topics

### Resolving the Intent Parameters
- [func resolveRestaurant(for: INGetAvailableRestaurantReservationBookingsIntent, completion: (INRestaurantResolutionResult) -> Void)](./ingetavailablerestaurantreservationbookingsintenthandling/resolverestaurant%28for,completion%29.md)
  Resolves the restaurant to use when gathering reservation times.
- [func resolvePartySize(for: INGetAvailableRestaurantReservationBookingsIntent, completion: (INIntegerResolutionResult) -> Void)](./ingetavailablerestaurantreservationbookingsintenthandling/resolvepartysize%28for,completion%29.md)
  Resolves the party size to use when generating the reservation times.
- [func resolvePreferredBookingDateComponents(for: INGetAvailableRestaurantReservationBookingsIntent, completion: (INDateComponentsResolutionResult) -> Void)](./ingetavailablerestaurantreservationbookingsintenthandling/resolvepreferredbookingdatecomponents%28for,completion%29.md)
  Resolves the date to use when generating the reservation times.
### Confirming the Response
- [func confirm(getAvailableRestaurantReservationBookings: INGetAvailableRestaurantReservationBookingsIntent, completion: (INGetAvailableRestaurantReservationBookingsIntentResponse) -> Void)](./ingetavailablerestaurantreservationbookingsintenthandling/confirm%28getavailablerestaurantreservationbookings,completion%29.md)
  Confirms whether you can provide a set of potential reservation times.
### Handling the Intent
- [func handle(getAvailableRestaurantReservationBookings: INGetAvailableRestaurantReservationBookingsIntent, completion: (INGetAvailableRestaurantReservationBookingsIntentResponse) -> Void)](./ingetavailablerestaurantreservationbookingsintenthandling/handle%28getavailablerestaurantreservationbookings,completion%29.md)
  Handles generating the list of potential reservation times.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Get Available Restaurant Reservation Bookings
- [class INGetAvailableRestaurantReservationBookingsIntent](./ingetavailablerestaurantreservationbookingsintent.md)
  A request for the time slots available for making a reservation.
- [class INGetAvailableRestaurantReservationBookingsIntentResponse](./ingetavailablerestaurantreservationbookingsintentresponse.md)
  Your app’s response to a get available restaurant reservation bookings intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingsintenthandling)*