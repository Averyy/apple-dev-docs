# allowsMixedState

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the cell supports three states instead of two.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var allowsMixedState: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the cell supports three states: on, off, and mixed. When the value is [`false`](https://developer.apple.com/documentation/Swift/false), the cell supports only the on and off states.

## See Also

- [var nextState: Int](nscell/nextstate.md)
  The cell’s next state.
- [func setNextState()](nscell/setnextstate.md)
  Changes cell’s state to the next value in the sequence.
- [var state: NSControl.StateValue](nscell/state.md)
  The cell’s current state.
- [NSControl.StateValue](nscontrol/statevalue.md)
  A constant that indicates whether a control is on, off, or in a mixed state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/allowsmixedstate)*