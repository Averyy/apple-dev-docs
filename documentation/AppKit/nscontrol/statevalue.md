# NSControl.StateValue

**Framework**: AppKit  
**Kind**: struct

A constant that indicates whether a control is on, off, or in a mixed state.

**Availability**:
- macOS ?+

## Declaration

```swift
struct StateValue
```

## Topics

### Setting a Control’s State
- [static let on: NSControl.StateValue](nscontrol/statevalue/on.md)
  A constant value that indicates a control is on or selected.
- [static let off: NSControl.StateValue](nscontrol/statevalue/off.md)
  A constant value that indicates a control is off or unselected.
- [static let mixed: NSControl.StateValue](nscontrol/statevalue/mixed.md)
  A constant value that indicates a control is in a mixed state, neither on nor off.
### Creating a State Value
- [init(Int)](nscontrol/statevalue/init(_:).md)
  Initializes a control state object.
- [init(rawValue: Int)](nscontrol/statevalue/init(rawvalue:).md)
  Initializes a state value from a raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var allowsMixedState: Bool](nscell/allowsmixedstate.md)
  A Boolean value indicating whether the cell supports three states instead of two.
- [var nextState: Int](nscell/nextstate.md)
  The cell’s next state.
- [func setNextState()](nscell/setnextstate.md)
  Changes cell’s state to the next value in the sequence.
- [var state: NSControl.StateValue](nscell/state.md)
  The cell’s current state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/statevalue)*