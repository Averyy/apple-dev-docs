# insertAction(_:at:)

**Framework**: Automator  
**Kind**: method

Inserts the specified action at the specified position of the receiving workflow.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
func insertAction(_ action: AMAction, at index: Int)
```

#### Discussion

The workflow retains the action but does not copy it.

## Parameters

- `action`: The action to insert.
- `index`: The position in the receiver at which to insert the action. If the position is invalid, this method does nothing.

## See Also

- [func addAction(AMAction)](amworkflow/addaction(_:).md)
  Adds the specified action at the end of the receiving workflow.
- [func moveAction(at: Int, to: Int)](amworkflow/moveaction(at:to:).md)
  Moves the action from the specified start position to the specified end position in the receiving workflow.
- [func removeAction(AMAction)](amworkflow/removeaction(_:).md)
  Removes the specified action from the workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflow/insertaction(_:at:))*