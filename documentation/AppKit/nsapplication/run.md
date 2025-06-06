# run()

**Framework**: AppKit  
**Kind**: method

Starts the main event loop.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func run()
```

#### Discussion

The loop continues until a [`stop(_:)`](nsapplication/stop(_:).md) or [`terminate(_:)`](nsapplication/terminate(_:).md) message is received. Upon each iteration through the loop, the next available event from the window server is stored and then dispatched by sending it to `NSApp` using [`sendEvent(_:)`](nsapplication/sendevent(_:).md).

After creating the `NSApplication` object, the `main` function should load your app’s main nib file and then start the event loop by sending the `NSApplication` object a [`run()`](nsapplication/run().md) message. If you create an Cocoa app project in Xcode, this `main` function is implemented for you.

## See Also

- [func runModalSession(NSApplication.ModalSession) -> NSApplication.ModalResponse](nsapplication/runmodalsession(_:).md)
  Runs a given modal session, as defined in a previous invocation of [`beginModalSession(for:)`](nsapplication/beginmodalsession(for:).md).
- [func runModal(for: NSWindow) -> NSApplication.ModalResponse](nsapplication/runmodal(for:).md)
  Starts a modal event loop for the specified window.
- [func applicationDidFinishLaunching(Notification)](nsapplicationdelegate/applicationdidfinishlaunching(_:).md)
  Tells the delegate that the app’s initialization is complete but it hasn’t received its first event.
- [func nextEvent(matching: NSEvent.EventTypeMask, until: Date?, inMode: RunLoop.Mode, dequeue: Bool) -> NSEvent?](nsapplication/nextevent(matching:until:inmode:dequeue:).md)
  Returns the next event matching a given mask, or `nil` if no such event is found before a specified expiration date.
- [func discardEvents(matching: NSEvent.EventTypeMask, before: NSEvent?)](nsapplication/discardevents(matching:before:).md)
  Removes all events matching the given mask and generated before the specified event.
- [var currentEvent: NSEvent?](nsapplication/currentevent.md)
  The last event object that the app retrieved from the event queue.
- [var isRunning: Bool](nsapplication/isrunning.md)
  A Boolean value indicating whether the main event loop is running.
- [func finishLaunching()](nsapplication/finishlaunching.md)
  Activates the app, opens any files specified by the `NSOpen` user default, and unhighlights the app’s icon.
- [func stop(Any?)](nsapplication/stop(_:).md)
  Stops the main event loop.
- [func sendEvent(NSEvent)](nsapplication/sendevent(_:).md)
  Dispatches an event to other objects.
- [func postEvent(NSEvent, atStart: Bool)](nsapplication/postevent(_:atstart:).md)
  Adds a given event to the receiver’s event queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/run())*