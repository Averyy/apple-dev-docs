# INGetAvailableRestaurantReservationBookingsIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request for the time slots available for making a reservation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class INGetAvailableRestaurantReservationBookingsIntent
```

```objc
@interface INGetAvailableRestaurantReservationBookingsIntent : INIntent
```

## Overview

An [`INGetAvailableRestaurantReservationBookingsIntent`](./ingetavailablerestaurantreservationbookingsintent.md) object asks you to generate details regarding the available time slots offered by a restaurant for a given party size. Maps sends this intent to your Intents extension when the user begins the booking process. You use this intent to obtain the initial details about the reservation request, including the number of people and the preferred date for the reservation. You use those details to identify potential time slots that can accommodate the party and return those time slots in your response object.

To handle this intent, the handler object in your Intents extension must adopt the [`INGetAvailableRestaurantReservationBookingsIntentHandling`](./ingetavailablerestaurantreservationbookingsintenthandling.md) protocol. Your handler should resolve and confirm any parameters and create an [`INGetAvailableRestaurantReservationBookingsIntentResponse`](./ingetavailablerestaurantreservationbookingsintentresponse.md) object with the list of potential time slots.

### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Maps |
| Always requires unlocked device | Yes |

## Topics

### Initializing the Intent Object
- [init(restaurant: INRestaurant, partySize: Int, preferredBooking: DateComponents?, maximumNumberOfResults: NSNumber?, earliestBookingDateForResults: Date?, latestBookingDateForResults: Date?)](./ingetavailablerestaurantreservationbookingsintent/init%28restaurant,partysize,preferredbooking,maximumnumberofresults,earliestbookingdateforresults,latestbookingdateforresults%29.md)
  Initializes the intent object with the specified reservation information.
### Getting the Restaurant
- [var restaurant: INRestaurant](./ingetavailablerestaurantreservationbookingsintent/restaurant.md)
  The restaurant associated with the reservation.
### Getting the Reservation Details
- [var partySize: Int](./ingetavailablerestaurantreservationbookingsintent/partysize.md)
  The number of people in the guest’s party.
- [var preferredBookingDateComponents: DateComponents?](./ingetavailablerestaurantreservationbookingsintent/preferredbookingdatecomponents.md)
  The date and time preferred by the user for the reservation.
### Getting the Time Slot Constraints
- [var earliestBookingDateForResults: Date?](./ingetavailablerestaurantreservationbookingsintent/earliestbookingdateforresults.md)
  The earliest date for which to return results.
- [var latestBookingDateForResults: Date?](./ingetavailablerestaurantreservationbookingsintent/latestbookingdateforresults.md)
  The latest date for which to return results.
- [var maximumNumberOfResults: NSNumber?](./ingetavailablerestaurantreservationbookingsintent/maximumnumberofresults.md)
  The maximum number of reservation results to return.
### Initializers
- [init(restaurant: INRestaurant, partySize: Int, preferredBookingDateComponents: DateComponents?, maximumNumberOfResults: NSNumber?, earliestBookingDateForResults: Date?, latestBookingDateForResults: Date?)](./ingetavailablerestaurantreservationbookingsintent/init%28restaurant,partysize,preferredbookingdatecomponents,maximumnumberofresults,earliestbookingdateforresults,latestbookingdateforresults%29.md)

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

### Get Available Restaurant Reservation Bookings
- [protocol INGetAvailableRestaurantReservationBookingsIntentHandling](./ingetavailablerestaurantreservationbookingsintenthandling.md)
  The handler interface for generating a list of potential reservation times from which the user can select.
- [class INGetAvailableRestaurantReservationBookingsIntentResponse](./ingetavailablerestaurantreservationbookingsintentresponse.md)
  Your app’s response to a get available restaurant reservation bookings intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingsintent)*