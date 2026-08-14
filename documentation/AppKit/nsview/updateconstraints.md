# updateConstraints()

**Framework**: AppKit  
**Kind**: method

Update constraints for the view.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func updateConstraints()
```

## Mentions

- [Updating views automatically with observation tracking in AppKit](updating-views-automatically-with-observation-tracking-in-appkit.md)

#### Discussion

Override this method to optimize changes to your constraints.

> **Note**:  It is almost always cleaner and easier to update a constraint immediately after the affecting change has occurred. For example, if you want to change a constraint in response to a button press, make that change directly in the button’s action method. You should only override this method when changing constraints in place is too slow, or when a view is producing a number of redundant changes.

To schedule a change, set the view’s [`needsUpdateConstraints`](nsview/needsupdateconstraints.md) property to [`true`](https://developer.apple.com/documentation/swift/true). The system then calls your implementation of [`updateConstraints()`](nsview/updateconstraints().md) before the layout occurs. This lets you verify that all necessary constraints for your content are in place at a time when your custom view’s properties are not changing.

Your implementation must be as efficient as possible. Do not deactivate all your constraints, then reactivate the ones you need. Instead, your app must have some way of tracking your constraints, and validating them during each update pass. Only change items that need to be changed. During each update pass, you must ensure that you have the appropriate constraints for the app’s current state.

Do not set the [`needsUpdateConstraints`](nsview/needsupdateconstraints.md) property inside your implementation. Setting [`needsUpdateConstraints`](nsview/needsupdateconstraints.md) to [`true`](https://developer.apple.com/documentation/swift/true) schedules another update pass, creating a feedback loop.

This method supports automatic observation tracking. For more information, see [`Updating views automatically with observation tracking in AppKit`](updating-views-automatically-with-observation-tracking-in-appkit.md).

> ❗ **Important**:  Call `[super updateConstraints]` as the final step in your implementation.

## See Also

- [Updating views automatically with observation tracking in AppKit](updating-views-automatically-with-observation-tracking-in-appkit.md)
  Use Swift Observation and automatic tracking to update your views in response to model data updates.
- [func layout()](nsview/layout.md)
  Perform layout in concert with the constraint-based layout system.
- [func updateLayer()](nsview/updatelayer.md)
  Updates the view’s content by modifying its underlying layer.
- [func draw(NSRect)](nsview/draw(_:).md)
  Overridden by subclasses to draw the view’s image within the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/updateconstraints())*