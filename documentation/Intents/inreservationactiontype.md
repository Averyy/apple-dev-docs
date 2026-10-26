# INReservationActionType

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the type of reservation action.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum INReservationActionType
```

```c
enum INReservationActionType : NSInteger;
```

## Topics

### Action Type
- [INReservationActionType.unknown](./inreservationactiontype/unknown.md)
  An unknown state.
- [INReservationActionType.checkIn](./inreservationactiontype/checkin.md)
  A check-in action.
### Initializers
- [init?(rawValue: Int)](./inreservationactiontype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Reservation Action Information
- [var type: INReservationActionType](./inreservationaction/type.md)
  The type of action for the reservation.
- [var userActivity: NSUserActivity](./inreservationaction/useractivity.md)
  The user activity object used when launching your app.
- [var validDuration: INDateComponentsRange](./inreservationaction/validduration.md)
  The date and time range that the action is valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inreservationactiontype)*