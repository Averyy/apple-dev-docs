# postEvent(_:atStart:)

**Framework**: AppKit  
**Kind**: method

Adds a given event to the receiver’s event queue.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func postEvent(_ event: NSEvent, atStart: Bool)
```

#### Discussion

This method can also be called in subthreads. Events posted in subthreads bubble up in the main thread event queue.

## Parameters

- `event`: The event object to post to the queue.
- `atStart`: Specify   to add the event to the front of the queue; otherwise, specify   to add the event to the back of the queue.

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
- [func sendEvent(NSEvent)](nsapplication/sendevent(_:).md)
  Dispatches an event to other objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/postevent(_:atstart:))*