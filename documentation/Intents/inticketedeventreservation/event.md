# event

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

An object containing detailed information about the ticketed event.

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
var event: INTicketedEvent { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) INTicketedEvent * event;
```

*macOS*

```objc
@property (atomic, copy, readonly) INTicketedEvent * event;
```

## See Also

### Getting the Ticketed Event Reservation Information
- [class INTicketedEvent](../inticketedevent.md)
  The information that describes a ticketed event.
- [var reservedSeat: INSeat?](./reservedseat.md)
  The user’s assigned seat for the ticketed event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inticketedeventreservation/event)*