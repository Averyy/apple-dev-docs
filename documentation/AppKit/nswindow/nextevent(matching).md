# nextEvent(matching:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the next event matching a given mask.

**Availability**:
- macOS

## Declaration

```swift
func nextEvent(matching mask: NSEvent.EventTypeMask) -> NSEvent?
```

```objc
- (NSEvent *) nextEventMatchingMask:(NSEventMask) mask;
```

#### Return Value

The next event whose mask matches `mask`; `nil` when no matching event was found.

#### Discussion

This method calls the [`nextEvent(matching:until:inMode:dequeue:)`](./nextevent%28matching,until,inmode,dequeue%29.md) method, where the matching mask parameter is the specified `mask`, the `until` (Swift) or `untilDate` (Objective-C) parameter is [`distantFuture`](../../Foundation/nsdate/distantfuture.md), the `inMode` parameter is [`NSEventTrackingRunLoopMode`](../nseventtrackingrunloopmode.md), and the `dequeue` parameter is [`true`](../../Swift/true.md).

## Parameters

- `mask`: The mask that the event to return must match. Events with non-matching masks are left in the queue. See [`discardEvents(matching:before:)`](../nsapplication/discardevents%28matching,before%29.md) in [`NSApplication`](../nsapplication.md) for the list of mask values.

## See Also

### Related Documentation
- [func nextEvent(matching: NSEvent.EventTypeMask, until: Date?, inMode: RunLoop.Mode, dequeue: Bool) -> NSEvent?](../nsapplication/nextevent%28matching,until,inmode,dequeue%29.md)
  Returns the next event matching a given mask, or `nil` if no such event is found before a specified expiration date.
### Handling Events
- [var currentEvent: NSEvent?](./currentevent.md)
  The event currently being processed by the application.
- [func nextEvent(matching: NSEvent.EventTypeMask, until: Date?, inMode: RunLoop.Mode, dequeue: Bool) -> NSEvent?](./nextevent%28matching,until,inmode,dequeue%29.md)
  Forwards the message to the global application object.
- [func discardEvents(matching: NSEvent.EventTypeMask, before: NSEvent?)](./discardevents%28matching,before%29.md)
  Forwards the message to the global application object.
- [func postEvent(NSEvent, atStart: Bool)](./postevent%28_,atstart%29.md)
  Forwards the message to the global application object.
- [func sendEvent(NSEvent)](./sendevent%28_%29.md)
  This action method dispatches mouse and keyboard events the global application object sends to the window.
- [func tryToPerform(Selector, with: Any?) -> Bool](./trytoperform%28_,with%29.md)
  Dispatches action messages with a given argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/nextevent(matching:))*