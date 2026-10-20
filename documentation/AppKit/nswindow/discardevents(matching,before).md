# discardEvents(matching:before:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Forwards the message to the global application object.

**Availability**:
- macOS

## Declaration

```swift
func discardEvents(matching mask: NSEvent.EventTypeMask, before lastEvent: NSEvent?)
```

```objc
- (void) discardEventsMatchingMask:(NSEventMask) mask beforeEvent:(NSEvent *) lastEvent;
```

## Parameters

- `mask`: The mask of the events to discard.
- `lastEvent`: The event up to which queued events are discarded from the queue.

## See Also

### Handling Events
- [var currentEvent: NSEvent?](./currentevent.md)
  The event currently being processed by the application.
- [func nextEvent(matching: NSEvent.EventTypeMask) -> NSEvent?](./nextevent%28matching%29.md)
  Returns the next event matching a given mask.
- [func nextEvent(matching: NSEvent.EventTypeMask, until: Date?, inMode: RunLoop.Mode, dequeue: Bool) -> NSEvent?](./nextevent%28matching,until,inmode,dequeue%29.md)
  Forwards the message to the global application object.
- [func postEvent(NSEvent, atStart: Bool)](./postevent%28_,atstart%29.md)
  Forwards the message to the global application object.
- [func sendEvent(NSEvent)](./sendevent%28_%29.md)
  This action method dispatches mouse and keyboard events the global application object sends to the window.
- [func tryToPerform(Selector, with: Any?) -> Bool](./trytoperform%28_,with%29.md)
  Dispatches action messages with a given argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/discardevents(matching:before:))*