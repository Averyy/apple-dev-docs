# run()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Starts the main event loop.

**Availability**:
- macOS

## Declaration

```swift
func run()
```

```objc
- (void) run;
```

#### Discussion

The loop continues until a [`stop(_:)`](./stop%28_%29.md) or [`terminate(_:)`](./terminate%28_%29.md) message is received. Upon each iteration through the loop, the next available event from the window server is stored and then dispatched by sending it to `NSApp` using [`sendEvent(_:)`](./sendevent%28_%29.md).

After creating the `NSApplication` object, the `main` function should load your app’s main nib file and then start the event loop by sending the `NSApplication` object a [`run()`](./run%28%29.md) message. If you create an Cocoa app project in Xcode, this `main` function is implemented for you.

## See Also

### Related Documentation
- [func runModalSession(NSApplication.ModalSession) -> NSApplication.ModalResponse](./runmodalsession%28_%29.md)
  Runs a given modal session, as defined in a previous invocation of [`beginModalSession(for:)`](./beginmodalsession%28for%29.md).
- [func runModal(for: NSWindow) -> NSApplication.ModalResponse](./runmodal%28for%29.md)
  Starts a modal event loop for the specified window.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/run())*