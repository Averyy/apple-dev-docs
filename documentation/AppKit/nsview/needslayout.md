# needsLayout

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the view needs a layout pass before it can be drawn.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var needsLayout: Bool { get set }
```

```objc
@property BOOL needsLayout;
```

#### Return Value

[`true`](../../Swift/true.md) if the view needs a layout pass, [`false`](../../Swift/false.md) otherwise.

#### Discussion

You only ever need to change the value of this property if your view implements the [`layout()`](./layout%28%29.md) method because it has custom layout that is not expressible in the constraint-based layout system. Setting this property to [`true`](../../Swift/true.md) lets the system know that the view’s layout needs to be updated before it is drawn. The system checks the value of this property prior to applying constraint-based layout rules for the view.

## See Also

### Triggering Auto Layout
- [func layout()](./layout%28%29.md)
  Perform layout in concert with the constraint-based layout system.
- [func layoutSubtreeIfNeeded()](./layoutsubtreeifneeded%28%29.md)
  Updates the layout of the receiving view and its subviews based on the current views and constraints.
- [var needsUpdateConstraints: Bool](./needsupdateconstraints.md)
  A Boolean value indicating whether the view’s constraints need to be updated.
- [func updateConstraints()](./updateconstraints%28%29.md)
  Update constraints for the view.
- [func updateConstraintsForSubtreeIfNeeded()](./updateconstraintsforsubtreeifneeded%28%29.md)
  Updates the constraints for the receiving view and its subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/needslayout)*