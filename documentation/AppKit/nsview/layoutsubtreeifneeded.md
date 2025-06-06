# layoutSubtreeIfNeeded()

**Framework**: AppKit  
**Kind**: method

Updates the layout of the receiving view and its subviews based on the current views and constraints.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func layoutSubtreeIfNeeded()
```

#### Discussion

Before displaying a view that uses constraints-based layout the system invokes this method to ensure that the layout of the view and its subviews is up to date. This method updates the layout if needed, first invoking [`updateConstraintsForSubtreeIfNeeded()`](nsview/updateconstraintsforsubtreeifneeded().md) to ensure that all constraints are up to date. This method is called automatically by the system, but may be invoked manually if you need to examine the most up to date layout.

Subclasses should not override this method.

## See Also

- [var needsLayout: Bool](nsview/needslayout.md)
  A Boolean value indicating whether the view needs a layout pass before it can be drawn.
- [func layout()](nsview/layout.md)
  Perform layout in concert with the constraint-based layout system.
- [var needsUpdateConstraints: Bool](nsview/needsupdateconstraints.md)
  A Boolean value indicating whether the view’s constraints need to be updated.
- [func updateConstraints()](nsview/updateconstraints.md)
  Update constraints for the view.
- [func updateConstraintsForSubtreeIfNeeded()](nsview/updateconstraintsforsubtreeifneeded.md)
  Updates the constraints for the receiving view and its subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/layoutsubtreeifneeded())*