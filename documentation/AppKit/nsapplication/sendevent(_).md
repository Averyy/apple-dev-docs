# sendEvent(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Dispatches an event to other objects.

**Availability**:
- macOS

## Declaration

```swift
func sendEvent(_ event: NSEvent)
```

```objc
- (void) sendEvent:(NSEvent *) event;
```

#### Discussion

You rarely invoke [`sendEvent(_:)`](./sendevent%28_%29.md) directly, although you might want to override this method to perform some action on every event. [`sendEvent(_:)`](./sendevent%28_%29.md) messages are sent from the main event loop (the [`run()`](./run%28%29.md) method). [`sendEvent(_:)`](./sendevent%28_%29.md) is the method that dispatches events to the appropriate responders—`NSApp` handles app events, the [`NSWindow`](../nswindow.md) object indicated in the event record handles window-related events, and mouse and key events are forwarded to the appropriate [`NSWindow`](../nswindow.md) object for further dispatching.

## Parameters

- `event`: The event object to dispatch.

## See Also

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
- [func stop(Any?)](./stop%28_%29.md)
  Stops the main event loop.
- [func postEvent(NSEvent, atStart: Bool)](./postevent%28_,atstart%29.md)
  Adds a given event to the receiver’s event queue.
- [NSEventTrackingRunLoopMode](../nseventtrackingrunloopmode.md)
  The mode set when tracking events modally, such as a mouse-dragging loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/sendevent(_:))*