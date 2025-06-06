# mouseLocationOutsideOfEventStream

**Framework**: AppKit  
**Kind**: property

The current location of the pointer reckoned in the window’s base coordinate system, regardless of the current event being handled or of any events pending.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var mouseLocationOutsideOfEventStream: NSPoint { get }
```

#### Discussion

For the same information in screen coordinates, use `NSEvent`’s [`mouseLocation`](nsevent/mouselocation.md).

## See Also

- [var currentEvent: NSEvent?](nsapplication/currentevent.md)
  The last event object that the app retrieved from the event queue.
- [var acceptsMouseMovedEvents: Bool](nswindow/acceptsmousemovedevents.md)
  A Boolean value that indicates whether the window accepts mouse-moved events.
- [var ignoresMouseEvents: Bool](nswindow/ignoresmouseevents.md)
  A Boolean value that indicates whether the window is transparent to mouse events.
- [class func windowNumber(at: NSPoint, belowWindowWithWindowNumber: Int) -> Int](nswindow/windownumber(at:belowwindowwithwindownumber:).md)
  Returns the number of the frontmost window that would be hit by a mouse-down at the specified screen location.
- [func trackEvents(matching: NSEvent.EventTypeMask, timeout: TimeInterval, mode: RunLoop.Mode, handler: (NSEvent?, UnsafeMutablePointer<ObjCBool>) -> Void)](nswindow/trackevents(matching:timeout:mode:handler:).md)
  Tracks events that match the specified mask using the specified tracking handler until the tracking handler explicitly terminates tracking.
- [func performDrag(with: NSEvent)](nswindow/performdrag(with:).md)
  Starts a window drag based on the specified mouse-down event.
- [class let foreverDuration: TimeInterval](nsevent/foreverduration.md)
  The longest time duration possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/mouselocationoutsideofeventstream)*