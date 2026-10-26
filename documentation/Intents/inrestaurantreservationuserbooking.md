# INRestaurantReservationUserBooking

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A reservation created by a user.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class INRestaurantReservationUserBooking
```

```objc
@interface INRestaurantReservationUserBooking : INRestaurantReservationBooking
```

#### Overview

An [`INRestaurantReservationUserBooking`](./inrestaurantreservationuserbooking.md) object contains information about a reservation placed by a user. When the user actually books a reservation at a restaurant, you create an instance of this class to represent the reservation details. This object contains the specific details of the reservation, including any user-specified information such as selected offers or special requests.

You create instances of this class when providing responses to [`INBookRestaurantReservationIntent`](./inbookrestaurantreservationintent.md) or [`INGetUserCurrentRestaurantReservationBookingsIntent`](./ingetusercurrentrestaurantreservationbookingsintent.md) objects. After initializing an instance of this class with basic information, fill in any additional properties with details relevant to the reservation before returning it with your response.

For information about additional properties of this class that you can configure for a booking, see [`INRestaurantReservationBooking`](./inrestaurantreservationbooking.md).

## Topics

### Initializing a Reservation
- [init(restaurant: INRestaurant, booking: Date, partySize: Int, bookingIdentifier: String, guest: INRestaurantGuest, status: INRestaurantReservationUserBookingStatus, dateStatusModified: Date)](./inrestaurantreservationuserbooking/init%28restaurant,booking,partysize,bookingidentifier,guest,status,datestatusmodified%29.md)
  Initializes the reservation object with the specified information and status.
### Accessing the Reservation Information
- [var guest: INRestaurantGuest](./inrestaurantreservationuserbooking/guest.md)
  The guest associated with the reservation.
- [var status: INRestaurantReservationUserBookingStatus](./inrestaurantreservationuserbooking/status.md)
  The current status of the reservation.
- [var dateStatusModified: Date](./inrestaurantreservationuserbooking/datestatusmodified.md)
  The date on which the status of the reservation changed.
- [var guestProvidedSpecialRequestText: String?](./inrestaurantreservationuserbooking/guestprovidedspecialrequesttext.md)
  Any special requests made by the user with the reservation.
### Accessing Special Offers
- [var selectedOffer: INRestaurantOffer?](./inrestaurantreservationuserbooking/selectedoffer.md)
  The offer selected by the user.
- [var advisementText: String?](./inrestaurantreservationuserbooking/advisementtext.md)
  A user-readable string containing policies and information related to the reservation.
### Constants
- [enum INRestaurantReservationUserBookingStatus](./inrestaurantreservationuserbookingstatus.md)
  Constants indicating the status of a user reservation.
### Initializers
- [init(restaurant: INRestaurant, bookingDate: Date, partySize: Int, bookingIdentifier: String, guest: INRestaurantGuest, status: INRestaurantReservationUserBookingStatus, dateStatusModified: Date)](./inrestaurantreservationuserbooking/init%28restaurant,bookingdate,partysize,bookingidentifier,guest,status,datestatusmodified%29.md)

## Relationships

### Inherits From
- [INRestaurantReservationBooking](./inrestaurantreservationbooking.md)
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

### Data Objects
- [class INRestaurant](./inrestaurant.md)
  A restaurant for which your app can make and manage reservations.
- [class INRestaurantGuest](./inrestaurantguest.md)
  The person assigned to a reservation.
- [class INRestaurantGuestDisplayPreferences](./inrestaurantguestdisplaypreferences.md)
  Options about how to display guest information from system interfaces.
- [class INRestaurantOffer](./inrestaurantoffer.md)
  Information about special offers made by a restaurant.
- [class INRestaurantReservationBooking](./inrestaurantreservationbooking.md)
  A potential reservation that a user can book.
- [class INTermsAndConditions](./intermsandconditions.md)
  The terms and conditions of service when making restaurant reservations.
- [enum INRestaurantReservationUserBookingStatus](./inrestaurantreservationuserbookingstatus.md)
  Constants indicating the status of a user reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantreservationuserbooking)*