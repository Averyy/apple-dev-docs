# updateConstraintsForSubtreeIfNeeded()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Updates the constraints for the receiving view and its subviews.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func updateConstraintsForSubtreeIfNeeded()
```

```objc
- (void) updateConstraintsForSubtreeIfNeeded;
```

#### Discussion

Whenever a new layout pass is triggered for a view, the system invokes this method to ensure that any constraints for the view and its subviews are updated with information from the current view hierarchy and its constraints. This method is called automatically by the system, but may be invoked manually if you need to examine the most up to date constraints.

Subclasses should not override this method.

## See Also

### Triggering Auto Layout
- [var needsLayout: Bool](./needslayout.md)
  A Boolean value indicating whether the view needs a layout pass before it can be drawn.
- [func layout()](./layout%28%29.md)
  Perform layout in concert with the constraint-based layout system.
- [func layoutSubtreeIfNeeded()](./layoutsubtreeifneeded%28%29.md)
  Updates the layout of the receiving view and its subviews based on the current views and constraints.
- [var needsUpdateConstraints: Bool](./needsupdateconstraints.md)
  A Boolean value indicating whether the view’s constraints need to be updated.
- [func updateConstraints()](./updateconstraints%28%29.md)
  Update constraints for the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/updateconstraintsforsubtreeifneeded())*