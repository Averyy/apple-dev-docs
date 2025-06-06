# performClick(_:)

**Framework**: AppKit  
**Kind**: method

Simulates the user clicking the button with the pointer.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func performClick(_ sender: Any?)
```

#### Discussion

This method essentially highlights the button, sends the button’s action message to the target object, and then unhighlights the button.

If an exception is raised while the target object is processing the action message, the button is unhighlighted before the exception is propagated out of [`performClick(_:)`](nsbuttoncell/performclick(_:).md).

## Parameters

- `sender`: The sender of the message.

## See Also

- [func mouseEntered(with: NSEvent)](nsbuttoncell/mouseentered(with:).md)
  Draws the button’s border.
- [func mouseExited(with: NSEvent)](nsbuttoncell/mouseexited(with:).md)
  Erases the button’s border.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/performclick(_:))*