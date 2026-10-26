# validDuration

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The date and time range that the action is valid.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@NSCopying
var validDuration: INDateComponentsRange { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) INDateComponentsRange * validDuration;
```

*macOS*

```objc
@property (atomic, copy, readonly) INDateComponentsRange * validDuration;
```

## See Also

### Getting the Reservation Action Information
- [var type: INReservationActionType](./type.md)
  The type of action for the reservation.
- [enum INReservationActionType](../inreservationactiontype.md)
  Constants that describe the type of reservation action.
- [var userActivity: NSUserActivity](./useractivity.md)
  The user activity object used when launching your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inreservationaction/validduration)*