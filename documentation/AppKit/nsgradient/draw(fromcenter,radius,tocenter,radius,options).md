# draw(fromCenter:radius:toCenter:radius:options:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws a radial gradient between the specified circles.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func draw(fromCenter startCenter: NSPoint, radius startRadius: CGFloat, toCenter endCenter: NSPoint, radius endRadius: CGFloat, options: NSGradient.DrawingOptions = [])
```

```objc
- (void) drawFromCenter:(NSPoint) startCenter radius:(CGFloat) startRadius toCenter:(NSPoint) endCenter radius:(CGFloat) endRadius options:(NSGradientDrawingOptions) options;
```

## Discussion

This method draws a radial gradient pattern starting at the first circle and ending at the second circle. The gradient color transitions occur in circular bands emanating from the starting circle and ending at the second circle.

This is a primitive method used by the `NSGradient` class to draw radial gradients. Because this method does not perform any clipping of the gradient fill pattern, you must ensure that the clipping region is configured properly if you intend to invoke this method directly. By default, the clipping region is set to the current view or window in which drawing occurs.

## Parameters

- `startCenter`: The center point of the circle that represents the beginning of the gradient.
- `startRadius`: The radius of the circle that represents the beginning of the gradient.
- `endCenter`: The center point of the circle that represents the end of the gradient.
- `endRadius`: The radius of the circle that represents the end of the gradient.
- `options`: The gradient options, if any. You can use these options to extend the gradient size beyond the start and end circles. For more information, see [`NSGradient.DrawingOptions`](./drawingoptions.md).

## See Also

### Drawing a Radial Gradient
- [func draw(in: NSRect, relativeCenterPosition: NSPoint)](./draw%28in,relativecenterposition%29-3a83.md)
  Draws a radial gradient starting at the center of the specified rectangle.
- [func draw(in: NSBezierPath, relativeCenterPosition: NSPoint)](./draw%28in,relativecenterposition%29-502cc.md)
  Draws a radial gradient starting at the center point of the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgradient/draw(fromcenter:radius:tocenter:radius:options:))*