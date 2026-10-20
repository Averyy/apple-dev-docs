# postEvent(_:atStart:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Forwards the message to the global application object.

**Availability**:
- macOS

## Declaration

```swift
func postEvent(_ event: NSEvent, atStart flag: Bool)
```

```objc
- (void) postEvent:(NSEvent *) event atStart:(BOOL) flag;
```

## Parameters

- `event`: The event to add to the window’s event queue.
- `flag`: [`true`](../../Swift/true.md) to place the event in the front of the queue; [`false`](../../Swift/false.md) to place it in the back.

## See Also

### Related Documentation
- [func postEvent(NSEvent, atStart: Bool)](../nsapplication/postevent%28_,atstart%29.md)
  Adds a given event to the receiver’s event queue.
### Handling Events
- [var currentEvent: NSEvent?](./currentevent.md)
  The event currently being processed by the application.
- [func nextEvent(matching: NSEvent.EventTypeMask) -> NSEvent?](./nextevent%28matching%29.md)
  Returns the next event matching a given mask.
- [func nextEvent(matching: NSEvent.EventTypeMask, until: Date?, inMode: RunLoop.Mode, dequeue: Bool) -> NSEvent?](./nextevent%28matching,until,inmode,dequeue%29.md)
  Forwards the message to the global application object.
- [func discardEvents(matching: NSEvent.EventTypeMask, before: NSEvent?)](./discardevents%28matching,before%29.md)
  Forwards the message to the global application object.
- [func sendEvent(NSEvent)](./sendevent%28_%29.md)
  This action method dispatches mouse and keyboard events the global application object sends to the window.
- [func tryToPerform(Selector, with: Any?) -> Bool](./trytoperform%28_,with%29.md)
  Dispatches action messages with a given argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/postevent(_:atstart:))*