# draw(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Overridden by subclasses to draw the view’s image within the specified rectangle.

**Availability**:
- macOS

## Declaration

```swift
func draw(_ dirtyRect: NSRect)
```

```objc
- (void) drawRect:(NSRect) dirtyRect;
```

## Mentions

- [Updating views automatically with observation tracking in AppKit](../updating-views-automatically-with-observation-tracking-in-appkit.md)

#### Discussion

Use this method to draw the specified portion of your view’s content. Your implementation of this method should be as fast as possible and do as little work as possible. The `dirtyRect` parameter helps you achieve better performance by specifying the portion of the view that needs to be drawn. You should always limit drawing to the content inside this rectangle. For even better performance, you can call the [`getRectsBeingDrawn(_:count:)`](./getrectsbeingdrawn%28_,count%29.md) method and use the list of rectangles returned by that method to limit drawing even further. You can also use the [`needsToDraw(_:)`](./needstodraw%28_%29.md) method to test whether objects in a particular rectangle need to be drawn.

The default implementation does nothing. Subclasses should override this method if they do custom drawing. Prior to calling this method, AppKit creates an appropriate drawing context and configures it for drawing to the view; you do not need to configure the drawing context yourself. If your app manages content using its layer object instead, use [`updateLayer()`](./updatelayer%28%29.md) to update your layer instead of overriding this method.

If your custom view is a direct `NSView` subclass, you do not need to call `super`. For all other views, call `super` at some point in your implementation so that the parent class can perform any additional drawing.

> ❗ **Important**:  If the view’s [`isOpaque`](./isopaque.md) property is [`true`](../../Swift/true.md), the view must completely fill the `dirtyRect` rectangle with opaque content.

For more information, see [Drawing](../nsview-drawing.md).

This method also supports automatic observation tracking. See [Updating views automatically with observation tracking in AppKit](../updating-views-automatically-with-observation-tracking-in-appkit.md).

## Parameters

- `dirtyRect`: A rectangle defining the portion of the view that requires redrawing. This rectangle usually represents the portion of the view that requires updating. When responsive scrolling is enabled, this rectangle can also represent a nonvisible portion of the view that AppKit wants to cache.

## See Also

### Related Documentation
- [func shouldDrawColor() -> Bool](./shoulddrawcolor%28%29.md)
  Returns a Boolean value indicating whether the view is being drawn to an environment that supports color.
- [func setNeedsDisplay(NSRect)](./setneedsdisplay%28_%29.md)
  Marks the region of the view within the specified rectangle as needing display, increasing the view’s existing invalid region to include it.
- [func display()](./display%28%29.md)
  Displays the view and all its subviews if possible, invoking each of the `NSView` methods [`lockFocus()`](./lockfocus%28%29.md), [`draw(_:)`](./draw%28_%29.md), and [`unlockFocus()`](./unlockfocus%28%29.md) as necessary.
- [var isFlipped: Bool](./isflipped.md)
  A Boolean value indicating whether the view uses a flipped coordinate system.
### Observing data in views
- [Updating views automatically with observation tracking in AppKit](../updating-views-automatically-with-observation-tracking-in-appkit.md)
  Use Swift Observation and automatic tracking to update your views in response to model data updates.
- [func layout()](./layout%28%29.md)
  Perform layout in concert with the constraint-based layout system.
- [func updateConstraints()](./updateconstraints%28%29.md)
  Update constraints for the view.
- [func updateLayer()](./updatelayer%28%29.md)
  Updates the view’s content by modifying its underlying layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/draw(_:))*