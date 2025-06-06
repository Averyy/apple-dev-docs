# draw(from:to:options:)

**Framework**: AppKit  
**Kind**: method

Draws a linear gradient between the specified start and end points.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func draw(from startingPoint: NSPoint, to endingPoint: NSPoint, options: NSGradient.DrawingOptions = [])
```

#### Discussion

This method draws the gradient color changes along the line formed by the two points. The gradient fill extends perpendicularly outward from line until it reaches the edges of the current clipping region.

This is a primitive method used by the `NSGradient` class to draw linear gradients. Because this method does not perform any clipping of the gradient fill pattern, you must ensure that the clipping region is configured properly if you intend to invoke this method directly. By default, the clipping region is set to the current view or window in which drawing occurs.

## Parameters

- `startingPoint`: The starting point for the gradient, in the local coordinate system. The gradient’s first color is drawn at this point.
- `endingPoint`: The end point for the gradient, in the local coordinate system. The gradient’s last color is drawn at this point.
- `options`: The gradient options, if any. You can use these options to extend the gradient size beyond the start and end points. For more information, see  .

## See Also

- [func draw(in: NSRect, angle: CGFloat)](nsgradient/draw(in:angle:)-7sdyh.md)
  Fills the specified rectangle with a linear gradient.
- [func draw(in: NSBezierPath, angle: CGFloat)](nsgradient/draw(in:angle:)-68adz.md)
  Fills the specified path with a linear gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgradient/draw(from:to:options:))*