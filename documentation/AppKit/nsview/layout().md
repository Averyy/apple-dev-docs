# layout()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Perform layout in concert with the constraint-based layout system.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func layout()
```

```objc
- (void) layout;
```

## Mentions

- [Updating views automatically with observation tracking in AppKit](../updating-views-automatically-with-observation-tracking-in-appkit.md)

## Discussion

Override this method if your custom view needs to perform custom layout not expressible using the constraint-based layout system. In this case you are responsible for setting [`needsLayout`](./needslayout.md) to [`true`](../../Swift/true.md) when something that impacts your custom layout changes.

You may not invalidate any constraints as part of your layout phase, nor invalidate the layout of your superview or views outside of your view hierarchy. You also may not invoke a drawing pass as part of layout.

You must call `[super layout]` as part of your implementation.

This method supports automatic observation tracking. For more information, see [Updating views automatically with observation tracking in AppKit](../updating-views-automatically-with-observation-tracking-in-appkit.md).

## See Also

### Observing data in views
- [Updating views automatically with observation tracking in AppKit](../updating-views-automatically-with-observation-tracking-in-appkit.md)
  Use Swift Observation and automatic tracking to update your views in response to model data updates.
- [func updateConstraints()](./updateconstraints%28%29.md)
  Update constraints for the view.
- [func updateLayer()](./updatelayer%28%29.md)
  Updates the view’s content by modifying its underlying layer.
- [func draw(NSRect)](./draw%28_%29.md)
  Overridden by subclasses to draw the view’s image within the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/layout())*