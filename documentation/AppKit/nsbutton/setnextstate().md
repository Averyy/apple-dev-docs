# setNextState()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the button to its next state.

**Availability**:
- macOS

## Declaration

```swift
func setNextState()
```

```objc
- (void) setNextState;
```

#### Discussion

If the button has three states, it cycles through them in this order: on, off, mixed, on, and so forth. If the button has two states, it toggles between them.

## See Also

### Managing button state
- [var allowsMixedState: Bool](./allowsmixedstate.md)
  A Boolean value that indicates whether the button allows a mixed state.
- [var state: NSControl.StateValue](./state.md)
  The button’s state.
- [func highlight(Bool)](./highlight%28_%29.md)
  Highlights (or unhighlights) the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/setnextstate())*