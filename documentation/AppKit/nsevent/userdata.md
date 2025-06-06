# userData

**Framework**: AppKit  
**Kind**: property

The data associated with a mouse-tracking event.

**Availability**:
- macOS ?+

## Declaration

```swift
var userData: UnsafeMutableRawPointer? { get }
```

#### Discussion

When you call [`addTrackingRect(_:owner:userData:assumeInside:)`](nsview/addtrackingrect(_:owner:userdata:assumeinside:).md) to set up a tracking rectangle, you can provide custom data to store in the event. AppKit makes that custom data available to you from this property.

This property is only valid when the event is of type [`NSMouseEntered`](nsmouseentered.md) or [`NSMouseExited`](nsmouseexited.md). If you access this property for any other type of event, AppKit raises [`internalInconsistencyException`](https://developer.apple.com/documentation/foundation/nsexceptionname/1416220-internalinconsistencyexception).

## See Also

- [class func enterExitEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, eventNumber: Int, trackingNumber: Int, userData: UnsafeMutableRawPointer?) -> NSEvent?](nsevent/enterexitevent(with:location:modifierflags:timestamp:windownumber:context:eventnumber:trackingnumber:userdata:).md)
  Creates and returns a new event object that describes a tracking-rectangle or cursor-update event.
- [var eventNumber: Int](nsevent/eventnumber.md)
  The counter value of the latest mouse or tracking-rectangle event object.
- [var trackingNumber: Int](nsevent/trackingnumber.md)
  The identifier of a mouse-tracking event.
- [var trackingArea: NSTrackingArea?](nsevent/trackingarea.md)
  The tracking area for the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/userdata)*