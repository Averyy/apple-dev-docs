# addAction(_:)

**Framework**: Automator  
**Kind**: method  
**Role**: Instance Method

Adds the specified action at the end of the receiving workflow.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
func addAction(_ action: AMAction)
```

```objc
- (void) addAction:(AMAction *) action;
```

## Discussion

The workflow retains the action but does not copy it.

## Parameters

- `action`: The action to add.

## See Also

### Manipulating the Workflow’s Actions
- [func insertAction(AMAction, at: Int)](./insertaction%28_,at%29.md)
  Inserts the specified action at the specified position of the receiving workflow.
- [func moveAction(at: Int, to: Int)](./moveaction%28at,to%29.md)
  Moves the action from the specified start position to the specified end position in the receiving workflow.
- [func removeAction(AMAction)](./removeaction%28_%29.md)
  Removes the specified action from the workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflow/addaction(_:))*