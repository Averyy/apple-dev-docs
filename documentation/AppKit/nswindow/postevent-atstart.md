# postEvent(_:atStart:)

**Framework**: AppKit  
**Kind**: method

Forwards the message to the global application object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func postEvent(_ event: NSEvent, atStart flag: Bool)
```

## Parameters

- `event`: The event to add to the window’s event queue.
- `flag`:   to place the event in the front of the queue;   to place it in the back.

## See Also

- [func postEvent(NSEvent, atStart: Bool)](nsapplication/postevent(_:atstart:).md)
  Adds a given event to the receiver’s event queue.
- [var currentEvent: NSEvent?](nswindow/currentevent.md)
  The event currently being processed by the application.
- [func nextEvent(matching: NSEvent.EventTypeMask) -> NSEvent?](nswindow/nextevent(matching:).md)
  Returns the next event matching a given mask.
- [func nextEvent(matching: NSEvent.EventTypeMask, until: Date?, inMode: RunLoop.Mode, dequeue: Bool) -> NSEvent?](nswindow/nextevent(matching:until:inmode:dequeue:).md)
  Forwards the message to the global application object.
- [func discardEvents(matching: NSEvent.EventTypeMask, before: NSEvent?)](nswindow/discardevents(matching:before:).md)
  Forwards the message to the global application object.
- [func sendEvent(NSEvent)](nswindow/sendevent(_:).md)
  This action method dispatches mouse and keyboard events the global application object sends to the window.
- [func tryToPerform(Selector, with: Any?) -> Bool](nswindow/trytoperform(_:with:).md)
  Dispatches action messages with a given argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/postevent(_:atstart:))*