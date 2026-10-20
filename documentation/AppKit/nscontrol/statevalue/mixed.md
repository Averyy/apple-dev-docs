# mixed

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A constant value that indicates a control is in a mixed state, neither on nor off.

**Availability**:
- macOS

## Declaration

```swift
static var mixed: NSControl.StateValue { get }
```

```c
static const NSControlStateValue NSControlStateValueMixed;
```

#### Discussion

For example, if a checkbox displays the state of more than one selected row in a table and the items have different states, then the checkbox’s state is mixed.

## See Also

### Setting a Control’s State
- [static var on: NSControl.StateValue](./on.md)
  A constant value that indicates a control is on or selected.
- [static var off: NSControl.StateValue](./off.md)
  A constant value that indicates a control is off or unselected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/statevalue/mixed)*