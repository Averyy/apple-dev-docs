# subtype

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The event’s subtype.

**Availability**:
- macOS

## Declaration

```swift
var subtype: NSEvent.EventSubtype { get }
```

```objc
@property (readonly) NSEventSubtype subtype;
```

#### Discussion

Access this property only if the event is a mouse event or if the [`type`](./type.md) property contains [`NSAppKitDefined`](../nsappkitdefined.md), [`NSSystemDefined`](../nssystemdefined.md), [`NSApplicationDefined`](../nsapplicationdefined.md), or [`NSPeriodic`](../nsperiodic.md). If you access this property for other types, AppKit raises [`internalInconsistencyException`](../../Foundation/nsexceptionname/internalinconsistencyexception.md). For information about predefined mouse and tablet subtypes, see `Getting Unicode Values`.

[`NSPeriodic`](../nsperiodic.md) events don’t use this property.

## See Also

### Related Documentation
- [var data1: Int](./data1.md)
  Additional data associated with this event.
- [var data2: Int](./data2.md)
  Additional data associated with this event.
- [class func otherEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, subtype: Int16, data1: Int, data2: Int) -> NSEvent?](./otherevent%28with,location,modifierflags,timestamp,windownumber,context,subtype,data1,data2%29.md)
  Creates and returns a new event object that describes a custom event.
### Getting the event type
- [var type: NSEvent.EventType](./type.md)
  The event’s type.
- [NSEvent.EventType](./eventtype.md)
  Constants for the types of events that responder objects can handle.
- [NSEvent.EventTypeMask](./eventtypemask.md)
  Constants that you use to filter out specific event types from the stream of incoming events.
- [NSEvent.EventSubtype](./eventsubtype.md)
  Subtypes for various types of events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/subtype)*