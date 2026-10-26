# isRunning

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the main event loop is running.

**Availability**:
- macOS

## Declaration

```swift
var isRunning: Bool { get }
```

```objc
@property (readonly, getter=isRunning) BOOL running;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) when the main event loop is running or [`false`](../../Swift/false.md) when it’s not. Calling the [`stop(_:)`](./stop%28_%29.md) method sets the value to [`false`](../../Swift/false.md).

## See Also

### Related Documentation
- [func terminate(Any?)](./terminate%28_%29.md)
  Terminates the receiver.
### Managing the event loop
- [func nextEvent(matching: NSEvent.EventTypeMask, until: Date?, inMode: RunLoop.Mode, dequeue: Bool) -> NSEvent?](./nextevent%28matching,until,inmode,dequeue%29.md)
  Returns the next event matching a given mask, or `nil` if no such event is found before a specified expiration date.
- [func discardEvents(matching: NSEvent.EventTypeMask, before: NSEvent?)](./discardevents%28matching,before%29.md)
  Removes all events matching the given mask and generated before the specified event.
- [var currentEvent: NSEvent?](./currentevent.md)
  The last event object that the app retrieved from the event queue.
- [func run()](./run%28%29.md)
  Starts the main event loop.
- [func finishLaunching()](./finishlaunching%28%29.md)
  Activates the app, opens any files specified by the `NSOpen` user default, and unhighlights the app’s icon.
- [func stop(Any?)](./stop%28_%29.md)
  Stops the main event loop.
- [func sendEvent(NSEvent)](./sendevent%28_%29.md)
  Dispatches an event to other objects.
- [func postEvent(NSEvent, atStart: Bool)](./postevent%28_,atstart%29.md)
  Adds a given event to the receiver’s event queue.
- [NSEventTrackingRunLoopMode](../nseventtrackingrunloopmode.md)
  The mode set when tracking events modally, such as a mouse-dragging loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/isrunning)*