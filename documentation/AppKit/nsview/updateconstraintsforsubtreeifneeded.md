# updateConstraintsForSubtreeIfNeeded()

**Framework**: AppKit  
**Kind**: method

Updates the constraints for the receiving view and its subviews.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func updateConstraintsForSubtreeIfNeeded()
```

#### Discussion

Whenever a new layout pass is triggered for a view, the system invokes this method to ensure that any constraints for the view and its subviews are updated with information from the current view hierarchy and its constraints. This method is called automatically by the system, but may be invoked manually if you need to examine the most up to date constraints.

Subclasses should not override this method.

## See Also

- [var needsLayout: Bool](nsview/needslayout.md)
  A Boolean value indicating whether the view needs a layout pass before it can be drawn.
- [func layout()](nsview/layout.md)
  Perform layout in concert with the constraint-based layout system.
- [func layoutSubtreeIfNeeded()](nsview/layoutsubtreeifneeded.md)
  Updates the layout of the receiving view and its subviews based on the current views and constraints.
- [var needsUpdateConstraints: Bool](nsview/needsupdateconstraints.md)
  A Boolean value indicating whether the view’s constraints need to be updated.
- [func updateConstraints()](nsview/updateconstraints.md)
  Update constraints for the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/updateconstraintsforsubtreeifneeded())*