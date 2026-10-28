# INBookRestaurantReservationIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface booking a reservation that the user selected.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
protocol INBookRestaurantReservationIntentHandling : NSObjectProtocol
```

```objc
@protocol INBookRestaurantReservationIntentHandling <NSObject>
```

## Overview

Use the methods of the [`INBookRestaurantReservationIntentHandling`](./inbookrestaurantreservationintenthandling.md) protocol to resolve, confirm, and handle requests to book a reservation based on the provided information. The system delivers an [`INBookRestaurantReservationIntent`](./inbookrestaurantreservationintent.md) object to your handler with the reservation details, including the restaurant, date, party size, and any special offers selected by the user. Use that intent object to complete the reservation in your system and to communicate the reservation details to the restaurant itself.

Maps does not require you to resolve or confirm the contents of a get available restaurant reservation bookings intent before handling it. User interactions drive the selection of data in Maps, ensuring that the data Maps places into an intent object is already valid.

## Topics

### Resolving the Intent Parameters
- [func resolveRestaurant(for: INBookRestaurantReservationIntent, completion: (INRestaurantResolutionResult) -> Void)](./inbookrestaurantreservationintenthandling/resolverestaurant%28for,completion%29.md)
  Resolves the restaurant associated with the reservation.
- [func resolveBookingDateComponents(for: INBookRestaurantReservationIntent, completion: (INDateComponentsResolutionResult) -> Void)](./inbookrestaurantreservationintenthandling/resolvebookingdatecomponents%28for,completion%29.md)
  Resolves the date of the reservation.
- [func resolvePartySize(for: INBookRestaurantReservationIntent, completion: (INIntegerResolutionResult) -> Void)](./inbookrestaurantreservationintenthandling/resolvepartysize%28for,completion%29.md)
  Resolves the number of people in the user’s party.
- [func resolveGuest(for: INBookRestaurantReservationIntent, completion: (INRestaurantGuestResolutionResult) -> Void)](./inbookrestaurantreservationintenthandling/resolveguest%28for,completion%29.md)
  Resolves the identity of the guest associated with the reservation.
- [func resolveGuestProvidedSpecialRequestText(for: INBookRestaurantReservationIntent, completion: (INStringResolutionResult) -> Void)](./inbookrestaurantreservationintenthandling/resolveguestprovidedspecialrequesttext%28for,completion%29.md)
  Resolves any special requests made in connection with the reservation.
### Confirming the Response
- [func confirm(bookRestaurantReservation: INBookRestaurantReservationIntent, completion: (INBookRestaurantReservationIntentResponse) -> Void)](./inbookrestaurantreservationintenthandling/confirm%28bookrestaurantreservation,completion%29.md)
  Confirms whether you can complete the reservation.
### Handling the Intent
- [func handle(bookRestaurantReservation: INBookRestaurantReservationIntent, completion: (INBookRestaurantReservationIntentResponse) -> Void)](./inbookrestaurantreservationintenthandling/handle%28bookrestaurantreservation,completion%29.md)
  Handles completing the user’s reservation.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Book Restaurant Reservation
- [class INBookRestaurantReservationIntent](./inbookrestaurantreservationintent.md)
  A request to create a reservation at the specified restaurant.
- [class INBookRestaurantReservationIntentResponse](./inbookrestaurantreservationintentresponse.md)
  Your app’s response to a book restaurant reservation intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbookrestaurantreservationintenthandling)*