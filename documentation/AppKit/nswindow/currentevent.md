# currentEvent

**Framework**: AppKit  
**Kind**: property

The event currently being processed by the application.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var currentEvent: NSEvent? { get }
```

#### Discussion

The value of this property is given by calling by invoking the [`NSApplication`](nsapplication.md) method [`currentEvent`](nsapplication/currentevent.md).

## See Also

- [func nextEvent(matching: NSEvent.EventTypeMask) -> NSEvent?](nswindow/nextevent(matching:).md)
  Returns the next event matching a given mask.
- [func nextEvent(matching: NSEvent.EventTypeMask, until: Date?, inMode: RunLoop.Mode, dequeue: Bool) -> NSEvent?](nswindow/nextevent(matching:until:inmode:dequeue:).md)
  Forwards the message to the global application object.
- [func discardEvents(matching: NSEvent.EventTypeMask, before: NSEvent?)](nswindow/discardevents(matching:before:).md)
  Forwards the message to the global application object.
- [func postEvent(NSEvent, atStart: Bool)](nswindow/postevent(_:atstart:).md)
  Forwards the message to the global application object.
- [func sendEvent(NSEvent)](nswindow/sendevent(_:).md)
  This action method dispatches mouse and keyboard events the global application object sends to the window.
- [func tryToPerform(Selector, with: Any?) -> Bool](nswindow/trytoperform(_:with:).md)
  Dispatches action messages with a given argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/currentevent)*