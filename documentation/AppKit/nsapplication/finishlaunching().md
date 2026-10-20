# finishLaunching()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Activates the app, opens any files specified by the `NSOpen` user default, and unhighlights the app’s icon.

**Availability**:
- macOS

## Declaration

```swift
func finishLaunching()
```

```objc
- (void) finishLaunching;
```

#### Discussion

The [`run()`](./run%28%29.md) method calls this method before it starts the event loop. When this method begins, it posts an [`willFinishLaunchingNotification`](./willfinishlaunchingnotification.md) to the default notification center. If you override [`finishLaunching()`](./finishlaunching%28%29.md), the subclass method should invoke the superclass method.

## See Also

### Related Documentation
- [func applicationWillFinishLaunching(Notification)](../nsapplicationdelegate/applicationwillfinishlaunching%28_%29.md)
  Tells the delegate that the app’s initialization is about to complete.
- [func applicationDidFinishLaunching(Notification)](../nsapplicationdelegate/applicationdidfinishlaunching%28_%29.md)
  Tells the delegate that the app’s initialization is complete but it hasn’t received its first event.
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
- [func stop(Any?)](./stop%28_%29.md)
  Stops the main event loop.
- [func sendEvent(NSEvent)](./sendevent%28_%29.md)
  Dispatches an event to other objects.
- [func postEvent(NSEvent, atStart: Bool)](./postevent%28_,atstart%29.md)
  Adds a given event to the receiver’s event queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/finishlaunching())*