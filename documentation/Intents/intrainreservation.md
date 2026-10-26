# INTrainReservation

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The information that describes a train reservation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INTrainReservation
```

```objc
@interface INTrainReservation : INReservation
```

## Topics

### Creating a Train Reservation
- [init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, url: URL?, reservedSeat: INSeat?, trainTrip: INTrainTrip)](./intrainreservation/init%28itemreference,reservationnumber,bookingtime,reservationstatus,reservationholdername,actions,url,reservedseat,traintrip%29-3z3wm.md)
  Creates a train reservation with the specified contents and attributes.
- [convenience init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, reservedSeat: INSeat?, trainTrip: INTrainTrip)](./intrainreservation/init%28itemreference,reservationnumber,bookingtime,reservationstatus,reservationholdername,actions,reservedseat,traintrip%29.md)
  Creates a new train reservation with the specified contents and attributes.
### Getting the Train Reservation Information
- [var reservedSeat: INSeat?](./intrainreservation/reservedseat.md)
  The seat reserved for the user.
- [var trainTrip: INTrainTrip](./intrainreservation/traintrip.md)
  An object containing the detailed information about the train trip.
- [class INTrainTrip](./intraintrip.md)
  The information that describes a train trip.
### Initializers
- [init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, URL: URL?, reservedSeat: INSeat?, trainTrip: INTrainTrip)](./intrainreservation/init%28itemreference,reservationnumber,bookingtime,reservationstatus,reservationholdername,actions,url,reservedseat,traintrip%29-5kkgr.md)

## Relationships

### Inherits From
- [INReservation](./inreservation.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Travel Reservations
- [class INFlightReservation](./inflightreservation.md)
  The information that describes a flight reservation.
- [class INBoatReservation](./inboatreservation.md)
  The information that describes a boat reservation.
- [class INBusReservation](./inbusreservation.md)
  The information that describes a bus reservation.
- [class INRentalCarReservation](./inrentalcarreservation.md)
  The information that describes a rental car reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intrainreservation)*