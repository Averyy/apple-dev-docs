# INRestaurant

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A restaurant for which your app can make and manage reservations.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class INRestaurant
```

```objc
@interface INRestaurant : NSObject
```

## Overview

An [`INRestaurant`](./inrestaurant.md) object contains identifying information for a restaurant. You must work with Apple to integrate your restaurant-specific information into the back-end database. Later, when the user selects a restaurant and tries to book a reservation, Apple packages the information you provided into a restaurant object and delivers it to your Intents extension. You use that information to look up the restaurant on your own server and retrieve any necessary information about it.

## Topics

### Initializing a Restaurant Object
- [init(location: CLLocation, name: String, vendorIdentifier: String, restaurantIdentifier: String)](./inrestaurant/init%28location,name,vendoridentifier,restaurantidentifier%29.md)
  Initializes a restaurant object with some identifying information.
### Accessing the Restaurant Information
- [var name: String](./inrestaurant/name.md)
  The name of the restaurant.
- [var location: CLLocation](./inrestaurant/location.md)
  The location of the restaurant.
- [var restaurantIdentifier: String](./inrestaurant/restaurantidentifier.md)
  A unique identifier for the restaurant.
- [var vendorIdentifier: String](./inrestaurant/vendoridentifier.md)
  The provider of the restaurant data.
### Initializers
- [init?(coder: NSCoder)](./inrestaurant/init%28coder%29.md)

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
- [class INRestaurantGuest](./inrestaurantguest.md)
  The person assigned to a reservation.
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

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurant)*