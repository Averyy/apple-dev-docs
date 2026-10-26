# initWithItemReference:reservationNumber:bookingTime:reservationStatus:reservationHolderName:actions:lodgingBusinessLocation:reservationDuration:numberOfAdults:numberOfChildren:

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Creates a new lodging reservation with the provided information.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```objc
- (instancetype) initWithItemReference:(INSpeakableString *) itemReference reservationNumber:(NSString *) reservationNumber bookingTime:(NSDate *) bookingTime reservationStatus:(INReservationStatus) reservationStatus reservationHolderName:(NSString *) reservationHolderName actions:(NSArray<INReservationAction *> *) actions lodgingBusinessLocation:(CLPlacemark *) lodgingBusinessLocation reservationDuration:(INDateComponentsRange *) reservationDuration numberOfAdults:(NSNumber *) numberOfAdults numberOfChildren:(NSNumber *) numberOfChildren;
```

#### Return Value

A new [`INLodgingReservation`](../inlodgingreservation.md) object or `nil` if unable to create one.

## Parameters

- `itemReference`: A unique value for the reservation item.
- `reservationNumber`: The reservation or booking number provided by the app.
- `bookingTime`: The date and time the user made the reservation.
- `reservationStatus`: The current status of the reservation.
- `reservationHolderName`: The name of the person the reservation is under.
- `actions`: The available actions for the reservation. For example, checking in for the reservation from your phone.
- `lodgingBusinessLocation`: The name and location of the lodging establishment.
- `reservationDuration`: The date and time range that indicates the start and end times for the reservation.
- `numberOfAdults`: The number of adults staying in the lodging.
- `numberOfChildren`: The number of children staying in the lodging.

## See Also

### Creating a Lodging Reservation
- [- initWithItemReference:reservationNumber:bookingTime:reservationStatus:reservationHolderName:actions:URL:lodgingBusinessLocation:reservationDuration:numberOfAdults:numberOfChildren:](./initwithitemreference_reservationnumber_bookingtime_reservationstatus_reservationholdername_actions_url_lodgingbusinesslocation_reservationduration_numberofadults_numberofchildren_.md)
  Creates a lodging reservation with the specified contents and attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlodgingreservation/initwithitemreference:reservationnumber:bookingtime:reservationstatus:reservationholdername:actions:lodgingbusinesslocation:reservationduration:numberofadults:numberofchildren:)*