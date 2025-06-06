# setNextState()

**Framework**: AppKit  
**Kind**: method

Sets the button to its next state.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setNextState()
```

#### Discussion

If the button has three states, it cycles through them in this order: on, off, mixed, on, and so forth. If the button has two states, it toggles between them.

## See Also

- [var allowsMixedState: Bool](nsbutton/allowsmixedstate.md)
  A Boolean value that indicates whether the button allows a mixed state.
- [var state: NSControl.StateValue](nsbutton/state.md)
  The button’s state.
- [func highlight(Bool)](nsbutton/highlight(_:).md)
  Highlights (or unhighlights) the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/setnextstate())*