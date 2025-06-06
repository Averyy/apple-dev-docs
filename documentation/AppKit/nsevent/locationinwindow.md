# locationInWindow

**Framework**: AppKit  
**Kind**: property

The event location in the base coordinate system of the associated window.

**Availability**:
- macOS ?+

## Declaration

```swift
var locationInWindow: NSPoint { get }
```

#### Discussion

This property applies to mouse events. For non-mouse events the value of this property is undefined.

With [`NSMouseMoved`](nsmousemoved.md) and possibly other events, the event can have a `nil` window (that is, the [`window`](nsevent/window.md) property contains nil). In this case, this property contains the event location in screen coordinates.

In a method of a custom view that handles mouse events, you commonly use this property with the [`convert(_:from:)`](nsview/convert(_:from:)-1dq9l.md) method of [`NSView`](nsview.md) to get the mouse location in the view’s coordinate system. The following code shows how to perform this conversion. The y coordinate in the returned point starts from a base of 1, and not 0.

```objc
NSPoint event_location = theEvent.locationInWindow;
NSPoint local_point = [self convertPoint:event_location fromView:nil];
```

## See Also

- [var timestamp: TimeInterval](nsevent/timestamp.md)
  The time when the event occurred in seconds since system startup.
- [var window: NSWindow?](nsevent/window.md)
  The window object associated with the event.
- [var windowNumber: Int](nsevent/windownumber.md)
  The identifier for the window device associated with the event.
- [var eventRef: UnsafeRawPointer?](nsevent/eventref.md)
  An opaque Carbon type associated with this event.
- [var cgEvent: CGEvent?](nsevent/cgevent.md)
  The Core Graphics event object corresponding to this event.
- [class let foreverDuration: TimeInterval](nsevent/foreverduration.md)
  The longest time duration possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/locationinwindow)*