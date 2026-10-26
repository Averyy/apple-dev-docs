# init(itemReference:reservationNumber:bookingTime:reservationStatus:reservationHolderName:actions:url:reservedSeat:boatTrip:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a boat reservation with the specified contents and attributes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, url URL: URL?, reservedSeat: INSeat?, boatTrip: INBoatTrip?)
```

```objc
- (instancetype) initWithItemReference:(INSpeakableString *) itemReference reservationNumber:(NSString *) reservationNumber bookingTime:(NSDate *) bookingTime reservationStatus:(INReservationStatus) reservationStatus reservationHolderName:(NSString *) reservationHolderName actions:(NSArray<INReservationAction *> *) actions URL:(NSURL *) URL reservedSeat:(INSeat *) reservedSeat boatTrip:(INBoatTrip *) boatTrip;
```

#### Return Value

A new `INBoatTripReservation` object or `nil` if the initializer can’t create one.

## Parameters

- `itemReference`: A unique identifier for the reservation.
- `reservationNumber`: The reservation number.
- `bookingTime`: The date and time the user booked the reservation.
- `reservationStatus`: The current status of the reservation.
- `reservationHolderName`: The reservation holder’s name.
- `actions`: Available actions associated with the reservation.
- `URL`: A webpage containing reservation information.
- `reservedSeat`: The passenger’s assigned seat.
- `boatTrip`: Information describing the voyage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inboatreservation/init(itemreference:reservationnumber:bookingtime:reservationstatus:reservationholdername:actions:url:reservedseat:boattrip:)-6q5gl)*