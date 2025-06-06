# activeWhenFirstResponder

**Framework**: AppKit  
**Kind**: property

The owner receives messages when the view is the first responder. This value specifies when the tracking area defined by an [`NSTrackingArea`](nstrackingarea.md) object is active.

**Availability**:
- macOS ?+

## Declaration

```swift
static var activeWhenFirstResponder: NSTrackingArea.Options { get }
```

## See Also

- [static var mouseEnteredAndExited: NSTrackingArea.Options](nstrackingarea/options-swift.struct/mouseenteredandexited.md)
  The owner of the tracking area receives [`mouseEntered(with:)`](nsresponder/mouseentered(with:).md) when the mouse cursor enters the area and [`mouseExited(with:)`](nsresponder/mouseexited(with:).md) events when the mouse leaves the area. This value specifies a type of tracking area.
- [static var mouseMoved: NSTrackingArea.Options](nstrackingarea/options-swift.struct/mousemoved.md)
  The owner of the tracking area receives [`mouseMoved(with:)`](nsresponder/mousemoved(with:).md) messages while the mouse cursor is within the area. This value specifies a type of tracking area.
- [static var cursorUpdate: NSTrackingArea.Options](nstrackingarea/options-swift.struct/cursorupdate.md)
  A tracking option that receives events when the mouse cursor enters and exits the tracking area.
- [static var activeInKeyWindow: NSTrackingArea.Options](nstrackingarea/options-swift.struct/activeinkeywindow.md)
  The owner receives messages when the view is in the key window. This value specifies when the tracking area defined by an [`NSTrackingArea`](nstrackingarea.md) object is active.
- [static var activeInActiveApp: NSTrackingArea.Options](nstrackingarea/options-swift.struct/activeinactiveapp.md)
  The owner receives messages when the application is active. This value specifies when the tracking area defined by an [`NSTrackingArea`](nstrackingarea.md) object is active.
- [static var activeAlways: NSTrackingArea.Options](nstrackingarea/options-swift.struct/activealways.md)
  The owner receives messages regardless of first-responder status, window status, or application status. The [`cursorUpdate(with:)`](nsresponder/cursorupdate(with:).md) message is  sent when the [`cursorUpdate`](nstrackingarea/options-swift.struct/cursorupdate.md) option is specified along with this constant. This value specifies when the tracking area defined by an [`NSTrackingArea`](nstrackingarea.md) object is active.
- [static var assumeInside: NSTrackingArea.Options](nstrackingarea/options-swift.struct/assumeinside.md)
  The first event is generated when the cursor leaves the tracking area, regardless if the cursor is inside the area when the `NSTrackingArea` is added to a view.  If this option is not specified, the first event is generated when the cursor leaves the tracking area if the cursor is initially inside the area, or when the cursor enters the area if the cursor is initially outside it. Generally, you do not want to request this behavior. This value specifies a behavior of the tracking area defined by the [`NSTrackingArea`](nstrackingarea.md).
- [static var inVisibleRect: NSTrackingArea.Options](nstrackingarea/options-swift.struct/invisiblerect.md)
  Mouse tracking occurs only in the visible rectangle of the view—in other words, that region of the tracking rectangle that is unobscured. Otherwise, the entire tracking area is active regardless of overlapping views. The `NSTrackingArea` object is automatically synchronized with changes in the view’s visible area ([`visibleRect`](nsview/visiblerect.md)) and the value returned from [`rect`](nstrackingarea/rect.md) is ignored. This value specifies a behavior of the tracking area defined by the [`NSTrackingArea`](nstrackingarea.md).
- [static var enabledDuringMouseDrag: NSTrackingArea.Options](nstrackingarea/options-swift.struct/enabledduringmousedrag.md)
  The owner receives [`NSMouseEntered`](nsmouseentered.md) events when the mouse cursor is dragged into the tracking area. If this option is not specified, the owner receives mouse-entered events when the mouse is moved (no buttons pressed) into the tracking area and on [`NSLeftMouseUp`](nsleftmouseup.md) events after a mouse drag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstrackingarea/options-swift.struct/activewhenfirstresponder)*