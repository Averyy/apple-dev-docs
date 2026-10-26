# init(itemReference:reservationNumber:bookingTime:reservationStatus:reservationHolderName:actions:reservedSeat:event:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a new ticketed event reservation with the specified contents and attributes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
convenience init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, reservedSeat: INSeat?, event: INTicketedEvent)
```

```objc
- (instancetype) initWithItemReference:(INSpeakableString *) itemReference reservationNumber:(NSString *) reservationNumber bookingTime:(NSDate *) bookingTime reservationStatus:(INReservationStatus) reservationStatus reservationHolderName:(NSString *) reservationHolderName actions:(NSArray<INReservationAction *> *) actions reservedSeat:(INSeat *) reservedSeat event:(INTicketedEvent *) event;
```

#### Return Value

A new [`INRentalCarReservation`](../inrentalcarreservation.md) object or `nil` if one can’t be created.

## Parameters

- `itemReference`: A unique value for the reservation item.
- `reservationNumber`: The reservation or booking number provided by the app.
- `bookingTime`: The date and time the user made the reservation.
- `reservationStatus`: The current status of the reservation.
- `reservationHolderName`: The reservation holder’s name.
- `actions`: The available actions for the reservation. For example, checking in for the reservation from your phone.
- `reservedSeat`: The user’s assigned seat for the ticketed event.
- `event`: An object containing detailed information on the ticketed event.

## See Also

### Creating a Ticketed Event Reservation
- [init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, url: URL?, reservedSeat: INSeat?, event: INTicketedEvent)](./init%28itemreference,reservationnumber,bookingtime,reservationstatus,reservationholdername,actions,url,reservedseat,event%29-9i6f1.md)
  Creates a ticketed event reservation with the specified contents and attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inticketedeventreservation/init(itemreference:reservationnumber:bookingtime:reservationstatus:reservationholdername:actions:reservedseat:event:))*