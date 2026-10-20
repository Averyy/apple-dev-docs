# enableKeyEquivalentForDefaultButtonCell()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Reenables the default button cell’s key equivalent, so it performs a click when the user presses Return (or Enter).

**Availability**:
- macOS

## Declaration

```swift
func enableKeyEquivalentForDefaultButtonCell()
```

```objc
- (void) enableKeyEquivalentForDefaultButtonCell;
```

## See Also

### Managing Default Buttons
- [var defaultButtonCell: NSButtonCell?](./defaultbuttoncell.md)
  The button cell that performs as if clicked when the window receives a Return (or Enter) key event.
- [func disableKeyEquivalentForDefaultButtonCell()](./disablekeyequivalentfordefaultbuttoncell%28%29.md)
  Disables the default button cell’s key equivalent, so it doesn’t perform a click when the user presses Return (or Enter).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/enablekeyequivalentfordefaultbuttoncell())*