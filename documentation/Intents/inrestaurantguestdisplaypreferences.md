# INRestaurantGuestDisplayPreferences

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Options about how to display guest information from system interfaces.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class INRestaurantGuestDisplayPreferences
```

```objc
@interface INRestaurantGuestDisplayPreferences : NSObject
```

#### Overview

An [`INRestaurantGuestDisplayPreferences`](./inrestaurantguestdisplaypreferences.md) object contains configuration options used by any reservation-related interfaces that present guest information. Create an instance of this class and assign it to the [`guestDisplayPreferences`](./ingetrestaurantguestintentresponse/guestdisplaypreferences.md) property of your [`INGetRestaurantGuestIntentResponse`](./ingetrestaurantguestintentresponse.md) object when handling a request for information about the person making a reservation. Use the properties of this class to specify what information you want displayed for a user and whether you can change that information prior to completing a reservation.

## Topics

### Specifying Which Fields to Display
- [var nameFieldShouldBeDisplayed: Bool](./inrestaurantguestdisplaypreferences/namefieldshouldbedisplayed.md)
  A Boolean value indicating whether to display the guest’s name should.
- [var phoneNumberFieldShouldBeDisplayed: Bool](./inrestaurantguestdisplaypreferences/phonenumberfieldshouldbedisplayed.md)
  A Boolean value indicating whether to display the guest’s phone number.
- [var emailAddressFieldShouldBeDisplayed: Bool](./inrestaurantguestdisplaypreferences/emailaddressfieldshouldbedisplayed.md)
  A Boolean value indicating whether to display the guest’s email address.
### Specifying Required Fields
- [var nameFieldFirstNameOptional: Bool](./inrestaurantguestdisplaypreferences/namefieldfirstnameoptional.md)
  A Boolean value indicating whether the reservation requires the guest’s first name.
- [var nameFieldLastNameOptional: Bool](./inrestaurantguestdisplaypreferences/namefieldlastnameoptional.md)
  A Boolean value indicating whether the reservation requires the guest’s last name.
### Making the Guest Information Editable
- [var nameEditable: Bool](./inrestaurantguestdisplaypreferences/nameeditable.md)
  A Boolean value indicating whether the name fields are editable.
- [var emailAddressEditable: Bool](./inrestaurantguestdisplaypreferences/emailaddresseditable.md)
  A Boolean value indicating whether the email address field is editable.
- [var phoneNumberEditable: Bool](./inrestaurantguestdisplaypreferences/phonenumbereditable.md)
  A Boolean value indicating whether the phone number field is editable.
### Initializers
- [init?(coder: NSCoder)](./inrestaurantguestdisplaypreferences/init%28coder%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantguestdisplaypreferences)*