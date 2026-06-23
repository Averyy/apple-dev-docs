# updateLayer()

**Framework**: AppKit  
**Kind**: method

Updates the view’s content by modifying its underlying layer.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func updateLayer()
```

#### Discussion

You use this method to optimize the rendering of your view in situations where you can represent your views contents entirely using a layer object. If your view’s [`wantsUpdateLayer`](nsview/wantsupdatelayer.md) property is [`true`](https://developer.apple.com/documentation/Swift/true), the view calls this method instead of [`draw(_:)`](nsview/draw(_:).md) during the view update cycle. Custom views can override this method and use it to modify the properties of the underlying layer object. Modifying layer properties is a much more efficient way to update your view than is redrawing its content each time something changes.

When you want to update the contents of your layer, mark the view as dirty by setting its [`needsDisplay`](nsview/needsdisplay.md) property to [`true`](https://developer.apple.com/documentation/Swift/true). Doing so adds the view to the list of views that need to be refreshed during the next update cycle. During that update cycle, this method is called if the [`wantsUpdateLayer`](nsview/wantsupdatelayer.md) property is still [`true`](https://developer.apple.com/documentation/Swift/true).

Your implementation of this method should not call `super`.

This method supports automatic observation tracking. For more information, see [`Updating views automatically with observation tracking in AppKit`](updating-views-automatically-with-observation-tracking-in-appkit.md).

## See Also

- [var wantsUpdateLayer: Bool](nsview/wantsupdatelayer.md)
  A Boolean value indicating which drawing path the view takes when updating its contents.
- [Updating views automatically with observation tracking in AppKit](updating-views-automatically-with-observation-tracking-in-appkit.md)
  Use Swift Observation and automatic tracking to update your views in response to model data updates.
- [func layout()](nsview/layout.md)
  Perform layout in concert with the constraint-based layout system.
- [func updateConstraints()](nsview/updateconstraints.md)
  Update constraints for the view.
- [func draw(NSRect)](nsview/draw(_:).md)
  Overridden by subclasses to draw the view’s image within the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/updatelayer())*