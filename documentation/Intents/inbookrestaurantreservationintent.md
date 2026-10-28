# INBookRestaurantReservationIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request to create a reservation at the specified restaurant.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class INBookRestaurantReservationIntent
```

```objc
@interface INBookRestaurantReservationIntent : INIntent
```

## Overview

An [`INBookRestaurantReservationIntent`](./inbookrestaurantreservationintent.md) object asks you to book the reservation time selected by the user. Maps sends this intent to your Intents extension when the user selects a reservation time from the available options. Use this intent object to obtain the details of the reservation, including the time slot and any selected special offers. Use those details to confirm the reservation with the restaurant and store the results in your system.

Booking a reservation is the last step in the reservation creation process. By the time the system delivers this intent to your Intents extension, the user has already had an opportunity to view a list of potential reservation times and configure the details of the reservation request. This intent object contains all of the final choices made by the user.

To handle this intent, the handler object in your Intents extension must adopt the [`INBookRestaurantReservationIntentHandling`](./inbookrestaurantreservationintenthandling.md) protocol. Your handler should resolve and confirm any parameters and create an [`INBookRestaurantReservationIntentResponse`](./inbookrestaurantreservationintentresponse.md) object with the status of the reservation.

### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Maps |
| Always requires unlocked device | Yes |

## Topics

### Initializing the Intent Object
- [init(restaurant: INRestaurant, booking: DateComponents, partySize: Int, bookingIdentifier: String?, guest: INRestaurantGuest?, selectedOffer: INRestaurantOffer?, guestProvidedSpecialRequestText: String?)](./inbookrestaurantreservationintent/init%28restaurant,booking,partysize,bookingidentifier,guest,selectedoffer,guestprovidedspecialrequesttext%29.md)
  Initializes the intent object with the specified booking information.
### Getting the Restaurant Information
- [var restaurant: INRestaurant](./inbookrestaurantreservationintent/restaurant.md)
  The restaurant to contact regarding the booking.
### Getting the Booking Details
- [var bookingDateComponents: DateComponents](./inbookrestaurantreservationintent/bookingdatecomponents.md)
  The date and time of the reservation.
- [var bookingIdentifier: String?](./inbookrestaurantreservationintent/bookingidentifier.md)
  The unique identifier associated with the initial reservation data.
- [var partySize: Int](./inbookrestaurantreservationintent/partysize.md)
  The total number of people in the user’s party.
- [var guest: INRestaurantGuest?](./inbookrestaurantreservationintent/guest.md)
  The identity of the guest associated with the reservation.
### Getting Special Requests and Offers
- [var guestProvidedSpecialRequestText: String?](./inbookrestaurantreservationintent/guestprovidedspecialrequesttext.md)
  Information about any special requests made by the user.
- [var selectedOffer: INRestaurantOffer?](./inbookrestaurantreservationintent/selectedoffer.md)
  The special offer, if any, selected by the user.
### Initializers
- [init(restaurant: INRestaurant, bookingDateComponents: DateComponents, partySize: Int, bookingIdentifier: String?, guest: INRestaurantGuest?, selectedOffer: INRestaurantOffer?, guestProvidedSpecialRequestText: String?)](./inbookrestaurantreservationintent/init%28restaurant,bookingdatecomponents,partysize,bookingidentifier,guest,selectedoffer,guestprovidedspecialrequesttext%29.md)

## Relationships

### Inherits From
- [INIntent](./inintent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [INIntentSetImageKeyPath](./inintentsetimagekeypath.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Book Restaurant Reservation
- [protocol INBookRestaurantReservationIntentHandling](./inbookrestaurantreservationintenthandling.md)
  The handler interface booking a reservation that the user selected.
- [class INBookRestaurantReservationIntentResponse](./inbookrestaurantreservationintentresponse.md)
  Your app’s response to a book restaurant reservation intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbookrestaurantreservationintent)*