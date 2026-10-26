# initWithItemReference:reservationNumber:bookingTime:reservationStatus:reservationHolderName:actions:URL:lodgingBusinessLocation:reservationDuration:numberOfAdults:numberOfChildren:

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Creates a lodging reservation with the specified contents and attributes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```objc
- (instancetype) initWithItemReference:(INSpeakableString *) itemReference reservationNumber:(NSString *) reservationNumber bookingTime:(NSDate *) bookingTime reservationStatus:(INReservationStatus) reservationStatus reservationHolderName:(NSString *) reservationHolderName actions:(NSArray<INReservationAction *> *) actions URL:(NSURL *) URL lodgingBusinessLocation:(CLPlacemark *) lodgingBusinessLocation reservationDuration:(INDateComponentsRange *) reservationDuration numberOfAdults:(NSNumber *) numberOfAdults numberOfChildren:(NSNumber *) numberOfChildren;
```

#### Return Value

A new [`INLodgingReservation`](../inlodgingreservation.md) object or `nil` if unable to create one.

## Parameters

- `itemReference`: A unique identifier for the reservation.
- `reservationNumber`: The reservation number.
- `bookingTime`: The date and time the user made the reservation.
- `reservationStatus`: The current status of the reservation.
- `reservationHolderName`: The reservation holder’s name.
- `actions`: Available actions associated with the reservation.
- `URL`: A webpage containing reservation information.
- `lodgingBusinessLocation`: The name and location of the lodging establishment.
- `reservationDuration`: The date and time range that defines the beginning and end of the reservation.
- `numberOfAdults`: The number of adults staying in the lodging.
- `numberOfChildren`: The number of children staying in the lodging.

## See Also

### Creating a Lodging Reservation
- [- initWithItemReference:reservationNumber:bookingTime:reservationStatus:reservationHolderName:actions:lodgingBusinessLocation:reservationDuration:numberOfAdults:numberOfChildren:](./initwithitemreference_reservationnumber_bookingtime_reservationstatus_reservationholdername_actions_lodgingbusinesslocation_reservationduration_numberofadults_numberofchildren_.md)
  Creates a new lodging reservation with the provided information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlodgingreservation/initwithitemreference:reservationnumber:bookingtime:reservationstatus:reservationholdername:actions:url:lodgingbusinesslocation:reservationduration:numberofadults:numberofchildren:)*