# performClick(_:)

**Framework**: AppKit  
**Kind**: method

Simulates a single mouse click on the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func performClick(_ sender: Any?)
```

#### Discussion

This method calls the [`performClick(_:)`](nscell/performclick(_:).md) method of the receiver’s cell with the sender being the control itself. This method raises an exception if the action message cannot be successfully sent.

## Parameters

- `sender`: The object requesting the action. This parameter is ignored.

## See Also

- [var refusesFirstResponder: Bool](nscontrol/refusesfirstresponder.md)
  A Boolean value indicating whether the receiver refuses the first responder role.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/performclick(_:))*