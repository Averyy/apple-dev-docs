# INSeat

**Framework**: Intents  
**Kind**: class  
**Role**: Class

An object containing seat information associated with a reservation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INSeat
```

```objc
@interface INSeat : NSObject
```

## Topics

### Creating a Seat Object
- [init(seatSection: String?, seatRow: String?, seatNumber: String?, seatingType: String?)](./inseat/init%28seatsection,seatrow,seatnumber,seatingtype%29.md)
  Creates a new seat object containing the required seat information.
### Describing a Seat
- [var seatSection: String?](./inseat/seatsection.md)
  The seat’s section.
- [var seatRow: String?](./inseat/seatrow.md)
  The seat’s row.
- [var seatNumber: String?](./inseat/seatnumber.md)
  The seat’s number.
- [var seatingType: String?](./inseat/seatingtype.md)
  The seat’s type.
### Initializers
- [init?(coder: NSCoder)](./inseat/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
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

### Common Reservation Data Objects
- [class INReservation](./inreservation.md)
  An object that describes a reservation.
- [class INReservationAction](./inreservationaction.md)
  An action a user can perform that’s relevant to a reservation.
- [enum INReservationStatus](./inreservationstatus.md)
  Constants that describe the current status of the reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inseat)*