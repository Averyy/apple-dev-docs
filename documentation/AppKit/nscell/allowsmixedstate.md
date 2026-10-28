# allowsMixedState

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the cell supports three states instead of two.

**Availability**:
- macOS

## Declaration

```swift
var allowsMixedState: Bool { get set }
```

```objc
@property BOOL allowsMixedState;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the cell supports three states: on, off, and mixed. When the value is [`false`](../../Swift/false.md), the cell supports only the on and off states.

## See Also

### Managing Cell State
- [var nextState: Int](./nextstate.md)
  The cell’s next state.
- [func setNextState()](./setnextstate%28%29.md)
  Changes cell’s state to the next value in the sequence.
- [var state: NSControl.StateValue](./state.md)
  The cell’s current state.
- [NSControl.StateValue](../nscontrol/statevalue.md)
  A constant that indicates whether a control is on, off, or in a mixed state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/allowsmixedstate)*