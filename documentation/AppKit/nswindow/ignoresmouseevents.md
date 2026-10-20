# ignoresMouseEvents

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the window is transparent to mouse events.

**Availability**:
- macOS

## Declaration

```swift
var ignoresMouseEvents: Bool { get set }
```

```objc
@property BOOL ignoresMouseEvents;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) when the window is transparent to mouse events; otherwise, [`false`](../../Swift/false.md).

## See Also

### Handling Mouse Events
- [var acceptsMouseMovedEvents: Bool](./acceptsmousemovedevents.md)
  A Boolean value that indicates whether the window accepts mouse-moved events.
- [var mouseLocationOutsideOfEventStream: NSPoint](./mouselocationoutsideofeventstream.md)
  The current location of the pointer reckoned in the window’s base coordinate system, regardless of the current event being handled or of any events pending.
- [class func windowNumber(at: NSPoint, belowWindowWithWindowNumber: Int) -> Int](./windownumber%28at,belowwindowwithwindownumber%29.md)
  Returns the number of the frontmost window that would be hit by a mouse-down at the specified screen location.
- [func trackEvents(matching: NSEvent.EventTypeMask, timeout: TimeInterval, mode: RunLoop.Mode, handler: (NSEvent?, UnsafeMutablePointer<ObjCBool>) -> Void)](./trackevents%28matching,timeout,mode,handler%29.md)
  Tracks events that match the specified mask using the specified tracking handler until the tracking handler explicitly terminates tracking.
- [func performDrag(with: NSEvent)](./performdrag%28with%29.md)
  Starts a window drag based on the specified mouse-down event.
- [class var foreverDuration: TimeInterval](../nsevent/foreverduration.md)
  The longest time duration possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/ignoresmouseevents)*