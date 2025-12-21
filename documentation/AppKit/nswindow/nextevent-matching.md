# nextEvent(matching:)

**Framework**: AppKit  
**Kind**: method

Returns the next event matching a given mask.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func nextEvent(matching mask: NSEvent.EventTypeMask) -> NSEvent?
```

#### Return Value

The next event whose mask matches `mask`; `nil` when no matching event was found.

#### Discussion

This method calls the [`nextEvent(matching:until:inMode:dequeue:)`](nswindow/nextevent(matching:until:inmode:dequeue:).md) method, where the matching mask parameter is the specified `mask`, the `until` (Swift) or `untilDate` (Objective-C) parameter is [`distantFuture`](https://developer.apple.com/documentation/Foundation/NSDate/distantFuture), the `inMode` parameter is [`NSEventTrackingRunLoopMode`](nseventtrackingrunloopmode.md), and the `dequeue` parameter is [`true`](https://developer.apple.com/documentation/Swift/true).

## Parameters

- `mask`: The mask that the event to return must match. Events with non-matching masks are left in the queue. See   in   for the list of mask values.

## See Also

- [func nextEvent(matching: NSEvent.EventTypeMask, until: Date?, inMode: RunLoop.Mode, dequeue: Bool) -> NSEvent?](nsapplication/nextevent(matching:until:inmode:dequeue:).md)
  Returns the next event matching a given mask, or `nil` if no such event is found before a specified expiration date.
- [var currentEvent: NSEvent?](nswindow/currentevent.md)
  The event currently being processed by the application.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/nextevent(matching:))*