# sendEvent(_:)

**Framework**: AppKit  
**Kind**: method

This action method dispatches mouse and keyboard events the global application object sends to the window.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func sendEvent(_ event: NSEvent)
```

#### Discussion

Never invoke this method directly. A right mouse-down event in a window of an inactive application isn’t delivered to the corresponding `NSWindow` object. Instead, a [`sendEvent(_:)`](nsapplication/sendevent(_:).md) message with a window number of `0` delivers it to the NSApplication object.

## Parameters

- `event`: The mouse or keyboard event to process.

## See Also

- [var currentEvent: NSEvent?](nswindow/currentevent.md)
  The event currently being processed by the application.
- [func nextEvent(matching: NSEvent.EventTypeMask) -> NSEvent?](nswindow/nextevent(matching:).md)
  Returns the next event matching a given mask.
- [func nextEvent(matching: NSEvent.EventTypeMask, until: Date?, inMode: RunLoop.Mode, dequeue: Bool) -> NSEvent?](nswindow/nextevent(matching:until:inmode:dequeue:).md)
  Forwards the message to the global application object.
- [func discardEvents(matching: NSEvent.EventTypeMask, before: NSEvent?)](nswindow/discardevents(matching:before:).md)
  Forwards the message to the global application object.
- [func postEvent(NSEvent, atStart: Bool)](nswindow/postevent(_:atstart:).md)
  Forwards the message to the global application object.
- [func tryToPerform(Selector, with: Any?) -> Bool](nswindow/trytoperform(_:with:).md)
  Dispatches action messages with a given argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/sendevent(_:))*