# needsUpdateConstraints

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the view’s constraints need to be updated.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var needsUpdateConstraints: Bool { get set }
```

```objc
@property BOOL needsUpdateConstraints;
```

## Discussion

When a property of your view changes in a way that would impact constraints, set the value of this property to [`true`](../../Swift/true.md) to indicate that the constraints need to be updated at some point in the future. The next time the layout process happens, the constraint-based layout system uses the value of this property to determine whether it needs to call [`updateConstraints()`](./updateconstraints%28%29.md) on the view. Use this as an optimization tool to batch constraint changes. Updating constraints all at once just before they are needed ensures that you don’t needlessly recalculate constraints when multiple changes are made to your view in between layout passes.

## See Also

### Triggering Auto Layout
- [var needsLayout: Bool](./needslayout.md)
  A Boolean value indicating whether the view needs a layout pass before it can be drawn.
- [func layout()](./layout%28%29.md)
  Perform layout in concert with the constraint-based layout system.
- [func layoutSubtreeIfNeeded()](./layoutsubtreeifneeded%28%29.md)
  Updates the layout of the receiving view and its subviews based on the current views and constraints.
- [func updateConstraints()](./updateconstraints%28%29.md)
  Update constraints for the view.
- [func updateConstraintsForSubtreeIfNeeded()](./updateconstraintsforsubtreeifneeded%28%29.md)
  Updates the constraints for the receiving view and its subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/needsupdateconstraints)*