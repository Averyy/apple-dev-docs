# trackEvents(matching:timeout:mode:handler:)

**Framework**: AppKit  
**Kind**: method

Tracks events that match the specified mask using the specified tracking handler until the tracking handler explicitly terminates tracking.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func trackEvents(matching mask: NSEvent.EventTypeMask, timeout: TimeInterval, mode: RunLoop.Mode, handler trackingHandler: (NSEvent?, UnsafeMutablePointer<ObjCBool>) -> Void)
```

#### Discussion

You can use this method in a tracking loop to get pressure events when you add [`pressure`](nsevent/eventtypemask/pressure.md) to the event mask. This method returns when tracking terminates.

Each event is removed from the event queue and then passed to the tracking handler. If a matching event does not exist in the event queue, the main thread blocks in the specified runloop mode until an event of the requested type is received or the specified timeout expires. If the timeout expires, the tracking handler is called with a `nil` event (a negative timeout is interpreted as `0`). Use `NSEventDurationForever` to prevent timing out. Tracking continues until you set `stop` to [`true`](https://developer.apple.com/documentation/Swift/true). Note that calls to [`nextEvent(matching:)`](nswindow/nextevent(matching:).md) are allowed inside the `trackingHandler` block.

## Parameters

- `mask`: The event mask (see   in   for possible values).
- `timeout`: The maximum time interval the system waits for an event before passing   to the handler.
- `mode`: The run loop mode.
- `trackingHandler`: A block that is called to track the events. The block takes the following parameters:

## See Also

- [var acceptsMouseMovedEvents: Bool](nswindow/acceptsmousemovedevents.md)
  A Boolean value that indicates whether the window accepts mouse-moved events.
- [var ignoresMouseEvents: Bool](nswindow/ignoresmouseevents.md)
  A Boolean value that indicates whether the window is transparent to mouse events.
- [var mouseLocationOutsideOfEventStream: NSPoint](nswindow/mouselocationoutsideofeventstream.md)
  The current location of the pointer reckoned in the window’s base coordinate system, regardless of the current event being handled or of any events pending.
- [class func windowNumber(at: NSPoint, belowWindowWithWindowNumber: Int) -> Int](nswindow/windownumber(at:belowwindowwithwindownumber:).md)
  Returns the number of the frontmost window that would be hit by a mouse-down at the specified screen location.
- [func performDrag(with: NSEvent)](nswindow/performdrag(with:).md)
  Starts a window drag based on the specified mouse-down event.
- [class let foreverDuration: TimeInterval](nsevent/foreverduration.md)
  The longest time duration possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/trackevents(matching:timeout:mode:handler:))*