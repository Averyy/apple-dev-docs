# type

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The type of action for the reservation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var type: INReservationActionType { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INReservationActionType type;
```

*macOS*

```objc
@property (atomic, assign, readonly) INReservationActionType type;
```

## See Also

### Getting the Reservation Action Information
- [enum INReservationActionType](../inreservationactiontype.md)
  Constants that describe the type of reservation action.
- [var userActivity: NSUserActivity](./useractivity.md)
  The user activity object used when launching your app.
- [var validDuration: INDateComponentsRange](./validduration.md)
  The date and time range that the action is valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inreservationaction/type)*