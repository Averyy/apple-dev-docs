# eventNumber

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The counter value of the latest mouse or tracking-rectangle event object.

**Availability**:
- macOS

## Declaration

```swift
var eventNumber: Int { get }
```

```objc
@property (readonly) NSInteger eventNumber;
```

## Discussion

Every system-generated mouse and tracking-rectangle event increments this counter. If you access this property on an event of an unsupported type, AppKit raises [`internalInconsistencyException`](../../Foundation/nsexceptionname/internalinconsistencyexception.md).

## See Also

### Related Documentation
- [class func enterExitEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, eventNumber: Int, trackingNumber: Int, userData: UnsafeMutableRawPointer?) -> NSEvent?](./enterexitevent%28with,location,modifierflags,timestamp,windownumber,context,eventnumber,trackingnumber,userdata%29.md)
  Creates and returns a new event object that describes a tracking-rectangle or cursor-update event.
- [class func mouseEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, eventNumber: Int, clickCount: Int, pressure: Float) -> NSEvent?](./mouseevent%28with,location,modifierflags,timestamp,windownumber,context,eventnumber,clickcount,pressure%29.md)
  Creates and returns a new event object that describes a mouse-down, -up, -moved, or -dragged event.
### Getting tracking area information
- [var trackingNumber: Int](./trackingnumber.md)
  The identifier of a mouse-tracking event.
- [var trackingArea: NSTrackingArea?](./trackingarea.md)
  The tracking area for the event.
- [var userData: UnsafeMutableRawPointer?](./userdata.md)
  The data associated with a mouse-tracking event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/eventnumber)*