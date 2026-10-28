# updateLayer()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Updates the view’s content by modifying its underlying layer.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func updateLayer()
```

```objc
- (void) updateLayer;
```

## Discussion

You use this method to optimize the rendering of your view in situations where you can represent your views contents entirely using a layer object. If your view’s [`wantsUpdateLayer`](./wantsupdatelayer.md) property is [`true`](../../Swift/true.md), the view calls this method instead of [`draw(_:)`](./draw%28_%29.md) during the view update cycle. Custom views can override this method and use it to modify the properties of the underlying layer object. Modifying layer properties is a much more efficient way to update your view than is redrawing its content each time something changes.

When you want to update the contents of your layer, mark the view as dirty by setting its [`needsDisplay`](./needsdisplay.md) property to [`true`](../../Swift/true.md). Doing so adds the view to the list of views that need to be refreshed during the next update cycle. During that update cycle, this method is called if the [`wantsUpdateLayer`](./wantsupdatelayer.md) property is still [`true`](../../Swift/true.md).

Your implementation of this method should not call `super`.

This method supports automatic observation tracking. For more information, see [Updating views automatically with observation tracking in AppKit](../updating-views-automatically-with-observation-tracking-in-appkit.md).

## See Also

### Related Documentation
- [var wantsUpdateLayer: Bool](./wantsupdatelayer.md)
  A Boolean value indicating which drawing path the view takes when updating its contents.
### Observing data in views
- [Updating views automatically with observation tracking in AppKit](../updating-views-automatically-with-observation-tracking-in-appkit.md)
  Use Swift Observation and automatic tracking to update your views in response to model data updates.
- [func layout()](./layout%28%29.md)
  Perform layout in concert with the constraint-based layout system.
- [func updateConstraints()](./updateconstraints%28%29.md)
  Update constraints for the view.
- [func draw(NSRect)](./draw%28_%29.md)
  Overridden by subclasses to draw the view’s image within the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/updatelayer())*