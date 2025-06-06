# discardEvents(matching:before:)

**Framework**: AppKit  
**Kind**: method

Forwards the message to the global application object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func discardEvents(matching mask: NSEvent.EventTypeMask, before lastEvent: NSEvent?)
```

## Parameters

- `mask`: The mask of the events to discard.
- `lastEvent`: The event up to which queued events are discarded from the queue.

## See Also

- [var currentEvent: NSEvent?](nswindow/currentevent.md)
  The event currently being processed by the application.
- [func nextEvent(matching: NSEvent.EventTypeMask) -> NSEvent?](nswindow/nextevent(matching:).md)
  Returns the next event matching a given mask.
- [func nextEvent(matching: NSEvent.EventTypeMask, until: Date?, inMode: RunLoop.Mode, dequeue: Bool) -> NSEvent?](nswindow/nextevent(matching:until:inmode:dequeue:).md)
  Forwards the message to the global application object.
- [func postEvent(NSEvent, atStart: Bool)](nswindow/postevent(_:atstart:).md)
  Forwards the message to the global application object.
- [func sendEvent(NSEvent)](nswindow/sendevent(_:).md)
  This action method dispatches mouse and keyboard events the global application object sends to the window.
- [func tryToPerform(Selector, with: Any?) -> Bool](nswindow/trytoperform(_:with:).md)
  Dispatches action messages with a given argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/discardevents(matching:before:))*