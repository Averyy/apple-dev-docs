# stop(_:)

**Framework**: AppKit  
**Kind**: method

Stops the main event loop.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func stop(_ sender: Any?)
```

#### Discussion

This method notifies the app that you want to exit the current run loop as soon as it finishes processing the current [`NSEvent`](nsevent.md) object. This method doesn’t forcibly exit the current run loop. Instead it sets a flag that the app checks only after it finishes dispatching an actual event object. For example, you could call this method from an action method responding to a button click or from one of the many methods defined by the [`NSResponder`](nsresponder.md) class. However, calling this method from a timer or run-loop observer routine wouldn’t stop the run loop because they don’t result in the posting of an [`NSEvent`](nsevent.md) object.

If you call this method from an event handler running in your main run loop, the app object exits out of the [`run()`](nsapplication/run().md) method, thereby returning control to the `main()` function. If you call this method from within a modal event loop, it will exit the modal loop instead of the main event loop.

## Parameters

- `sender`: The object that sent this message.

## See Also

- [func runModalSession(NSApplication.ModalSession) -> NSApplication.ModalResponse](nsapplication/runmodalsession(_:).md)
  Runs a given modal session, as defined in a previous invocation of [`beginModalSession(for:)`](nsapplication/beginmodalsession(for:).md).
- [func terminate(Any?)](nsapplication/terminate(_:).md)
  Terminates the receiver.
- [func runModal(for: NSWindow) -> NSApplication.ModalResponse](nsapplication/runmodal(for:).md)
  Starts a modal event loop for the specified window.
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
- [func sendEvent(NSEvent)](nsapplication/sendevent(_:).md)
  Dispatches an event to other objects.
- [func postEvent(NSEvent, atStart: Bool)](nsapplication/postevent(_:atstart:).md)
  Adds a given event to the receiver’s event queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/stop(_:))*