# INGetUserCurrentRestaurantReservationBookingsIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request for the list of the user’s current reservations.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class INGetUserCurrentRestaurantReservationBookingsIntent
```

```objc
@interface INGetUserCurrentRestaurantReservationBookingsIntent : INIntent
```

#### Overview

An [`INGetUserCurrentRestaurantReservationBookingsIntent`](./ingetusercurrentrestaurantreservationbookingsintent.md) object asks you to retrieve the current restaurant reservations associated with the user. Maps sends this intent to your Intents extension when it needs information about all of the user’s current reservations, or when it needs information about one or more specific reservations. Use the properties of this object to determine which reservations to return.

When searching for reservations, use the [`reservationIdentifier`](./ingetusercurrentrestaurantreservationbookingsintent/reservationidentifier.md) properties to fetch only the specified reservation, or use the [`restaurant`](./ingetusercurrentrestaurantreservationbookingsintent/restaurant.md) property to fetch pending reservations only at the specified restaurant. If both of those properties are `nil`, retrieve all of the user’s currently pending reservations. After fetching the appropriate set of reservations, use the [`maximumNumberOfResults`](./ingetusercurrentrestaurantreservationbookingsintent/maximumnumberofresults.md) and [`earliestBookingDateForResults`](./ingetusercurrentrestaurantreservationbookingsintent/earliestbookingdateforresults.md) properties to limit the set of results you return as part of your response.

To handle this intent, the handler object in your Intents extension must adopt the [`INGetUserCurrentRestaurantReservationBookingsIntentHandling`](./ingetusercurrentrestaurantreservationbookingsintenthandling.md) protocol. Your handler should resolve and confirm any parameters and create an [`INGetUserCurrentRestaurantReservationBookingsIntentResponse`](./ingetusercurrentrestaurantreservationbookingsintentresponse.md) object using the found results.

##### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Maps |
| Always requires unlocked device | Yes |

## Topics

### Initializing the Intent Object
- [init(restaurant: INRestaurant?, reservationIdentifier: String?, maximumNumberOfResults: NSNumber?, earliestBookingDateForResults: Date?)](./ingetusercurrentrestaurantreservationbookingsintent/init%28restaurant,reservationidentifier,maximumnumberofresults,earliestbookingdateforresults%29.md)
  Initializes the intent object with the specified reservation information.
### Getting the Search Parameters
- [var restaurant: INRestaurant?](./ingetusercurrentrestaurantreservationbookingsintent/restaurant.md)
  A restaurant to use as a filter when searching for reservations.
- [var reservationIdentifier: String?](./ingetusercurrentrestaurantreservationbookingsintent/reservationidentifier.md)
  An identifier to use when searching for the user’s reservations.
### Getting the Result Limits
- [var maximumNumberOfResults: NSNumber?](./ingetusercurrentrestaurantreservationbookingsintent/maximumnumberofresults.md)
  The maximum number of reservations to include in your response object.
- [var earliestBookingDateForResults: Date?](./ingetusercurrentrestaurantreservationbookingsintent/earliestbookingdateforresults.md)
  The earliest date to associate with any reservations.

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

### Get User Current Restaurant Reservation Bookings
- [protocol INGetUserCurrentRestaurantReservationBookingsIntentHandling](./ingetusercurrentrestaurantreservationbookingsintenthandling.md)
  The handler interface for fetching and delivering the user’s current reservations.
- [class INGetUserCurrentRestaurantReservationBookingsIntentResponse](./ingetusercurrentrestaurantreservationbookingsintentresponse.md)
  Your app’s response to a get user current restaurant reservation bookings intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetusercurrentrestaurantreservationbookingsintent)*