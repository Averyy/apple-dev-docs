# windowNumber(at:belowWindowWithWindowNumber:)

**Framework**: AppKit  
**Kind**: method

Returns the number of the frontmost window that would be hit by a mouse-down at the specified screen location.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
class func windowNumber(at point: NSPoint, belowWindowWithWindowNumber windowNumber: Int) -> Int
```

#### Return Value

The window number of the window under the point. The window number returned may correspond to a window in another application.

#### Discussion

Because this method uses the same rules as mouse-down hit-testing, windows with transparency at the given point, and windows that ignore mouse events, will not be returned.

## Parameters

- `point`: The location of the mouse-down in screen coordinates.
- `windowNumber`: If non-0, the search will start below   window in z-order.

## See Also

- [var acceptsMouseMovedEvents: Bool](nswindow/acceptsmousemovedevents.md)
  A Boolean value that indicates whether the window accepts mouse-moved events.
- [var ignoresMouseEvents: Bool](nswindow/ignoresmouseevents.md)
  A Boolean value that indicates whether the window is transparent to mouse events.
- [var mouseLocationOutsideOfEventStream: NSPoint](nswindow/mouselocationoutsideofeventstream.md)
  The current location of the pointer reckoned in the window’s base coordinate system, regardless of the current event being handled or of any events pending.
- [func trackEvents(matching: NSEvent.EventTypeMask, timeout: TimeInterval, mode: RunLoop.Mode, handler: (NSEvent?, UnsafeMutablePointer<ObjCBool>) -> Void)](nswindow/trackevents(matching:timeout:mode:handler:).md)
  Tracks events that match the specified mask using the specified tracking handler until the tracking handler explicitly terminates tracking.
- [func performDrag(with: NSEvent)](nswindow/performdrag(with:).md)
  Starts a window drag based on the specified mouse-down event.
- [class let foreverDuration: TimeInterval](nsevent/foreverduration.md)
  The longest time duration possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/windownumber(at:belowwindowwithwindownumber:))*