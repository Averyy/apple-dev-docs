# init(itemReference:reservationNumber:bookingTime:reservationStatus:reservationHolderName:actions:url:reservedSeat:event:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a ticketed event reservation with the specified contents and attributes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, url URL: URL?, reservedSeat: INSeat?, event: INTicketedEvent)
```

```objc
- (instancetype) initWithItemReference:(INSpeakableString *) itemReference reservationNumber:(NSString *) reservationNumber bookingTime:(NSDate *) bookingTime reservationStatus:(INReservationStatus) reservationStatus reservationHolderName:(NSString *) reservationHolderName actions:(NSArray<INReservationAction *> *) actions URL:(NSURL *) URL reservedSeat:(INSeat *) reservedSeat event:(INTicketedEvent *) event;
```

#### Return Value

A new [`INTicketedEventReservation`](../inticketedeventreservation.md) object or `nil` if one can’t be created.

## Parameters

- `itemReference`: A unique identifier for the reservation.
- `reservationNumber`: The reservation number.
- `bookingTime`: The date and time the user made the reservation.
- `reservationStatus`: The current status of the reservation.
- `reservationHolderName`: The reservation holder’s name.
- `actions`: Available actions associated with the reservation.
- `URL`: A webpage containing reservation information.
- `reservedSeat`: The user’s assigned seat for the ticketed event.
- `event`: Information describing the ticketed event.

## See Also

### Creating a Ticketed Event Reservation
- [convenience init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, reservedSeat: INSeat?, event: INTicketedEvent)](./init%28itemreference,reservationnumber,bookingtime,reservationstatus,reservationholdername,actions,reservedseat,event%29.md)
  Creates a new ticketed event reservation with the specified contents and attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inticketedeventreservation/init(itemreference:reservationnumber:bookingtime:reservationstatus:reservationholdername:actions:url:reservedseat:event:)-9i6f1)*