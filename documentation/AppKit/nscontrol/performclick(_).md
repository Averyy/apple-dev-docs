# performClick(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Simulates a single mouse click on the receiver.

**Availability**:
- macOS

## Declaration

```swift
func performClick(_ sender: Any?)
```

```objc
- (void) performClick:(id) sender;
```

## Discussion

This method calls the [`performClick(_:)`](../nscell/performclick%28_%29.md) method of the receiver’s cell with the sender being the control itself. This method raises an exception if the action message cannot be successfully sent.

## Parameters

- `sender`: The object requesting the action. This parameter is ignored.

## See Also

### Activating from the Keyboard
- [var refusesFirstResponder: Bool](./refusesfirstresponder.md)
  A Boolean value indicating whether the receiver refuses the first responder role.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/performclick(_:))*