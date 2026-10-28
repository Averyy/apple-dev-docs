# INGetUserCurrentRestaurantReservationBookingsIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a get user current restaurant reservation bookings intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class INGetUserCurrentRestaurantReservationBookingsIntentResponse
```

```objc
@interface INGetUserCurrentRestaurantReservationBookingsIntentResponse : INIntentResponse
```

## Overview

An [`INGetUserCurrentRestaurantReservationBookingsIntentResponse`](./ingetusercurrentrestaurantreservationbookingsintentresponse.md) object contains the current reservations associated with the user and matching the search criteria in the corresponding [`INGetUserCurrentRestaurantReservationBookingsIntent`](./ingetusercurrentrestaurantreservationbookingsintent.md) object. You create instances of this class when confirming or handling an intent object of that type.

You create an [`INGetUserCurrentRestaurantReservationBookingsIntentResponse`](./ingetusercurrentrestaurantreservationbookingsintentresponse.md) object in the [`confirm(getUserCurrentRestaurantReservationBookings:completion:)`](./ingetusercurrentrestaurantreservationbookingsintenthandling/confirm%28getusercurrentrestaurantreservationbookings,completion%29.md) and [`handle(getUserCurrentRestaurantReservationBookings:completion:)`](./ingetusercurrentrestaurantreservationbookingsintenthandling/handle%28getusercurrentrestaurantreservationbookings,completion%29.md) methods of your handler object. For more information about implementing your handler object, see [`INGetUserCurrentRestaurantReservationBookingsIntentHandling`](./ingetusercurrentrestaurantreservationbookingsintenthandling.md).

## Topics

### Initializing the Response Object
- [init(userCurrentBookings: [INRestaurantReservationUserBooking], code: INGetUserCurrentRestaurantReservationBookingsIntentResponseCode, userActivity: NSUserActivity?)](./ingetusercurrentrestaurantreservationbookingsintentresponse/init%28usercurrentbookings,code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INGetUserCurrentRestaurantReservationBookingsIntentResponseCode](./ingetusercurrentrestaurantreservationbookingsintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INGetUserCurrentRestaurantReservationBookingsIntentResponseCode](./ingetusercurrentrestaurantreservationbookingsintentresponsecode.md)
  Constants indicating the state of the response.
### Specifying the User’s Current Reservations
- [var userCurrentBookings: [INRestaurantReservationUserBooking]](./ingetusercurrentrestaurantreservationbookingsintentresponse/usercurrentbookings.md)
  An array of the user’s current reservations.

## Relationships

### Inherits From
- [INIntentResponse](./inintentresponse.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Get User Current Restaurant Reservation Bookings
- [protocol INGetUserCurrentRestaurantReservationBookingsIntentHandling](./ingetusercurrentrestaurantreservationbookingsintenthandling.md)
  The handler interface for fetching and delivering the user’s current reservations.
- [class INGetUserCurrentRestaurantReservationBookingsIntent](./ingetusercurrentrestaurantreservationbookingsintent.md)
  A request for the list of the user’s current reservations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetusercurrentrestaurantreservationbookingsintentresponse)*