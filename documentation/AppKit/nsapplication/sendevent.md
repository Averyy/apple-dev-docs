# sendEvent(_:)

**Framework**: AppKit  
**Kind**: method

Dispatches an event to other objects.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func sendEvent(_ event: NSEvent)
```

#### Discussion

You rarely invoke [`sendEvent(_:)`](nsapplication/sendevent(_:).md) directly, although you might want to override this method to perform some action on every event. [`sendEvent(_:)`](nsapplication/sendevent(_:).md) messages are sent from the main event loop (the [`run()`](nsapplication/run().md) method). [`sendEvent(_:)`](nsapplication/sendevent(_:).md) is the method that dispatches events to the appropriate responders—`NSApp` handles app events, the [`NSWindow`](nswindow.md) object indicated in the event record handles window-related events, and mouse and key events are forwarded to the appropriate [`NSWindow`](nswindow.md) object for further dispatching.

## Parameters

- `event`: The event object to dispatch.

## See Also

- [func nextEvent(matching: NSEvent.EventTypeMask, until: Date?, inMode: RunLoop.Mode, dequeue: Bool) -> NSEvent?](nsapplication/nextevent(matching:until:inmode:dequeue:).md)
  Returns the next event matching a given mask, or `nil` if no such event is found before a specified expiration date.
- [func discardEvents(matching: NSEvent.EventTypeMask, before: NSEvent?)](nsapplication/discardevents(matching:before:).md)
  Removes all events matching the given mask and generated before the specified event.
- [var currentEvent: NSEvent?](nsapplication/currentevent.md)
  The last event object that the app retrieved from the event queue.
- [var isRunning: Bool](nsapplication/isrunning.md)
  A Boolean value indicating whether the main event loop is running.
- [func run()](nsapplication/run.md)
  Starts the main event loop.
- [func finishLaunching()](nsapplication/finishlaunching.md)
  Activates the app, opens any files specified by the `NSOpen` user default, and unhighlights the app’s icon.
- [func stop(Any?)](nsapplication/stop(_:).md)
  Stops the main event loop.
- [func postEvent(NSEvent, atStart: Bool)](nsapplication/postevent(_:atstart:).md)
  Adds a given event to the receiver’s event queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/sendevent(_:))*