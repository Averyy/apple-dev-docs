# addAction(_:)

**Framework**: Automator  
**Kind**: method

Adds the specified action at the end of the receiving workflow.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
func addAction(_ action: AMAction)
```

#### Discussion

The workflow retains the action but does not copy it.

## Parameters

- `action`: The action to add.

## See Also

- [func insertAction(AMAction, at: Int)](amworkflow/insertaction(_:at:).md)
  Inserts the specified action at the specified position of the receiving workflow.
- [func moveAction(at: Int, to: Int)](amworkflow/moveaction(at:to:).md)
  Moves the action from the specified start position to the specified end position in the receiving workflow.
- [func removeAction(AMAction)](amworkflow/removeaction(_:).md)
  Removes the specified action from the workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflow/addaction(_:))*