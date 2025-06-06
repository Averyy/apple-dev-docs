# currentEvent

**Framework**: AppKit  
**Kind**: property

The last event object that the app retrieved from the event queue.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var currentEvent: NSEvent? { get }
```

#### Discussion

The shared app object receives events and forwards them to the affected [`NSWindow`](nswindow.md) objects, which then distribute them to the objects in its view hierarchy. Use this property to get the event that was last handled by the app.

## See Also

- [func nextEvent(matching: NSEvent.EventTypeMask, until: Date?, inMode: RunLoop.Mode, dequeue: Bool) -> NSEvent?](nsapplication/nextevent(matching:until:inmode:dequeue:).md)
  Returns the next event matching a given mask, or `nil` if no such event is found before a specified expiration date.
- [func discardEvents(matching: NSEvent.EventTypeMask, before: NSEvent?)](nsapplication/discardevents(matching:before:).md)
  Removes all events matching the given mask and generated before the specified event.
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
- [func postEvent(NSEvent, atStart: Bool)](nsapplication/postevent(_:atstart:).md)
  Adds a given event to the receiver’s event queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/currentevent)*