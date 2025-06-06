# needsUpdateConstraints

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the view’s constraints need to be updated.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var needsUpdateConstraints: Bool { get set }
```

#### Discussion

When a property of your view changes in a way that would impact constraints, set the value of this property to [`true`](https://developer.apple.com/documentation/swift/true) to indicate that the constraints need to be updated at some point in the future. The next time the layout process happens, the constraint-based layout system uses the value of this property to determine whether it needs to call [`updateConstraints()`](nsview/updateconstraints().md) on the view. Use this as an optimization tool to batch constraint changes. Updating constraints all at once just before they are needed ensures that you don’t needlessly recalculate constraints when multiple changes are made to your view in between layout passes.

## See Also

- [var needsLayout: Bool](nsview/needslayout.md)
  A Boolean value indicating whether the view needs a layout pass before it can be drawn.
- [func layout()](nsview/layout.md)
  Perform layout in concert with the constraint-based layout system.
- [func layoutSubtreeIfNeeded()](nsview/layoutsubtreeifneeded.md)
  Updates the layout of the receiving view and its subviews based on the current views and constraints.
- [func updateConstraints()](nsview/updateconstraints.md)
  Update constraints for the view.
- [func updateConstraintsForSubtreeIfNeeded()](nsview/updateconstraintsforsubtreeifneeded.md)
  Updates the constraints for the receiving view and its subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/needsupdateconstraints)*