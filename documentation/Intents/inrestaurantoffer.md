# INRestaurantOffer

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Information about special offers made by a restaurant.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class INRestaurantOffer
```

```objc
@interface INRestaurantOffer : NSObject
```

## Overview

An [`INRestaurantOffer`](./inrestaurantoffer.md) object provides information about a special offer made by a restaurant. Restaurants might offer special pricing as part of a promotion or advertisement. This object captures the details of an offer, which the system then displays to the user during the reservation selection process. When booking the reservation, you include the offer selected by the user with the information you provide to the restaurant.

When creating a response to a [`INGetAvailableRestaurantReservationBookingsIntent`](./ingetavailablerestaurantreservationbookingsintent.md) intent, you create [`INRestaurantReservationBooking`](./inrestaurantreservationbooking.md) objects with information about the time slots available to the user. If a restaurant offers special deals in a given time slot, create one or more instances of this class, populate them with the details of the offers, and assign them to the corresponding [`INRestaurantReservationBooking`](./inrestaurantreservationbooking.md) objects.

You are responsible for obtaining the information about special offers from the restaurants you support. Including special offers with reservations is not required.

## Topics

### Accessing the Offer Details
- [var offerTitleText: String](./inrestaurantoffer/offertitletext.md)
  The user-readable text that summarizes the offer.
- [var offerDetailText: String](./inrestaurantoffer/offerdetailtext.md)
  The user-readable text containing the details of the offer.
- [var offerIdentifier: String](./inrestaurantoffer/offeridentifier.md)
  The unique identifier associated with the offer.
### Initializers
- [init?(coder: NSCoder)](./inrestaurantoffer/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
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
- [class INRestaurantReservationBooking](./inrestaurantreservationbooking.md)
  A potential reservation that a user can book.
- [class INRestaurantReservationUserBooking](./inrestaurantreservationuserbooking.md)
  A reservation created by a user.
- [class INTermsAndConditions](./intermsandconditions.md)
  The terms and conditions of service when making restaurant reservations.
- [enum INRestaurantReservationUserBookingStatus](./inrestaurantreservationuserbookingstatus.md)
  Constants indicating the status of a user reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantoffer)*