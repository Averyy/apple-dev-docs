# trackingArea

**Framework**: AppKit  
**Kind**: property

The tracking area for the event.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var trackingArea: NSTrackingArea? { get }
```

#### Discussion

If you access this property on an event object that is not a mouse-tracking event — that is, its event type isn’t [`NSMouseEntered`](nsmouseentered.md), [`NSMouseExited`](nsmouseexited.md), or [`NSCursorUpdate`](nscursorupdate.md) —AppKit raises an [`internalInconsistencyException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/internalInconsistencyException).

If the event corresponds to a tracking rectangle installed with the [`addTrackingRect(_:owner:userData:assumeInside:)`](nsview/addtrackingrect(_:owner:userdata:assumeinside:).md) method of [`NSView`](nsview.md), the value of this property is `nil`. The [`trackingNumber`](nsevent/trackingnumber.md) property contains either an [`NSTrackingArea`](nstrackingarea.md) object or [`NSView.TrackingRectTag`](nsview/trackingrecttag.md), depending on how AppKit generated the event.

## See Also

- [var eventNumber: Int](nsevent/eventnumber.md)
  The counter value of the latest mouse or tracking-rectangle event object.
- [var trackingNumber: Int](nsevent/trackingnumber.md)
  The identifier of a mouse-tracking event.
- [var userData: UnsafeMutableRawPointer?](nsevent/userdata.md)
  The data associated with a mouse-tracking event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/trackingarea)*