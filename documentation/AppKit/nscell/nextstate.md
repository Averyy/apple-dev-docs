# nextState

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The cell’s next state.

**Availability**:
- macOS

## Declaration

```swift
var nextState: Int { get }
```

```objc
@property (readonly) NSInteger nextState;
```

#### Discussion

If a cell has three states, it cycles in this order: on, off, mixed, on, off, and so forth. If the cell has only two states, it toggles between them.

For a list of constants representing the possible cell states, see [`NSCell.StateValue`](./statevalue.md).

## See Also

### Managing Cell State
- [var allowsMixedState: Bool](./allowsmixedstate.md)
  A Boolean value indicating whether the cell supports three states instead of two.
- [func setNextState()](./setnextstate%28%29.md)
  Changes cell’s state to the next value in the sequence.
- [var state: NSControl.StateValue](./state.md)
  The cell’s current state.
- [NSControl.StateValue](../nscontrol/statevalue.md)
  A constant that indicates whether a control is on, off, or in a mixed state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/nextstate)*