# INReservationStatus

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the current status of the reservation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum INReservationStatus
```

```c
enum INReservationStatus : NSInteger;
```

## Topics

### Reservation Status
- [INReservationStatus.unknown](./inreservationstatus/unknown.md)
  The current reservation is unknown.
- [INReservationStatus.canceled](./inreservationstatus/canceled.md)
  The user or business canceled the reservation.
- [INReservationStatus.pending](./inreservationstatus/pending.md)
  The reservation confirmation is pending.
- [INReservationStatus.hold](./inreservationstatus/hold.md)
  The reservation is on hold.
- [INReservationStatus.confirmed](./inreservationstatus/confirmed.md)
  The reservation is confirmed.
### Initializers
- [init?(rawValue: Int)](./inreservationstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Common Reservation Data Objects
- [class INReservation](./inreservation.md)
  An object that describes a reservation.
- [class INReservationAction](./inreservationaction.md)
  An action a user can perform that’s relevant to a reservation.
- [class INSeat](./inseat.md)
  An object containing seat information associated with a reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inreservationstatus)*