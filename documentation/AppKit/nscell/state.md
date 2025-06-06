# state

**Framework**: AppKit  
**Kind**: property

The cell’s current state.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var state: NSControl.StateValue { get set }
```

#### Discussion

The [`NSOffState`](nsoffstate.md) state indicates the normal or unpressed state. The [`NSOnState`](nsonstate.md) state indicates the alternate or pressed state. The [`NSMixedState`](nsmixedstate.md) state indicates that the feature represented by the control is in effect somewhere.

Although using the enumerated constants is preferred, you can also assign an integer value to this property. If the cell has two states, `0` is treated as [`NSOffState`](nsoffstate.md), and a nonzero value is treated as [`NSOnState`](nsonstate.md). If the cell has three states, `0` is treated as [`NSOffState`](nsoffstate.md), a negative value is treated as `NSMixedState`, and a positive value is treated as [`NSOnState`](nsonstate.md).

## See Also

- [var allowsMixedState: Bool](nscell/allowsmixedstate.md)
  A Boolean value indicating whether the cell supports three states instead of two.
- [var nextState: Int](nscell/nextstate.md)
  The cell’s next state.
- [func setNextState()](nscell/setnextstate.md)
  Changes cell’s state to the next value in the sequence.
- [NSControl.StateValue](nscontrol/statevalue.md)
  A constant that indicates whether a control is on, off, or in a mixed state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/state)*