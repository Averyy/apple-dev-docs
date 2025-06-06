# needsLayout

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the view needs a layout pass before it can be drawn.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var needsLayout: Bool { get set }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the view needs a layout pass, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

You only ever need to change the value of this property if your view implements the [`layout()`](nsview/layout().md) method because it has custom layout that is not expressible in the constraint-based layout system. Setting this property to [`true`](https://developer.apple.com/documentation/swift/true) lets the system know that the view’s layout needs to be updated before it is drawn. The system checks the value of this property prior to applying constraint-based layout rules for the view.

## See Also

- [func layout()](nsview/layout.md)
  Perform layout in concert with the constraint-based layout system.
- [func layoutSubtreeIfNeeded()](nsview/layoutsubtreeifneeded.md)
  Updates the layout of the receiving view and its subviews based on the current views and constraints.
- [var needsUpdateConstraints: Bool](nsview/needsupdateconstraints.md)
  A Boolean value indicating whether the view’s constraints need to be updated.
- [func updateConstraints()](nsview/updateconstraints.md)
  Update constraints for the view.
- [func updateConstraintsForSubtreeIfNeeded()](nsview/updateconstraintsforsubtreeifneeded.md)
  Updates the constraints for the receiving view and its subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/needslayout)*