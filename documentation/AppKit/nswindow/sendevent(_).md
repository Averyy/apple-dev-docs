# sendEvent(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

This action method dispatches mouse and keyboard events the global application object sends to the window.

**Availability**:
- macOS

## Declaration

```swift
func sendEvent(_ event: NSEvent)
```

```objc
- (void) sendEvent:(NSEvent *) event;
```

## Discussion

Never invoke this method directly. A right mouse-down event in a window of an inactive application isn’t delivered to the corresponding `NSWindow` object. Instead, a [`sendEvent(_:)`](../nsapplication/sendevent%28_%29.md) message with a window number of `0` delivers it to the NSApplication object.

## Parameters

- `event`: The mouse or keyboard event to process.

## See Also

### Handling Events
- [var currentEvent: NSEvent?](./currentevent.md)
  The event currently being processed by the application.
- [func nextEvent(matching: NSEvent.EventTypeMask) -> NSEvent?](./nextevent%28matching%29.md)
  Returns the next event matching a given mask.
- [func nextEvent(matching: NSEvent.EventTypeMask, until: Date?, inMode: RunLoop.Mode, dequeue: Bool) -> NSEvent?](./nextevent%28matching,until,inmode,dequeue%29.md)
  Forwards the message to the global application object.
- [func discardEvents(matching: NSEvent.EventTypeMask, before: NSEvent?)](./discardevents%28matching,before%29.md)
  Forwards the message to the global application object.
- [func postEvent(NSEvent, atStart: Bool)](./postevent%28_,atstart%29.md)
  Forwards the message to the global application object.
- [func tryToPerform(Selector, with: Any?) -> Bool](./trytoperform%28_,with%29.md)
  Dispatches action messages with a given argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/sendevent(_:))*