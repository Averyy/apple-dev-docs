# draw(_:)

**Framework**: AppKit  
**Kind**: method

Overridden by subclasses to draw the view’s image within the specified rectangle.

**Availability**:
- macOS ?+

## Declaration

```swift
func draw(_ dirtyRect: NSRect)
```

#### Discussion

Use this method to draw the specified portion of your view’s content. Your implementation of this method should be as fast as possible and do as little work as possible. The `dirtyRect` parameter helps you achieve better performance by specifying the portion of the view that needs to be drawn. You should always limit drawing to the content inside this rectangle. For even better performance, you can call the [`getRectsBeingDrawn(_:count:)`](nsview/getrectsbeingdrawn(_:count:).md) method and use the list of rectangles returned by that method to limit drawing even further. You can also use the [`needsToDraw(_:)`](nsview/needstodraw(_:).md) method to test whether objects in a particular rectangle need to be drawn.

The default implementation does nothing. Subclasses should override this method if they do custom drawing. Prior to calling this method, AppKit creates an appropriate drawing context and configures it for drawing to the view; you do not need to configure the drawing context yourself. If your app manages content using its layer object instead, use [`updateLayer()`](nsview/updatelayer().md) to update your layer instead of overriding this method.

If your custom view is a direct `NSView` subclass, you do not need to call `super`. For all other views, call `super` at some point in your implementation so that the parent class can perform any additional drawing.

> ❗ **Important**:  If the view’s [`isOpaque`](nsview/isopaque.md) property is [`true`](https://developer.apple.com/documentation/Swift/true), the view must completely fill the `dirtyRect` rectangle with opaque content.

For more information, see [`Drawing`](nsview-drawing.md).

This method also supports automatic observation tracking. See [`Updating views automatically with observation tracking`](updating-views-automatically-with-observation-tracking.md).

## Parameters

- `dirtyRect`: A rectangle defining the portion of the view that requires redrawing. This rectangle usually represents the portion of the view that requires updating. When responsive scrolling is enabled, this rectangle can also represent a nonvisible portion of the view that AppKit wants to cache.

## See Also

- [func shouldDrawColor() -> Bool](nsview/shoulddrawcolor.md)
  Returns a Boolean value indicating whether the view is being drawn to an environment that supports color.
- [func setNeedsDisplay(NSRect)](nsview/setneedsdisplay(_:).md)
  Marks the region of the view within the specified rectangle as needing display, increasing the view’s existing invalid region to include it.
- [func display()](nsview/display.md)
  Displays the view and all its subviews if possible, invoking each of the `NSView` methods [`lockFocus()`](nsview/lockfocus().md), [`draw(_:)`](nsview/draw(_:).md), and [`unlockFocus()`](nsview/unlockfocus().md) as necessary.
- [var isFlipped: Bool](nsview/isflipped.md)
  A Boolean value indicating whether the view uses a flipped coordinate system.
- [Updating views automatically with observation tracking](updating-views-automatically-with-observation-tracking.md)
  Use Swift Observation and AppKit’s automatic tracking to update your views in response to model data updates.
- [func layout()](nsview/layout.md)
  Perform layout in concert with the constraint-based layout system.
- [func updateConstraints()](nsview/updateconstraints.md)
  Update constraints for the view.
- [func updateLayer()](nsview/updatelayer.md)
  Updates the view’s content by modifying its underlying layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/draw(_:))*