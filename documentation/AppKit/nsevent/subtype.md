# subtype

**Framework**: AppKit  
**Kind**: property

The event’s subtype.

**Availability**:
- macOS ?+

## Declaration

```swift
var subtype: NSEvent.EventSubtype { get }
```

#### Discussion

Access this property only if the event is a mouse event or if the [`type`](nsevent/type.md) property contains [`NSAppKitDefined`](nsappkitdefined.md), [`NSSystemDefined`](nssystemdefined.md), [`NSApplicationDefined`](nsapplicationdefined.md), or [`NSPeriodic`](nsperiodic.md). If you access this property for other types, AppKit raises [`internalInconsistencyException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/internalInconsistencyException). For information about predefined mouse and tablet subtypes, see `Getting Unicode Values`.

[`NSPeriodic`](nsperiodic.md) events don’t use this property.

## See Also

- [var data1: Int](nsevent/data1.md)
  Additional data associated with this event.
- [var data2: Int](nsevent/data2.md)
  Additional data associated with this event.
- [class func otherEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, subtype: Int16, data1: Int, data2: Int) -> NSEvent?](nsevent/otherevent(with:location:modifierflags:timestamp:windownumber:context:subtype:data1:data2:).md)
  Creates and returns a new event object that describes a custom event.
- [var type: NSEvent.EventType](nsevent/type.md)
  The event’s type.
- [NSEvent.EventType](nsevent/eventtype.md)
  Constants for the types of events that responder objects can handle.
- [NSEvent.EventTypeMask](nsevent/eventtypemask.md)
  Constants that you use to filter out specific event types from the stream of incoming events.
- [NSEvent.EventSubtype](nsevent/eventsubtype.md)
  Subtypes for various types of events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/subtype)*