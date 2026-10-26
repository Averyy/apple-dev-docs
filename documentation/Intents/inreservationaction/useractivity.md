# userActivity

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The user activity object used when launching your app.

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
var userActivity: NSUserActivity { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSUserActivity * userActivity;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSUserActivity * userActivity;
```

## See Also

### Getting the Reservation Action Information
- [var type: INReservationActionType](./type.md)
  The type of action for the reservation.
- [enum INReservationActionType](../inreservationactiontype.md)
  Constants that describe the type of reservation action.
- [var validDuration: INDateComponentsRange](./validduration.md)
  The date and time range that the action is valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inreservationaction/useractivity)*