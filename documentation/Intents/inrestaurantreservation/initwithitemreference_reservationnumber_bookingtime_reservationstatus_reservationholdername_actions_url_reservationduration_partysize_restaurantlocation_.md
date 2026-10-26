# initWithItemReference:reservationNumber:bookingTime:reservationStatus:reservationHolderName:actions:URL:reservationDuration:partySize:restaurantLocation:

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Creates a restaurant reservation with the provided information.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```objc
- (instancetype) initWithItemReference:(INSpeakableString *) itemReference reservationNumber:(NSString *) reservationNumber bookingTime:(NSDate *) bookingTime reservationStatus:(INReservationStatus) reservationStatus reservationHolderName:(NSString *) reservationHolderName actions:(NSArray<INReservationAction *> *) actions URL:(NSURL *) URL reservationDuration:(INDateComponentsRange *) reservationDuration partySize:(NSNumber *) partySize restaurantLocation:(CLPlacemark *) restaurantLocation;
```

#### Return Value

A new [`INRestaurantReservation`](../inrestaurantreservation.md) object or `nil` if unable to create one.

## Parameters

- `itemReference`: A unique identifier for the reservation.
- `reservationNumber`: The reservation number.
- `bookingTime`: The date and time the user made the reservation.
- `reservationStatus`: The current status of the reservation.
- `reservationHolderName`: The reservation holder’s name.
- `actions`: Available actions associated with the reservation, such as checking in when the user arrives at the restaurant.
- `URL`: A webpage containing reservation information.
- `reservationDuration`: The date and time range that defines the start and end times for the restaurant reservation.
- `partySize`: The size of the party for the reservation.
- `restaurantLocation`: The name and location of the restaurant.

## See Also

### Creating a Restaurant Reservation
- [- initWithItemReference:reservationNumber:bookingTime:reservationStatus:reservationHolderName:actions:reservationDuration:partySize:restaurantLocation:](./initwithitemreference_reservationnumber_bookingtime_reservationstatus_reservationholdername_actions_reservationduration_partysize_restaurantlocation_.md)
  Creates a new restaurant reservation with the provided information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantreservation/initwithitemreference:reservationnumber:bookingtime:reservationstatus:reservationholdername:actions:url:reservationduration:partysize:restaurantlocation:)*