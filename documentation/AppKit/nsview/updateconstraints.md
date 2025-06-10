# updateConstraints()

**Framework**: AppKit  
**Kind**: method

Update constraints for the view.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func updateConstraints()
```

#### Discussion

Override this method to optimize changes to your constraints.

> **Note**:  It is almost always cleaner and easier to update a constraint immediately after the affecting change has occurred. For example, if you want to change a constraint in response to a button press, make that change directly in the button’s action method. You should only override this method when changing constraints in place is too slow, or when a view is producing a number of redundant changes.

To schedule a change, set the view’s [`needsUpdateConstraints`](nsview/needsupdateconstraints.md) property to [`true`](https://developer.apple.com/documentation/swift/true). The system then calls your implementation of [`updateConstraints()`](nsview/updateconstraints().md) before the layout occurs. This lets you verify that all necessary constraints for your content are in place at a time when your custom view’s properties are not changing.

Your implementation must be as efficient as possible. Do not deactivate all your constraints, then reactivate the ones you need. Instead, your app must have some way of tracking your constraints, and validating them during each update pass. Only change items that need to be changed. During each update pass, you must ensure that you have the appropriate constraints for the app’s current state.

Do not set the [`needsUpdateConstraints`](nsview/needsupdateconstraints.md) property inside your implementation. Setting [`needsUpdateConstraints`](nsview/needsupdateconstraints.md) to [`true`](https://developer.apple.com/documentation/swift/true) schedules another update pass, creating a feedback loop.

> ❗ **Important**:  Call `[super updateConstraints]` as the final step in your implementation.

## See Also

- [var needsLayout: Bool](nsview/needslayout.md)
  A Boolean value indicating whether the view needs a layout pass before it can be drawn.
- [func layout()](nsview/layout.md)
  Perform layout in concert with the constraint-based layout system.
- [func layoutSubtreeIfNeeded()](nsview/layoutsubtreeifneeded.md)
  Updates the layout of the receiving view and its subviews based on the current views and constraints.
- [var needsUpdateConstraints: Bool](nsview/needsupdateconstraints.md)
  A Boolean value indicating whether the view’s constraints need to be updated.
- [func updateConstraintsForSubtreeIfNeeded()](nsview/updateconstraintsforsubtreeifneeded.md)
  Updates the constraints for the receiving view and its subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/updateconstraints())*