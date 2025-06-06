# highlight(_:)

**Framework**: AppKit  
**Kind**: method

Highlights (or unhighlights) the button.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func highlight(_ flag: Bool)
```

#### Discussion

Highlighting makes the button appear recessed, displays its alternate title or image, or causes the button to appear illuminated.

## Parameters

- `flag`:   to highlight the button;   to unhighlight the button.  If the current state of the button matches  , no action is taken.

## See Also

- [func setButtonType(NSButton.ButtonType)](nsbutton/setbuttontype(_:).md)
  Sets the button’s type, which affects its user interface and behavior when clicked.
- [var allowsMixedState: Bool](nsbutton/allowsmixedstate.md)
  A Boolean value that indicates whether the button allows a mixed state.
- [var state: NSControl.StateValue](nsbutton/state.md)
  The button’s state.
- [func setNextState()](nsbutton/setnextstate.md)
  Sets the button to its next state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/highlight(_:))*