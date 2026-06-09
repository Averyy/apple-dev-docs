# Updating views automatically with observation tracking

**Framework**: AppKit

Use Swift Observation and AppKit’s automatic tracking to update your views in response to model data updates.

#### Overview

Swift [`Observation`](https://developer.apple.com/documentation/Observation) provides the [`Observable`](https://developer.apple.com/documentation/Observation/Observable) macro to mark your models for automatic change tracking. When you combine `Observable` models with AppKit, the system automatically watches for property changes and updates your views. You don’t need to manually invalidate anything — AppKit handles it for you.

AppKit provides methods in several objects where automatic observation tracking happens. In a view subclass, [`updateConstraints()`](nsview/updateconstraints().md) and [`layout()`](nsview/layout().md) are examples of two methods that automatically track any `Observable` properties you read, and AppKit updates your views when those properties change.

> **Note**: In macOS 15, the system doesn’t enable automatic observation tracking by default. To enable it, add the [`NSObservationTrackingEnabled`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSObservationTrackingEnabled) key to your app’s information property list and set the key’s value to [`true`](https://developer.apple.com/documentation/Swift/true).

##### Update View Properties Automatically

The [`viewWillLayout()`](nsviewcontroller/viewwilllayout().md) method automatically tracks `Observable` properties and updates views when they change. For example, to show a message list with a status label that displays unread message information, start by creating an `Observable` model with the properties your view needs:

```swift
@Observable
class MessageModel {
    var showStatus: Bool
    var statusText: String
}
```

Then, use these properties in your view controller’s `viewWillLayout()` method:

```swift
override func viewWillLayout() {
    super.viewWillLayout()
    statusLabel.alpha = model.showStatus ? 1.0 : 0.0
    statusLabel.text = model.statusText
}
```

When the view first appears, AppKit runs `viewWillLayout()` and tracks that you read `showStatus` and `statusText`. If either property changes later, AppKit automatically runs `viewWillLayout()` again to update the label.

You can also automatically track changes in a custom view using [`layout()`](nsview/layout().md).

## See Also

- [func layout()](nsview/layout.md)
  Perform layout in concert with the constraint-based layout system.
- [func updateConstraints()](nsview/updateconstraints.md)
  Update constraints for the view.
- [func updateLayer()](nsview/updatelayer.md)
  Updates the view’s content by modifying its underlying layer.
- [func draw(NSRect)](nsview/draw(_:).md)
  Overridden by subclasses to draw the view’s image within the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/updating-views-automatically-with-observation-tracking)*