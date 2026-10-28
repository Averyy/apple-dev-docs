# nextEvent(matching:until:inMode:dequeue:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Forwards the message to the global application object.

**Availability**:
- macOS

## Declaration

```swift
func nextEvent(matching mask: NSEvent.EventTypeMask, until expiration: Date?, inMode mode: RunLoop.Mode, dequeue deqFlag: Bool) -> NSEvent?
```

```objc
- (NSEvent *) nextEventMatchingMask:(NSEventMask) mask untilDate:(NSDate *) expiration inMode:(NSRunLoopMode) mode dequeue:(BOOL) deqFlag;
```

## Return Value

The next event whose mask matches the specified `mask`; otherwise, `nil`.

## Parameters

- `mask`: The mask that the event to return must match.
- `expiration`: The date until which to wait for events.
- `mode`: The run loop mode to use while waiting for events
- `deqFlag`: [`true`](../../Swift/true.md) to remove the returned event from the event queue; [`false`](../../Swift/false.md) to leave the returned event in the queue.

## See Also

### Related Documentation
- [func nextEvent(matching: NSEvent.EventTypeMask, until: Date?, inMode: RunLoop.Mode, dequeue: Bool) -> NSEvent?](../nsapplication/nextevent%28matching,until,inmode,dequeue%29.md)
  Returns the next event matching a given mask, or `nil` if no such event is found before a specified expiration date.
### Handling Events
- [var currentEvent: NSEvent?](./currentevent.md)
  The event currently being processed by the application.
- [func nextEvent(matching: NSEvent.EventTypeMask) -> NSEvent?](./nextevent%28matching%29.md)
  Returns the next event matching a given mask.
- [func discardEvents(matching: NSEvent.EventTypeMask, before: NSEvent?)](./discardevents%28matching,before%29.md)
  Forwards the message to the global application object.
- [func postEvent(NSEvent, atStart: Bool)](./postevent%28_,atstart%29.md)
  Forwards the message to the global application object.
- [func sendEvent(NSEvent)](./sendevent%28_%29.md)
  This action method dispatches mouse and keyboard events the global application object sends to the window.
- [func tryToPerform(Selector, with: Any?) -> Bool](./trytoperform%28_,with%29.md)
  Dispatches action messages with a given argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/nextevent(matching:until:inmode:dequeue:))*