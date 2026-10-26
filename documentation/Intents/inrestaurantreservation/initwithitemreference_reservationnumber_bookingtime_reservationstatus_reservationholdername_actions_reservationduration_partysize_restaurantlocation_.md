# initWithItemReference:reservationNumber:bookingTime:reservationStatus:reservationHolderName:actions:reservationDuration:partySize:restaurantLocation:

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Creates a new restaurant reservation with the provided information.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```objc
- (instancetype) initWithItemReference:(INSpeakableString *) itemReference reservationNumber:(NSString *) reservationNumber bookingTime:(NSDate *) bookingTime reservationStatus:(INReservationStatus) reservationStatus reservationHolderName:(NSString *) reservationHolderName actions:(NSArray<INReservationAction *> *) actions reservationDuration:(INDateComponentsRange *) reservationDuration partySize:(NSNumber *) partySize restaurantLocation:(CLPlacemark *) restaurantLocation;
```

#### Return Value

A new [`INRestaurantReservation`](../inrestaurantreservation.md) object or `nil` if unable to create one.

## Parameters

- `itemReference`: A unique value for the reservation item.
- `reservationNumber`: The reservation or booking number provided by the app.
- `bookingTime`: The date and time the user made the reservation.
- `reservationStatus`: The current status of the reservation.
- `reservationHolderName`: The name of the person the reservation is under.
- `actions`: The available actions for the reservation. For example, checking in for the reservation from your phone.
- `reservationDuration`: The date and time range that defines the start and end times for the restaurant reservation.
- `partySize`: The size of the party for the reservation.
- `restaurantLocation`: The name and location of the restaurant.

## See Also

### Creating a Restaurant Reservation
- [- initWithItemReference:reservationNumber:bookingTime:reservationStatus:reservationHolderName:actions:URL:reservationDuration:partySize:restaurantLocation:](./initwithitemreference_reservationnumber_bookingtime_reservationstatus_reservationholdername_actions_url_reservationduration_partysize_restaurantlocation_.md)
  Creates a restaurant reservation with the provided information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantreservation/initwithitemreference:reservationnumber:bookingtime:reservationstatus:reservationholdername:actions:reservationduration:partysize:restaurantlocation:)*