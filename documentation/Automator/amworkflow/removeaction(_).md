# removeAction(_:)

**Framework**: Automator  
**Kind**: method  
**Role**: Instance Method

Removes the specified action from the workflow.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
func removeAction(_ action: AMAction)
```

```objc
- (void) removeAction:(AMAction *) action;
```

## Discussion

The action receives an `AMAction closed` message before being released.

## Parameters

- `action`: The action to be removed.

## See Also

### Manipulating the Workflow’s Actions
- [func addAction(AMAction)](./addaction%28_%29.md)
  Adds the specified action at the end of the receiving workflow.
- [func insertAction(AMAction, at: Int)](./insertaction%28_,at%29.md)
  Inserts the specified action at the specified position of the receiving workflow.
- [func moveAction(at: Int, to: Int)](./moveaction%28at,to%29.md)
  Moves the action from the specified start position to the specified end position in the receiving workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflow/removeaction(_:))*