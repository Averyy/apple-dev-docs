# action

**Framework**: AppKit  
**Kind**: property

The default action-message selector associated with the control.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var action: Selector? { get set }
```

#### Discussion

This property contains the action message selector of the receiver’s cell. Controls that support multiple cells (such as `NSMatrix` and `NSForm`) must supply the appropriate action-message selector in this property. Specify `NULL` to prevent action messages from being sent to the receiver’s target.

If you want the action-message selector for a control that has multiple cells, it is better to get the selector directly from the cell’s own `action` property.

## See Also

- [var target: AnyObject?](nscontrol/target.md)
  The target object that receives action messages from the cell.
- [var isContinuous: Bool](nscontrol/iscontinuous.md)
  A Boolean value indicating whether the receiver’s cell sends its action message continuously to its target during mouse tracking.
- [func sendAction(Selector?, to: Any?) -> Bool](nscontrol/sendaction(_:to:).md)
  Causes the specified action to be sent to the target.
- [func sendAction(on: NSEvent.EventTypeMask) -> Int](nscontrol/sendaction(on:).md)
  Sets the conditions on which the receiver sends action messages to its target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/action)*