# init(itemReference:reservationNumber:bookingTime:reservationStatus:reservationHolderName:actions:url:reservedSeat:busTrip:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a bus reservation with the specified contents and attributes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, url URL: URL?, reservedSeat: INSeat?, busTrip: INBusTrip?)
```

```objc
- (instancetype) initWithItemReference:(INSpeakableString *) itemReference reservationNumber:(NSString *) reservationNumber bookingTime:(NSDate *) bookingTime reservationStatus:(INReservationStatus) reservationStatus reservationHolderName:(NSString *) reservationHolderName actions:(NSArray<INReservationAction *> *) actions URL:(NSURL *) URL reservedSeat:(INSeat *) reservedSeat busTrip:(INBusTrip *) busTrip;
```

#### Return Value

A new `INBusTripReservation` object or `nil` if the initializer can’t create one.

## Parameters

- `itemReference`: A unique identifier for the reservation.
- `reservationNumber`: The reservation number.
- `bookingTime`: The date and time the user made the reservation.
- `reservationStatus`: The current status of the reservation.
- `reservationHolderName`: The reservation holder’s name.
- `actions`: Available actions associated with the reservation.
- `URL`: A webpage containing reservation information.
- `reservedSeat`: The passenger’s assigned seat.
- `busTrip`: Information describing the bus trip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbusreservation/init(itemreference:reservationnumber:bookingtime:reservationstatus:reservationholdername:actions:url:reservedseat:bustrip:)-4spk1)*