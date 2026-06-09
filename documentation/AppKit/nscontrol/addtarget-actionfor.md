# addTarget(_:action:for:)

**Framework**: AppKit  
**Kind**: method

Registers a target-action pair for the specified control events.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func addTarget(_ target: Any?, action: Selector, for controlEvents: NSControl.Events)
```

#### Discussion

You can call this method multiple times to register additional target-action pairs for the same or different events. You can also register multiple targets or multiple actions for the same event. The control holds a weak reference to each registered target.

## Parameters

- `target`: The object to receive the action message. Pass `nil` to send the action up the responder chain.
- `action`: The selector to invoke on `target` when the specified events occur. This parameter can’t be `nil`. The selector may include the sender, the event, or both as parameters, in that order.
- `controlEvents`: A bit mask of [`NSControl.Events`](nscontrol/events.md) values specifying which events initiate the action.

## See Also

- [NSControl.Events](nscontrol/events.md)
  A set of events that a control can report to its target.
- [func removeTarget(Any?, action: Selector?, for: NSControl.Events)](nscontrol/removetarget(_:action:for:).md)
  Stops the delivery of events to the specified target object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/addtarget(_:action:for:))*