# INGetAvailableRestaurantReservationBookingDefaultsIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for providing default values to the system when pre-fetching an initial set of possible reservation times.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
protocol INGetAvailableRestaurantReservationBookingDefaultsIntentHandling : NSObjectProtocol
```

```objc
@protocol INGetAvailableRestaurantReservationBookingDefaultsIntentHandling <NSObject>
```

## Overview

Use the methods of the [`INGetAvailableRestaurantReservationBookingDefaultsIntentHandling`](./ingetavailablerestaurantreservationbookingdefaultsintenthandling.md) protocol to resolve, confirm, and handle requests for default values for the system to use when pre-fetching reservation times. The system delivers an [`INGetAvailableRestaurantReservationBookingDefaultsIntent`](./ingetavailablerestaurantreservationbookingdefaultsintent.md) object to your handler before it asks your Intents extension for any initial reservation times. Use this intent object to provide a set of reasonable default values that are likely to yield good results when doing an initial search for available reservation times. For example, the default date provided by your handler should represent a date and time when the restaurant is open and has available tables.

Maps does not require you to resolve or confirm the contents of a get available restaurant reservation booking defaults intent before handling it. User interactions drive the selection of data in Maps, ensuring that the data Maps places into an intent object is already valid.

## Topics

### Resolving the Intent Parameters
- [func resolveRestaurant(for: INGetAvailableRestaurantReservationBookingDefaultsIntent, completion: (INRestaurantResolutionResult) -> Void)](./ingetavailablerestaurantreservationbookingdefaultsintenthandling/resolverestaurant%28for,completion%29.md)
  Resolves the restaurant for which you are providing default values.
### Confirming the Response
- [func confirm(getAvailableRestaurantReservationBookingDefaults: INGetAvailableRestaurantReservationBookingDefaultsIntent, completion: (INGetAvailableRestaurantReservationBookingDefaultsIntentResponse) -> Void)](./ingetavailablerestaurantreservationbookingdefaultsintenthandling/confirm%28getavailablerestaurantreservationbookingdefaults,completion%29.md)
  Confirms whether you can return default values.
### Handling the Intent
- [func handle(getAvailableRestaurantReservationBookingDefaults: INGetAvailableRestaurantReservationBookingDefaultsIntent, completion: (INGetAvailableRestaurantReservationBookingDefaultsIntentResponse) -> Void)](./ingetavailablerestaurantreservationbookingdefaultsintenthandling/handle%28getavailablerestaurantreservationbookingdefaults,completion%29.md)
  Handles returning the default values to use when pre-fetching reservations.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Get Available Restaurant Reservation Booking Defaults
- [class INGetAvailableRestaurantReservationBookingDefaultsIntent](./ingetavailablerestaurantreservationbookingdefaultsintent.md)
  A request for the default values to use when fetching potential reservation options.
- [class INGetAvailableRestaurantReservationBookingDefaultsIntentResponse](./ingetavailablerestaurantreservationbookingdefaultsintentresponse.md)
  Your app’s response to a get available restaurant reservation booking defaults intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingdefaultsintenthandling)*