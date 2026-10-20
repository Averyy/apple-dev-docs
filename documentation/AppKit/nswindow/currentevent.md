# currentEvent

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The event currently being processed by the application.

**Availability**:
- macOS

## Declaration

```swift
var currentEvent: NSEvent? { get }
```

```objc
@property (strong, readonly, nullable) NSEvent * currentEvent;
```

#### Discussion

The value of this property is given by calling by invoking the [`NSApplication`](../nsapplication.md) method [`currentEvent`](../nsapplication/currentevent.md).

## See Also

### Handling Events
- [func nextEvent(matching: NSEvent.EventTypeMask) -> NSEvent?](./nextevent%28matching%29.md)
  Returns the next event matching a given mask.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/currentevent)*