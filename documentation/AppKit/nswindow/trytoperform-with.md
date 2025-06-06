# tryToPerform(_:with:)

**Framework**: AppKit  
**Kind**: method

Dispatches action messages with a given argument.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func tryToPerform(_ action: Selector, with object: Any?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) when the window or its delegate perform `action` with `object`; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The window tries to perform the method `action` using its inherited `NSResponder` method [`tryToPerform(_:with:)`](nsresponder/trytoperform(_:with:).md). If the window doesn’t perform `action`, the delegate is given the opportunity to perform it using its inherited `NSObject` method [`perform(_:with:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/perform(_:with:)).

## Parameters

- `action`: The selector to attempt to execute.
- `object`: The message’s argument.

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
- [func sendEvent(NSEvent)](nswindow/sendevent(_:).md)
  This action method dispatches mouse and keyboard events the global application object sends to the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/trytoperform(_:with:))*