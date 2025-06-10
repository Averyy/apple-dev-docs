# eventNumber

**Framework**: AppKit  
**Kind**: property

The counter value of the latest mouse or tracking-rectangle event object.

**Availability**:
- macOS ?+

## Declaration

```swift
var eventNumber: Int { get }
```

#### Discussion

Every system-generated mouse and tracking-rectangle event increments this counter. If you access this property on an event of an unsupported type, AppKit raises [`internalInconsistencyException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/internalInconsistencyException).

## See Also

- [class func enterExitEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, eventNumber: Int, trackingNumber: Int, userData: UnsafeMutableRawPointer?) -> NSEvent?](nsevent/enterexitevent(with:location:modifierflags:timestamp:windownumber:context:eventnumber:trackingnumber:userdata:).md)
  Creates and returns a new event object that describes a tracking-rectangle or cursor-update event.
- [class func mouseEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, eventNumber: Int, clickCount: Int, pressure: Float) -> NSEvent?](nsevent/mouseevent(with:location:modifierflags:timestamp:windownumber:context:eventnumber:clickcount:pressure:).md)
  Creates and returns a new event object that describes a mouse-down, -up, -moved, or -dragged event.
- [var trackingNumber: Int](nsevent/trackingnumber.md)
  The identifier of a mouse-tracking event.
- [var trackingArea: NSTrackingArea?](nsevent/trackingarea.md)
  The tracking area for the event.
- [var userData: UnsafeMutableRawPointer?](nsevent/userdata.md)
  The data associated with a mouse-tracking event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/eventnumber)*