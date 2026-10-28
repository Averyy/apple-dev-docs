# postEvent(_:atStart:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds a given event to the receiver’s event queue.

**Availability**:
- macOS

## Declaration

```swift
func postEvent(_ event: NSEvent, atStart: Bool)
```

```objc
- (void) postEvent:(NSEvent *) event atStart:(BOOL) atStart;
```

## Discussion

This method can also be called in subthreads. Events posted in subthreads bubble up in the main thread event queue.

## Parameters

- `event`: The event object to post to the queue.
- `atStart`: Specify [`true`](../../Swift/true.md) to add the event to the front of the queue; otherwise, specify [`false`](../../Swift/false.md) to add the event to the back of the queue.

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
- [func sendEvent(NSEvent)](./sendevent%28_%29.md)
  Dispatches an event to other objects.
- [NSEventTrackingRunLoopMode](../nseventtrackingrunloopmode.md)
  The mode set when tracking events modally, such as a mouse-dragging loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/postevent(_:atstart:))*