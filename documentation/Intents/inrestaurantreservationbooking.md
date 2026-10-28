# INRestaurantReservationBooking

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A potential reservation that a user can book.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class INRestaurantReservationBooking
```

```objc
@interface INRestaurantReservationBooking : NSObject
```

## Overview

An [`INRestaurantReservationBooking`](./inrestaurantreservationbooking.md) object contains information about a potential unbooked reservation. When handling a [`INGetAvailableRestaurantReservationBookingsIntent`](./ingetavailablerestaurantreservationbookingsintent.md) object, create instances of this class for each time slot that you want to offer to the user. The system presents this information to the user, allowing them to choose which time slot they prefer. Each reservation booking contains details about the restaurant, date, and party size. They also contain information about special offers and any requirements needed to complete the reservation.

The creation of an [`INRestaurantReservationBooking`](./inrestaurantreservationbooking.md) object does not constitute the booking of the associated reservation. When the user selects a particular time slot, the system sends a [`INBookRestaurantReservationIntent`](./inbookrestaurantreservationintent.md) object to your Intents extension with the selected reservation booking object. At that time, you use the reservation booking object to complete the reservation process.

## Topics

### Initializing the Reservation Booking Object
- [init(restaurant: INRestaurant, booking: Date, partySize: Int, bookingIdentifier: String)](./inrestaurantreservationbooking/init%28restaurant,booking,partysize,bookingidentifier%29.md)
  Initializes the reservation object with the specified information and status.
### Accessing the Reservation Information
- [var restaurant: INRestaurant](./inrestaurantreservationbooking/restaurant.md)
  The restaurant associated with the reservation.
- [var partySize: Int](./inrestaurantreservationbooking/partysize.md)
  The total number of guests in the party.
- [var offers: [INRestaurantOffer]?](./inrestaurantreservationbooking/offers.md)
  An array of special offers from the restaurant.
### Accessing the Booking Information
- [var bookingIdentifier: String](./inrestaurantreservationbooking/bookingidentifier.md)
  The unique identifier associated with this reservation.
- [var isBookingAvailable: Bool](./inrestaurantreservationbooking/isbookingavailable.md)
  A Boolean value indicating whether the time slot is available for booking.
- [var bookingDate: Date](./inrestaurantreservationbooking/bookingdate.md)
  The date and time of the reservation.
- [var bookingDescription: String?](./inrestaurantreservationbooking/bookingdescription.md)
  An optional description of the booking.
### Configuring the Required Information
- [var requiresName: Bool](./inrestaurantreservationbooking/requiresname.md)
  A Boolean indicating whether the reservation requires a guest name before booking.
- [var requiresEmailAddress: Bool](./inrestaurantreservationbooking/requiresemailaddress.md)
  A Boolean indicating whether the reservation requires an email address before it booking.
- [var requiresPhoneNumber: Bool](./inrestaurantreservationbooking/requiresphonenumber.md)
  A Boolean indicating whether the reservation requires a phone number before booking.
- [var requiresManualRequest: Bool](./inrestaurantreservationbooking/requiresmanualrequest.md)
  A Boolean indicating whether the reservation requires manually contacting the restaurant to confirm the details.
### Initializers
- [init?(coder: NSCoder)](./inrestaurantreservationbooking/init%28coder%29.md)
- [init(restaurant: INRestaurant, bookingDate: Date, partySize: Int, bookingIdentifier: String)](./inrestaurantreservationbooking/init%28restaurant,bookingdate,partysize,bookingidentifier%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [INRestaurantReservationUserBooking](./inrestaurantreservationuserbooking.md)
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
- [class INRestaurantReservationUserBooking](./inrestaurantreservationuserbooking.md)
  A reservation created by a user.
- [class INTermsAndConditions](./intermsandconditions.md)
  The terms and conditions of service when making restaurant reservations.
- [enum INRestaurantReservationUserBookingStatus](./inrestaurantreservationuserbookingstatus.md)
  Constants indicating the status of a user reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantreservationbooking)*