# INGetAvailableRestaurantReservationBookingsIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a get available restaurant reservation bookings intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class INGetAvailableRestaurantReservationBookingsIntentResponse
```

```objc
@interface INGetAvailableRestaurantReservationBookingsIntentResponse : INIntentResponse
```

## Overview

An [`INGetAvailableRestaurantReservationBookingsIntentResponse`](./ingetavailablerestaurantreservationbookingsintentresponse.md) object contains the reservation booking objects that represent the time slots available for making a reservation at the given restaurant. You create an instance of this class when confirming or handling an [`INGetAvailableRestaurantReservationBookingsIntent`](./ingetavailablerestaurantreservationbookingsintent.md) object, which contains the basic details you use to determine your response.

You create an [`INGetAvailableRestaurantReservationBookingsIntentResponse`](./ingetavailablerestaurantreservationbookingsintentresponse.md) object in the [`confirm(getAvailableRestaurantReservationBookings:completion:)`](./ingetavailablerestaurantreservationbookingsintenthandling/confirm%28getavailablerestaurantreservationbookings,completion%29.md) and [`handle(getAvailableRestaurantReservationBookings:completion:)`](./ingetavailablerestaurantreservationbookingsintenthandling/handle%28getavailablerestaurantreservationbookings,completion%29.md) methods of your handler object. For more information about implementing your handler object, see [`INGetAvailableRestaurantReservationBookingsIntentHandling`](./ingetavailablerestaurantreservationbookingsintenthandling.md).

## Topics

### Initializing the Response Object
- [init(availableBookings: [INRestaurantReservationBooking], code: INGetAvailableRestaurantReservationBookingsIntentCode, userActivity: NSUserActivity?)](./ingetavailablerestaurantreservationbookingsintentresponse/init%28availablebookings,code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Specifying the Reservation Results
- [var availableBookings: [INRestaurantReservationBooking]](./ingetavailablerestaurantreservationbookingsintentresponse/availablebookings.md)
  An array of available time slots for the reservation.
### Specifying Additional Information
- [var localizedRestaurantDescriptionText: String?](./ingetavailablerestaurantreservationbookingsintentresponse/localizedrestaurantdescriptiontext.md)
  A localized, user-readable string containing a description of the restaurant.
- [var localizedBookingAdvisementText: String?](./ingetavailablerestaurantreservationbookingsintentresponse/localizedbookingadvisementtext.md)
  A localized, user-readable string containing policies and information related to the reservation.
- [var termsAndConditions: INTermsAndConditions?](./ingetavailablerestaurantreservationbookingsintentresponse/termsandconditions.md)
  The terms and conditions of using your company’s services.
### Getting the Response Code
- [var code: INGetAvailableRestaurantReservationBookingsIntentCode](./ingetavailablerestaurantreservationbookingsintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INGetAvailableRestaurantReservationBookingsIntentCode](./ingetavailablerestaurantreservationbookingsintentcode.md)
  Constants indicating the state of the response.

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

### Get Available Restaurant Reservation Bookings
- [protocol INGetAvailableRestaurantReservationBookingsIntentHandling](./ingetavailablerestaurantreservationbookingsintenthandling.md)
  The handler interface for generating a list of potential reservation times from which the user can select.
- [class INGetAvailableRestaurantReservationBookingsIntent](./ingetavailablerestaurantreservationbookingsintent.md)
  A request for the time slots available for making a reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingsintentresponse)*