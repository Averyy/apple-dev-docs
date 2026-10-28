# INRestaurantGuest

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The person assigned to a reservation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class INRestaurantGuest
```

```objc
@interface INRestaurantGuest : INPerson
```

## Overview

An [`INRestaurantGuest`](./inrestaurantguest.md) object identifies the user assigned to a reservation and includes contact information used to communicate changes or updates to the reservation. During the creation of a reservation, the system sends a [`INGetRestaurantGuestIntent`](./ingetrestaurantguestintent.md) intent to your Intents extension and asks it to provide the identity of the guest to assign to the reservation. You create an instance of this class and associate it with your response to that intent.

Depending on the preferences you return to the system about how to display guest information, the user might have the option of changing the name and contact info assigned to a reservation. When that happens, the system may return a new instance of this class during the final booking stages of the reservation with the revised guest information.

## Topics

### Initializing a Restaurant Guest
- [init(nameComponents: PersonNameComponents?, phoneNumber: String?, emailAddress: String?)](./inrestaurantguest/init%28namecomponents,phonenumber,emailaddress%29.md)
  Initializes the object with the specified name and contact information for the user.
### Accessing the Guest Information
- [var phoneNumber: String?](./inrestaurantguest/phonenumber.md)
  The phone number to use when contacting the user about reservations.
- [var emailAddress: String?](./inrestaurantguest/emailaddress.md)
  The email address to use when contacting the user about reservations.

## Relationships

### Inherits From
- [INPerson](./inperson.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [INSpeakable](./inspeakable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Data Objects
- [class INRestaurant](./inrestaurant.md)
  A restaurant for which your app can make and manage reservations.
- [class INRestaurantGuestDisplayPreferences](./inrestaurantguestdisplaypreferences.md)
  Options about how to display guest information from system interfaces.
- [class INRestaurantOffer](./inrestaurantoffer.md)
  Information about special offers made by a restaurant.
- [class INRestaurantReservationBooking](./inrestaurantreservationbooking.md)
  A potential reservation that a user can book.
- [class INRestaurantReservationUserBooking](./inrestaurantreservationuserbooking.md)
  A reservation created by a user.
- [class INTermsAndConditions](./intermsandconditions.md)
  The terms and conditions of service when making restaurant reservations.
- [enum INRestaurantReservationUserBookingStatus](./inrestaurantreservationuserbookingstatus.md)
  Constants indicating the status of a user reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantguest)*