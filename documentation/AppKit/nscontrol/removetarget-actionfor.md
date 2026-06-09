# removeTarget(_:action:for:)

**Framework**: AppKit  
**Kind**: method

Stops the delivery of events to the specified target object.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func removeTarget(_ target: Any?, action: Selector?, for controlEvents: NSControl.Events)
```

#### Discussion

Use this method to prevent the delivery of control events to a target object. If you specify a valid object in the `target` parameter, this method stops the delivery of the specified events to all action methods associated with that object. If you specify `nil` for the `target` parameter, this method prevents the delivery of those events to all action methods of all target objects.

## Parameters

- `target`: A target object registered with the control. Specify `nil` to remove the specified control events for all target objects.
- `action`: A selector identifying a registered action method. You may specify `nil` for this parameter.
- `controlEvents`: A bit mask specifying the control events to remove for the specified `target` object. For a list of possible constants, see [`NSControl.Events`](nscontrol/events.md).

## See Also

- [NSControl.Events](nscontrol/events.md)
  A set of events that a control can report to its target.
- [func addTarget(Any?, action: Selector, for: NSControl.Events)](nscontrol/addtarget(_:action:for:).md)
  Registers a target-action pair for the specified control events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/removetarget(_:action:for:))*