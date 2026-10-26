# stop(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Stops the main event loop.

**Availability**:
- macOS

## Declaration

```swift
func stop(_ sender: Any?)
```

```objc
- (void) stop:(id) sender;
```

#### Discussion

This method notifies the app that you want to exit the current run loop as soon as it finishes processing the current [`NSEvent`](../nsevent.md) object. This method doesn’t forcibly exit the current run loop. Instead it sets a flag that the app checks only after it finishes dispatching an actual event object. For example, you could call this method from an action method responding to a button click or from one of the many methods defined by the [`NSResponder`](../nsresponder.md) class. However, calling this method from a timer or run-loop observer routine wouldn’t stop the run loop because they don’t result in the posting of an [`NSEvent`](../nsevent.md) object.

If you call this method from an event handler running in your main run loop, the app object exits out of the [`run()`](./run%28%29.md) method, thereby returning control to the `main()` function. If you call this method from within a modal event loop, it will exit the modal loop instead of the main event loop.

## Parameters

- `sender`: The object that sent this message.

## See Also

### Related Documentation
- [func runModalSession(NSApplication.ModalSession) -> NSApplication.ModalResponse](./runmodalsession%28_%29.md)
  Runs a given modal session, as defined in a previous invocation of [`beginModalSession(for:)`](./beginmodalsession%28for%29.md).
- [func terminate(Any?)](./terminate%28_%29.md)
  Terminates the receiver.
- [func runModal(for: NSWindow) -> NSApplication.ModalResponse](./runmodal%28for%29.md)
  Starts a modal event loop for the specified window.
### Managing the event loop
- [func nextEvent(matching: NSEvent.EventTypeMask, until: Date?, inMode: RunLoop.Mode, dequeue: Bool) -> NSEvent?](./nextevent%28matching,until,inmode,dequeue%29.md)
  Returns the next event matching a given mask, or `nil` if no such event is found before a specified expiration date.
- [func discardEvents(matching: NSEvent.EventTypeMask, before: NSEvent?)](./discardevents%28matching,before%29.md)
  Removes all events matching the given mask and generated before the specified event.
- [var currentEvent: NSEvent?](./currentevent.md)
  The last event object that the app retrieved from the event queue.
- [var isRunning: Bool](./isrunning.md)
  A Boolean value indicating whether the main event loop is running.
- [func run()](./run%28%29.md)
  Starts the main event loop.
- [func finishLaunching()](./finishlaunching%28%29.md)
  Activates the app, opens any files specified by the `NSOpen` user default, and unhighlights the app’s icon.
- [func sendEvent(NSEvent)](./sendevent%28_%29.md)
  Dispatches an event to other objects.
- [func postEvent(NSEvent, atStart: Bool)](./postevent%28_,atstart%29.md)
  Adds a given event to the receiver’s event queue.
- [NSEventTrackingRunLoopMode](../nseventtrackingrunloopmode.md)
  The mode set when tracking events modally, such as a mouse-dragging loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/stop(_:))*