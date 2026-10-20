# mouseEnteredAndExited

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The owner of the tracking area receives [`mouseEntered(with:)`](../../nsresponder/mouseentered%28with%29.md) when the mouse cursor enters the area and [`mouseExited(with:)`](../../nsresponder/mouseexited%28with%29.md) events when the mouse leaves the area. This value specifies a type of tracking area.

**Availability**:
- macOS

## Declaration

```swift
static var mouseEnteredAndExited: NSTrackingArea.Options { get }
```

```c
NSTrackingMouseEnteredAndExited
```

## See Also

### Constants
- [static var mouseMoved: NSTrackingArea.Options](./mousemoved.md)
  The owner of the tracking area receives [`mouseMoved(with:)`](../../nsresponder/mousemoved%28with%29.md) messages while the mouse cursor is within the area. This value specifies a type of tracking area.
- [static var cursorUpdate: NSTrackingArea.Options](./cursorupdate.md)
  A tracking option that receives events when the mouse cursor enters and exits the tracking area.
- [static var activeWhenFirstResponder: NSTrackingArea.Options](./activewhenfirstresponder.md)
  The owner receives messages when the view is the first responder. This value specifies when the tracking area defined by an [`NSTrackingArea`](../../nstrackingarea.md) object is active.
- [static var activeInKeyWindow: NSTrackingArea.Options](./activeinkeywindow.md)
  The owner receives messages when the view is in the key window. This value specifies when the tracking area defined by an [`NSTrackingArea`](../../nstrackingarea.md) object is active.
- [static var activeInActiveApp: NSTrackingArea.Options](./activeinactiveapp.md)
  The owner receives messages when the application is active. This value specifies when the tracking area defined by an [`NSTrackingArea`](../../nstrackingarea.md) object is active.
- [static var activeAlways: NSTrackingArea.Options](./activealways.md)
  The owner receives messages regardless of first-responder status, window status, or application status. The [`cursorUpdate(with:)`](../../nsresponder/cursorupdate%28with%29.md) message is *not* sent when the [`cursorUpdate`](./cursorupdate.md) option is specified along with this constant. This value specifies when the tracking area defined by an [`NSTrackingArea`](../../nstrackingarea.md) object is active.
- [static var assumeInside: NSTrackingArea.Options](./assumeinside.md)
  The first event is generated when the cursor leaves the tracking area, regardless if the cursor is inside the area when the `NSTrackingArea` is added to a view.  If this option is not specified, the first event is generated when the cursor leaves the tracking area if the cursor is initially inside the area, or when the cursor enters the area if the cursor is initially outside it. Generally, you do not want to request this behavior. This value specifies a behavior of the tracking area defined by the [`NSTrackingArea`](../../nstrackingarea.md).
- [static var inVisibleRect: NSTrackingArea.Options](./invisiblerect.md)
  Mouse tracking occurs only in the visible rectangle of the view—in other words, that region of the tracking rectangle that is unobscured. Otherwise, the entire tracking area is active regardless of overlapping views. The `NSTrackingArea` object is automatically synchronized with changes in the view’s visible area ([`visibleRect`](../../nsview/visiblerect.md)) and the value returned from [`rect`](../rect.md) is ignored. This value specifies a behavior of the tracking area defined by the [`NSTrackingArea`](../../nstrackingarea.md).
- [static var enabledDuringMouseDrag: NSTrackingArea.Options](./enabledduringmousedrag.md)
  The owner receives [`NSMouseEntered`](../../nsmouseentered.md) events when the mouse cursor is dragged into the tracking area. If this option is not specified, the owner receives mouse-entered events when the mouse is moved (no buttons pressed) into the tracking area and on [`NSLeftMouseUp`](../../nsleftmouseup.md) events after a mouse drag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstrackingarea/options-swift.struct/mouseenteredandexited)*