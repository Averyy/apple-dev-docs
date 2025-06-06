# setNextState()

**Framework**: AppKit  
**Kind**: method

Changes cell’s state to the next value in the sequence.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setNextState()
```

#### Discussion

If a cell has three states, it cycles in this order: on, off, mixed, on, off, and so forth. If the cell has only two states, it toggles between them.

## See Also

- [var allowsMixedState: Bool](nscell/allowsmixedstate.md)
  A Boolean value indicating whether the cell supports three states instead of two.
- [var nextState: Int](nscell/nextstate.md)
  The cell’s next state.
- [var state: NSControl.StateValue](nscell/state.md)
  The cell’s current state.
- [NSControl.StateValue](nscontrol/statevalue.md)
  A constant that indicates whether a control is on, off, or in a mixed state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/setnextstate())*