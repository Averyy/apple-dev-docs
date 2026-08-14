# Updating views automatically with observation tracking in AppKit

**Framework**: AppKit

Use Swift Observation and automatic tracking to update your views in response to model data updates.

#### Overview

Swift [`Observation`](https://developer.apple.com/documentation/observation) provides the [`Observable`](https://developer.apple.com/documentation/observation/observable) macro to mark your models for automatic change tracking. When you combine `Observable` models with AppKit, the system automatically watches for property changes and updates your views. You don’t need to manually invalidate anything — AppKit handles it for you.

AppKit provides methods in several objects where automatic observation tracking happens. In a view subclass, [`updateConstraints()`](nsview/updateconstraints().md), [`layout()`](nsview/layout().md), and [`draw(_:)`](nsview/draw(_:).md) are examples of methods that automatically track any `Observable` properties you read, and AppKit updates your views when those properties change.

> **Note**: In macOS 15, the system doesn’t enable automatic observation tracking by default. To enable it, add the [`NSObservationTrackingEnabled`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsobservationtrackingenabled) key to your app’s information property list and set the key’s value to [`true`](https://developer.apple.com/documentation/swift/true).

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
    statusLabel.alphaValue = model.showStatus ? 1.0 : 0.0
    statusLabel.stringValue = model.statusText
}
```

When the view first appears, AppKit runs `viewWillLayout()` and tracks that you read `showStatus` and `statusText`. If either property changes later, AppKit automatically runs `viewWillLayout()` again to update the label.

You can also automatically track changes in a custom view using [`layout()`](nsview/layout().md).

##### Draw Views Automatically

AppKit automatically tracks any `Observable` properties you read inside your [`draw(_:)`](nsview/draw(_:).md) override. When those properties change, AppKit invalidates and redraws the view.

This automatic tracking also covers any methods that [`draw(_:)`](nsview/draw(_:).md) calls. This means that if you override drawing methods in a cell subclass, such as [`drawKnob(_:)`](nsslidercell/drawknob(_:).md) and [`drawBar(inside:flipped:)`](nsslidercell/drawbar(inside:flipped:).md), AppKit also tracks those overrides.

For example, to draw a custom slider cell that responds to model changes, start by creating an `Observable` model with the visual properties your cell needs:

```swift
@Observable
class SliderAppearance {
    var knobColor: NSColor
    var trackColor: NSColor
}
```

Then, override the drawing methods in your [`NSSliderCell`](nsslidercell.md) subclass and read from the model inside each override:

```swift
class CustomSliderCell: NSSliderCell {
    var appearance: SliderAppearance

    override func drawKnob(_ knobRect: NSRect) {
        appearance.knobColor.setFill()
        NSBezierPath(ovalIn: knobRect).fill()
    }

    override func drawBar(inside rect: NSRect, flipped: Bool) {
        appearance.trackColor.setFill()
        NSBezierPath(roundedRect: rect, xRadius: 2, yRadius: 2).fill()
    }
}
```

When [`drawKnob(_:)`](nsslidercell/drawknob(_:).md) and [`drawBar(inside:flipped:)`](nsslidercell/drawbar(inside:flipped:).md) run, AppKit tracks that they read `knobColor` and `trackColor`. If either property changes later, AppKit automatically redraws the slider.

## See Also

- [func viewWillLayout()](nsviewcontroller/viewwilllayout.md)
  Called just before the [`layout()`](nsview/layout().md) method of the view controller’s view is called.
- [func updateViewConstraints()](nsviewcontroller/updateviewconstraints.md)
  Called during Auto Layout constraint updating to enable the view controller to mediate the process.
- [func draw(NSRect)](nsview/draw(_:).md)
  Overridden by subclasses to draw the view’s image within the specified rectangle.
- [func layout()](nsview/layout.md)
  Perform layout in concert with the constraint-based layout system.
- [func updateConstraints()](nsview/updateconstraints.md)
  Update constraints for the view.
- [func layout()](nsview/layout.md)
  Perform layout in concert with the constraint-based layout system.
- [func updateConstraints()](nsview/updateconstraints.md)
  Update constraints for the view.
- [func updateLayer()](nsview/updatelayer.md)
  Updates the view’s content by modifying its underlying layer.
- [func draw(NSRect)](nsview/draw(_:).md)
  Overridden by subclasses to draw the view’s image within the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/updating-views-automatically-with-observation-tracking-in-appkit)*