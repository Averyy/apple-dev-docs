# trackingNumber

**Framework**: AppKit  
**Kind**: property

The identifier of a mouse-tracking event.

**Availability**:
- macOS ?+

## Declaration

```swift
var trackingNumber: Int { get }
```

#### Discussion

This property contains either an [`NSTrackingArea`](nstrackingarea.md) object or an [`NSView.TrackingRectTag`](nsview/trackingrecttag.md) constant, depending on how AppKit generated the event. Valid mouse-tracking event types are [`NSMouseEntered`](nsmouseentered.md), [`NSMouseExited`](nsmouseexited.md), and [`NSCursorUpdate`](nscursorupdate.md). For other types of events, accessing this property raises [`internalInconsistencyException`](https://developer.apple.com/documentation/foundation/nsexceptionname/1416220-internalinconsistencyexception).

## See Also

- [class func enterExitEvent(with: NSEvent.EventType, location: NSPoint, modifierFlags: NSEvent.ModifierFlags, timestamp: TimeInterval, windowNumber: Int, context: NSGraphicsContext?, eventNumber: Int, trackingNumber: Int, userData: UnsafeMutableRawPointer?) -> NSEvent?](nsevent/enterexitevent(with:location:modifierflags:timestamp:windownumber:context:eventnumber:trackingnumber:userdata:).md)
  Creates and returns a new event object that describes a tracking-rectangle or cursor-update event.
- [func addTrackingRect(NSRect, owner: Any, userData: UnsafeMutableRawPointer?, assumeInside: Bool) -> NSView.TrackingRectTag](nsview/addtrackingrect(_:owner:userdata:assumeinside:).md)
  Establishes  an area for tracking mouse-entered and mouse-exited events within the view and returns a tag that identifies the tracking rectangle.
- [var eventNumber: Int](nsevent/eventnumber.md)
  The counter value of the latest mouse or tracking-rectangle event object.
- [var trackingArea: NSTrackingArea?](nsevent/trackingarea.md)
  The tracking area for the event.
- [var userData: UnsafeMutableRawPointer?](nsevent/userdata.md)
  The data associated with a mouse-tracking event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/trackingnumber)*