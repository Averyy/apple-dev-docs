# init(itemReference:reservationNumber:bookingTime:reservationStatus:reservationHolderName:actions:reservedSeat:trainTrip:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a new train reservation with the specified contents and attributes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
convenience init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, reservedSeat: INSeat?, trainTrip: INTrainTrip)
```

```objc
- (instancetype) initWithItemReference:(INSpeakableString *) itemReference reservationNumber:(NSString *) reservationNumber bookingTime:(NSDate *) bookingTime reservationStatus:(INReservationStatus) reservationStatus reservationHolderName:(NSString *) reservationHolderName actions:(NSArray<INReservationAction *> *) actions reservedSeat:(INSeat *) reservedSeat trainTrip:(INTrainTrip *) trainTrip;
```

#### Return Value

A new [`INTrainReservation`](../intrainreservation.md) object or `nil` if one can’t be created.

## Parameters

- `itemReference`: A unique identifier for the reservation.
- `reservationNumber`: The reservation or booking number for the reservation.
- `bookingTime`: The date and time the user made the reservation.
- `reservationStatus`: The current status of the reservation.
- `reservationHolderName`: The reservation holder’s name.
- `actions`: The available actions associated with the reservation.
- `reservedSeat`: The seat assigned to the passenger.
- `trainTrip`: The information that describes the train trip.

## See Also

### Creating a Train Reservation
- [init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, url: URL?, reservedSeat: INSeat?, trainTrip: INTrainTrip)](./init%28itemreference,reservationnumber,bookingtime,reservationstatus,reservationholdername,actions,url,reservedseat,traintrip%29-3z3wm.md)
  Creates a train reservation with the specified contents and attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intrainreservation/init(itemreference:reservationnumber:bookingtime:reservationstatus:reservationholdername:actions:reservedseat:traintrip:))*