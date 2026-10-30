# currentEvent

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The last event object that the app retrieved from the event queue.

**Availability**:
- macOS

## Declaration

```swift
var currentEvent: NSEvent? { get }
```

```objc
@property (strong, readonly, nullable) NSEvent * currentEvent;
```

## Mentions

- [Adopting gesture recognizers in your app](../adopting-gesture-recognizers-in-your-app.md)

## Discussion

The shared app object receives events and forwards them to the affected [`NSWindow`](../nswindow.md) objects, which then distribute them to the objects in its view hierarchy. Use this property to get the event that was last handled by the app.

## See Also

### Managing the event loop
- [func nextEvent(matching: NSEvent.EventTypeMask, until: Date?, inMode: RunLoop.Mode, dequeue: Bool) -> NSEvent?](./nextevent%28matching,until,inmode,dequeue%29.md)
  Returns the next event matching a given mask, or `nil` if no such event is found before a specified expiration date.
- [func discardEvents(matching: NSEvent.EventTypeMask, before: NSEvent?)](./discardevents%28matching,before%29.md)
  Removes all events matching the given mask and generated before the specified event.
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
- [func postEvent(NSEvent, atStart: Bool)](./postevent%28_,atstart%29.md)
  Adds a given event to the receiver’s event queue.
- [NSEventTrackingRunLoopMode](../nseventtrackingrunloopmode.md)
  The mode set when tracking events modally, such as a mouse-dragging loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/currentevent)*