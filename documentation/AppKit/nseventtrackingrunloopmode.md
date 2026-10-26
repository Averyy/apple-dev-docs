# NSEventTrackingRunLoopMode

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

The mode set when tracking events modally, such as a mouse-dragging loop.

**Availability**:
- macOS

## Declaration

```c
extern NSRunLoopMode NSEventTrackingRunLoopMode;
```

## See Also

### Managing the event loop
- [func nextEvent(matching: NSEvent.EventTypeMask, until: Date?, inMode: RunLoop.Mode, dequeue: Bool) -> NSEvent?](./nsapplication/nextevent%28matching,until,inmode,dequeue%29.md)
  Returns the next event matching a given mask, or `nil` if no such event is found before a specified expiration date.
- [func discardEvents(matching: NSEvent.EventTypeMask, before: NSEvent?)](./nsapplication/discardevents%28matching,before%29.md)
  Removes all events matching the given mask and generated before the specified event.
- [var currentEvent: NSEvent?](./nsapplication/currentevent.md)
  The last event object that the app retrieved from the event queue.
- [var isRunning: Bool](./nsapplication/isrunning.md)
  A Boolean value indicating whether the main event loop is running.
- [func run()](./nsapplication/run%28%29.md)
  Starts the main event loop.
- [func finishLaunching()](./nsapplication/finishlaunching%28%29.md)
  Activates the app, opens any files specified by the `NSOpen` user default, and unhighlights the app’s icon.
- [func stop(Any?)](./nsapplication/stop%28_%29.md)
  Stops the main event loop.
- [func sendEvent(NSEvent)](./nsapplication/sendevent%28_%29.md)
  Dispatches an event to other objects.
- [func postEvent(NSEvent, atStart: Bool)](./nsapplication/postevent%28_,atstart%29.md)
  Adds a given event to the receiver’s event queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nseventtrackingrunloopmode)*