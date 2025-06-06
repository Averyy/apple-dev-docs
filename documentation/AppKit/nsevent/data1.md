# data1

**Framework**: AppKit  
**Kind**: property

Additional data associated with this event.

**Availability**:
- macOS ?+

## Declaration

```swift
var data1: Int { get }
```

#### Discussion

The originator of the event defines the data in this property, and the data is dependent on the event type. If the type of this event isn’t  [`NSAppKitDefined`](nsappkitdefined.md), [`NSSystemDefined`](nssystemdefined.md), [`NSApplicationDefined`](nsapplicationdefined.md), or [`NSPeriodic`](nsperiodic.md), accessing this property raises [`internalInconsistencyException`](https://developer.apple.com/documentation/foundation/nsexceptionname/1416220-internalinconsistencyexception).

[`NSPeriodic`](nsperiodic.md) events don’t use this property.

## See Also

- [var subtype: NSEvent.EventSubtype](nsevent/subtype.md)
  The event’s subtype.
- [class func otherEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, subtype: Int16, data1: Int, data2: Int) -> NSEvent?](nsevent/otherevent(with:location:modifierflags:timestamp:windownumber:context:subtype:data1:data2:).md)
  Creates and returns a new event object that describes a custom event.
- [var data2: Int](nsevent/data2.md)
  Additional data associated with this event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/data1)*