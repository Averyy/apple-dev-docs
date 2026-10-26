# INReservationAction

**Framework**: Intents  
**Kind**: class  
**Role**: Class

An action a user can perform that’s relevant to a reservation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INReservationAction
```

```objc
@interface INReservationAction : NSObject
```

## Mentions

- [Donating Reservations](../SiriKit/donating-reservations.md)

## Topics

### Creating a Reservation Action
- [init(type: INReservationActionType, validDuration: INDateComponentsRange, userActivity: NSUserActivity)](./inreservationaction/init%28type,validduration,useractivity%29.md)
  Creates a new reservation action.
### Getting the Reservation Action Information
- [var type: INReservationActionType](./inreservationaction/type.md)
  The type of action for the reservation.
- [enum INReservationActionType](./inreservationactiontype.md)
  Constants that describe the type of reservation action.
- [var userActivity: NSUserActivity](./inreservationaction/useractivity.md)
  The user activity object used when launching your app.
- [var validDuration: INDateComponentsRange](./inreservationaction/validduration.md)
  The date and time range that the action is valid.
### Initializers
- [init?(coder: NSCoder)](./inreservationaction/init%28coder%29.md)

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
- [enum INReservationStatus](./inreservationstatus.md)
  Constants that describe the current status of the reservation.
- [class INSeat](./inseat.md)
  An object containing seat information associated with a reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inreservationaction)*