# mouseLocationOutsideOfEventStream

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The current location of the pointer reckoned in the window’s base coordinate system, regardless of the current event being handled or of any events pending.

**Availability**:
- macOS

## Declaration

```swift
var mouseLocationOutsideOfEventStream: NSPoint { get }
```

```objc
@property (readonly) NSPoint mouseLocationOutsideOfEventStream;
```

#### Discussion

For the same information in screen coordinates, use `NSEvent`’s [`mouseLocation`](../nsevent/mouselocation.md).

## See Also

### Related Documentation
- [var currentEvent: NSEvent?](../nsapplication/currentevent.md)
  The last event object that the app retrieved from the event queue.
### Handling Mouse Events
- [var acceptsMouseMovedEvents: Bool](./acceptsmousemovedevents.md)
  A Boolean value that indicates whether the window accepts mouse-moved events.
- [var ignoresMouseEvents: Bool](./ignoresmouseevents.md)
  A Boolean value that indicates whether the window is transparent to mouse events.
- [class func windowNumber(at: NSPoint, belowWindowWithWindowNumber: Int) -> Int](./windownumber%28at,belowwindowwithwindownumber%29.md)
  Returns the number of the frontmost window that would be hit by a mouse-down at the specified screen location.
- [func trackEvents(matching: NSEvent.EventTypeMask, timeout: TimeInterval, mode: RunLoop.Mode, handler: (NSEvent?, UnsafeMutablePointer<ObjCBool>) -> Void)](./trackevents%28matching,timeout,mode,handler%29.md)
  Tracks events that match the specified mask using the specified tracking handler until the tracking handler explicitly terminates tracking.
- [func performDrag(with: NSEvent)](./performdrag%28with%29.md)
  Starts a window drag based on the specified mouse-down event.
- [class var foreverDuration: TimeInterval](../nsevent/foreverduration.md)
  The longest time duration possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/mouselocationoutsideofeventstream)*