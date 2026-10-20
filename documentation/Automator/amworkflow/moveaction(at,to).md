# moveAction(at:to:)

**Framework**: Automator  
**Kind**: method  
**Role**: Instance Method

Moves the action from the specified start position to the specified end position in the receiving workflow.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
func moveAction(at startIndex: Int, to endIndex: Int)
```

```objc
- (void) moveActionAtIndex:(NSUInteger) startIndex toIndex:(NSUInteger) endIndex;
```

#### Discussion

If either index is invalid, this method does nothing.

## Parameters

- `startIndex`: The start position of the action to move.
- `endIndex`: The end position for the action that is moved.

## See Also

### Manipulating the Workflow’s Actions
- [func addAction(AMAction)](./addaction%28_%29.md)
  Adds the specified action at the end of the receiving workflow.
- [func insertAction(AMAction, at: Int)](./insertaction%28_,at%29.md)
  Inserts the specified action at the specified position of the receiving workflow.
- [func removeAction(AMAction)](./removeaction%28_%29.md)
  Removes the specified action from the workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflow/moveaction(at:to:))*