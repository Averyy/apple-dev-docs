# NSControl.StateValue

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

A constant that indicates whether a control is on, off, or in a mixed state.

**Availability**:
- macOS

## Declaration

```swift
struct StateValue
```

```c
typedef NSInteger NSControlStateValue;
```

## Topics

### Setting a Control’s State
- [static var on: NSControl.StateValue](./statevalue/on.md)
  A constant value that indicates a control is on or selected.
- [static var off: NSControl.StateValue](./statevalue/off.md)
  A constant value that indicates a control is off or unselected.
- [static var mixed: NSControl.StateValue](./statevalue/mixed.md)
  A constant value that indicates a control is in a mixed state, neither on nor off.
### Creating a State Value
- [init(Int)](./statevalue/init%28_%29.md)
  Initializes a control state object.
- [init(rawValue: Int)](./statevalue/init%28rawvalue%29.md)
  Initializes a state value from a raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing Cell State
- [var allowsMixedState: Bool](../nscell/allowsmixedstate.md)
  A Boolean value indicating whether the cell supports three states instead of two.
- [var nextState: Int](../nscell/nextstate.md)
  The cell’s next state.
- [func setNextState()](../nscell/setnextstate%28%29.md)
  Changes cell’s state to the next value in the sequence.
- [var state: NSControl.StateValue](../nscell/state.md)
  The cell’s current state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/statevalue)*