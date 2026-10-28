# type

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The event’s type.

**Availability**:
- macOS

## Declaration

```swift
var type: NSEvent.EventType { get }
```

```objc
@property (readonly) NSEventType type;
```

## Discussion

For a list of possible values, see [`NSEvent.EventType`](./eventtype.md).

## See Also

### Getting the event type
- [NSEvent.EventType](./eventtype.md)
  Constants for the types of events that responder objects can handle.
- [NSEvent.EventTypeMask](./eventtypemask.md)
  Constants that you use to filter out specific event types from the stream of incoming events.
- [var subtype: NSEvent.EventSubtype](./subtype.md)
  The event’s subtype.
- [NSEvent.EventSubtype](./eventsubtype.md)
  Subtypes for various types of events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/type)*