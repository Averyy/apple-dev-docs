# tryToPerform(_:with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Dispatches action messages with a given argument.

**Availability**:
- macOS

## Declaration

```swift
func tryToPerform(_ action: Selector, with object: Any?) -> Bool
```

```objc
- (BOOL) tryToPerform:(SEL) action with:(id) object;
```

#### Return Value

[`true`](../../Swift/true.md) when the window or its delegate perform `action` with `object`; otherwise, [`false`](../../Swift/false.md).

#### Discussion

The window tries to perform the method `action` using its inherited `NSResponder` method [`tryToPerform(_:with:)`](../nsresponder/trytoperform%28_,with%29.md). If the window doesn’t perform `action`, the delegate is given the opportunity to perform it using its inherited `NSObject` method [`perform(_:with:)`](../../ObjectiveC/nsobjectprotocol/perform%28_,with%29.md).

## Parameters

- `action`: The selector to attempt to execute.
- `object`: The message’s argument.

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
- [func sendEvent(NSEvent)](./sendevent%28_%29.md)
  This action method dispatches mouse and keyboard events the global application object sends to the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/trytoperform(_:with:))*