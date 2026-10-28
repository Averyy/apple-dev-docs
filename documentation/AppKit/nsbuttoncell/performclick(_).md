# performClick(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Simulates the user clicking the button with the pointer.

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

This method essentially highlights the button, sends the button’s action message to the target object, and then unhighlights the button.

If an exception is raised while the target object is processing the action message, the button is unhighlighted before the exception is propagated out of [`performClick(_:)`](./performclick%28_%29.md).

## Parameters

- `sender`: The sender of the message.

## See Also

### Handling Events and Action Messages
- [func mouseEntered(with: NSEvent)](./mouseentered%28with%29.md)
  Draws the button’s border.
- [func mouseExited(with: NSEvent)](./mouseexited%28with%29.md)
  Erases the button’s border.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/performclick(_:))*