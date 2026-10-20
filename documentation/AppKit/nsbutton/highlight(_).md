# highlight(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Highlights (or unhighlights) the button.

**Availability**:
- macOS

## Declaration

```swift
func highlight(_ flag: Bool)
```

```objc
- (void) highlight:(BOOL) flag;
```

#### Discussion

Highlighting makes the button appear recessed, displays its alternate title or image, or causes the button to appear illuminated.

## Parameters

- `flag`: [`true`](../../Swift/true.md) to highlight the button; [`false`](../../Swift/false.md) to unhighlight the button.  If the current state of the button matches `flag`, no action is taken.

## See Also

### Related Documentation
- [func setButtonType(NSButton.ButtonType)](./setbuttontype%28_%29.md)
  Sets the button’s type, which affects its user interface and behavior when clicked.
### Managing button state
- [var allowsMixedState: Bool](./allowsmixedstate.md)
  A Boolean value that indicates whether the button allows a mixed state.
- [var state: NSControl.StateValue](./state.md)
  The button’s state.
- [func setNextState()](./setnextstate%28%29.md)
  Sets the button to its next state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/highlight(_:))*