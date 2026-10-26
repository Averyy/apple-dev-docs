# INTermsAndConditions

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The terms and conditions of service when making restaurant reservations.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class INTermsAndConditions
```

```objc
@interface INTermsAndConditions : NSObject
```

#### Overview

An [`INTermsAndConditions`](./intermsandconditions.md) object contains information about the terms and conditions that your company applies to users when handling restaurant reservations. Use this object to communicate the details of your company’s policies. The system presents your terms and conditions to the user through the built-in reservation interfaces. You create instances of this class when providing a response to a [`INGetAvailableRestaurantReservationBookingsIntent`](./ingetavailablerestaurantreservationbookingsintent.md) object.

## Topics

### Initializing the Terms and Conditions Object
- [init(localizedTermsAndConditionsText: String, privacyPolicyURL: URL?, termsAndConditionsURL: URL?)](./intermsandconditions/init%28localizedtermsandconditionstext,privacypolicyurl,termsandconditionsurl%29.md)
  Initializes the terms and conditions object with the specified information.
### Getting the Terms and Conditions
- [var localizedTermsAndConditionsText: String](./intermsandconditions/localizedtermsandconditionstext.md)
  A localized, user-readable string that summarizes the terms and conditions of your company’s services.
- [var privacyPolicyURL: URL?](./intermsandconditions/privacypolicyurl.md)
  The URL to your company’s privacy policy web page.
- [var termsAndConditionsURL: URL?](./intermsandconditions/termsandconditionsurl.md)
  The URL to your company’s terms and conditions web page.
### Initializers
- [init?(coder: NSCoder)](./intermsandconditions/init%28coder%29.md)

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
- [class INRestaurantOffer](./inrestaurantoffer.md)
  Information about special offers made by a restaurant.
- [class INRestaurantReservationBooking](./inrestaurantreservationbooking.md)
  A potential reservation that a user can book.
- [class INRestaurantReservationUserBooking](./inrestaurantreservationuserbooking.md)
  A reservation created by a user.
- [enum INRestaurantReservationUserBookingStatus](./inrestaurantreservationuserbookingstatus.md)
  Constants indicating the status of a user reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intermsandconditions)*