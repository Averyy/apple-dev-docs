# performDrag(with:)

**Framework**: AppKit  
**Kind**: method

Starts a window drag based on the specified mouse-down event.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func performDrag(with event: NSEvent)
```

#### Discussion

Your application (or a view) can call this method after receiving and examining a mouse-down event. Upon examination of the event, a view may allow that portion of the window to start a window drag and can hand off the work to the Window Server process by calling this method. Doing so allows the window to participate in space switching and other system features.

This method returns right away, and a mouse-up event may not get sent.

## Parameters

- `event`: The original mouse-down event received by the application or a view.

## See Also

- [var acceptsMouseMovedEvents: Bool](nswindow/acceptsmousemovedevents.md)
  A Boolean value that indicates whether the window accepts mouse-moved events.
- [var ignoresMouseEvents: Bool](nswindow/ignoresmouseevents.md)
  A Boolean value that indicates whether the window is transparent to mouse events.
- [var mouseLocationOutsideOfEventStream: NSPoint](nswindow/mouselocationoutsideofeventstream.md)
  The current location of the pointer reckoned in the window’s base coordinate system, regardless of the current event being handled or of any events pending.
- [class func windowNumber(at: NSPoint, belowWindowWithWindowNumber: Int) -> Int](nswindow/windownumber(at:belowwindowwithwindownumber:).md)
  Returns the number of the frontmost window that would be hit by a mouse-down at the specified screen location.
- [func trackEvents(matching: NSEvent.EventTypeMask, timeout: TimeInterval, mode: RunLoop.Mode, handler: (NSEvent?, UnsafeMutablePointer<ObjCBool>) -> Void)](nswindow/trackevents(matching:timeout:mode:handler:).md)
  Tracks events that match the specified mask using the specified tracking handler until the tracking handler explicitly terminates tracking.
- [class let foreverDuration: TimeInterval](nsevent/foreverduration.md)
  The longest time duration possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/performdrag(with:))*