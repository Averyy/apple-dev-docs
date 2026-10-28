# locationInWindow

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The event location in the base coordinate system of the associated window.

**Availability**:
- macOS

## Declaration

```swift
var locationInWindow: NSPoint { get }
```

```objc
@property (readonly) NSPoint locationInWindow;
```

## Discussion

This property applies to mouse events. For non-mouse events the value of this property is undefined.

With [`NSMouseMoved`](../nsmousemoved.md) and possibly other events, the event can have a `nil` window (that is, the [`window`](./window.md) property contains nil). In this case, this property contains the event location in screen coordinates.

In a method of a custom view that handles mouse events, you commonly use this property with the [`convert(_:from:)`](../nsview/convert%28_,from%29-1dq9l.md) method of [`NSView`](../nsview.md) to get the mouse location in the view’s coordinate system. The following code shows how to perform this conversion. The y coordinate in the returned point starts from a base of 1, and not 0.

```objc
NSPoint event_location = theEvent.locationInWindow;
NSPoint local_point = [self convertPoint:event_location fromView:nil];
```

## See Also

### Getting general event information
- [var timestamp: TimeInterval](./timestamp.md)
  The time when the event occurred in seconds since system startup.
- [var window: NSWindow?](./window.md)
  The window object associated with the event.
- [var windowNumber: Int](./windownumber.md)
  The identifier for the window device associated with the event.
- [var eventRef: UnsafeRawPointer?](./eventref.md)
  An opaque Carbon type associated with this event.
- [var cgEvent: CGEvent?](./cgevent.md)
  The Core Graphics event object corresponding to this event.
- [class var foreverDuration: TimeInterval](./foreverduration.md)
  The longest time duration possible.
- [var context: NSGraphicsContext?](./context.md)
  The display graphics context for this event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/locationinwindow)*