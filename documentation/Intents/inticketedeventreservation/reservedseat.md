# reservedSeat

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The user’s assigned seat for the ticketed event.

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
var reservedSeat: INSeat? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INSeat * reservedSeat;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INSeat * reservedSeat;
```

## See Also

### Getting the Ticketed Event Reservation Information
- [var event: INTicketedEvent](./event.md)
  An object containing detailed information about the ticketed event.
- [class INTicketedEvent](../inticketedevent.md)
  The information that describes a ticketed event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inticketedeventreservation/reservedseat)*