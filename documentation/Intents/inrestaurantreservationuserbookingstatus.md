# INRestaurantReservationUserBookingStatus

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the status of a user reservation.

## Declaration

```swift
enum INRestaurantReservationUserBookingStatus
```

```c
enum INRestaurantReservationUserBookingStatus : NSUInteger;
```

## Topics

### Constants
- [INRestaurantReservationUserBookingStatus.pending](./inrestaurantreservationuserbookingstatus/pending.md)
  The restaurant hasn’t confirmed or denied the reservation.
- [INRestaurantReservationUserBookingStatus.confirmed](./inrestaurantreservationuserbookingstatus/confirmed.md)
  The restaurant accepted the reservation.
- [INRestaurantReservationUserBookingStatus.denied](./inrestaurantreservationuserbookingstatus/denied.md)
  The restaurant declined the reservation.
### Initializers
- [init?(rawValue: UInt)](./inrestaurantreservationuserbookingstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

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
- [class INTermsAndConditions](./intermsandconditions.md)
  The terms and conditions of service when making restaurant reservations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantreservationuserbookingstatus)*