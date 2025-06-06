# acceptsMouseMovedEvents

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the window accepts mouse-moved events.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var acceptsMouseMovedEvents: Bool { get set }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) when the window accepts (and distributes) mouse-moved events; otherwise, [`false`](https://developer.apple.com/documentation/swift/false). By default the value is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var ignoresMouseEvents: Bool](nswindow/ignoresmouseevents.md)
  A Boolean value that indicates whether the window is transparent to mouse events.
- [var mouseLocationOutsideOfEventStream: NSPoint](nswindow/mouselocationoutsideofeventstream.md)
  The current location of the pointer reckoned in the window’s base coordinate system, regardless of the current event being handled or of any events pending.
- [class func windowNumber(at: NSPoint, belowWindowWithWindowNumber: Int) -> Int](nswindow/windownumber(at:belowwindowwithwindownumber:).md)
  Returns the number of the frontmost window that would be hit by a mouse-down at the specified screen location.
- [func trackEvents(matching: NSEvent.EventTypeMask, timeout: TimeInterval, mode: RunLoop.Mode, handler: (NSEvent?, UnsafeMutablePointer<ObjCBool>) -> Void)](nswindow/trackevents(matching:timeout:mode:handler:).md)
  Tracks events that match the specified mask using the specified tracking handler until the tracking handler explicitly terminates tracking.
- [func performDrag(with: NSEvent)](nswindow/performdrag(with:).md)
  Starts a window drag based on the specified mouse-down event.
- [class let foreverDuration: TimeInterval](nsevent/foreverduration.md)
  The longest time duration possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/acceptsmousemovedevents)*