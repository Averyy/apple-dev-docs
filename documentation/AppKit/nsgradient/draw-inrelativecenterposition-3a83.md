# draw(in:relativeCenterPosition:)

**Framework**: AppKit  
**Kind**: method

Draws a radial gradient starting at the center of the specified rectangle.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func draw(in rect: NSRect, relativeCenterPosition: NSPoint)
```

#### Discussion

The center point of the starting circle is the same as the center point of `rect`. The radius of the starting circle is 0, resulting in the starting circle being just a point.

The center point of the end circle starts at the center point of `rect` and is modified by the value in the `relativeCenterPosition` parameter. For example, if `relativeCenterPosition` contains the point (1.0, 1.0), the center of the end circle is located in the top-right corner of `rect`. The radius of the end circle is set to the smallest value that ensures `rect` is covered by the end circle.

The gradient formed by this method is clipped to `rect`.

## Parameters

- `rect`: The rectangle to fill.
- `relativeCenterPosition`: The relative location within the rectangle to use as the center point of the gradient’s end circle. Each coordinate must contain a value between -1.0 and 1.0. A coordinate value of 0 represents the center of   along the given axis. In the default coordinate system, a value of -1.0 corresponds to the bottom or left edge of the rectangle and a value of 1.0 corresponds to the top or right edge.

## See Also

- [func draw(fromCenter: NSPoint, radius: CGFloat, toCenter: NSPoint, radius: CGFloat, options: NSGradient.DrawingOptions)](nsgradient/draw(fromcenter:radius:tocenter:radius:options:).md)
  Draws a radial gradient between the specified circles.
- [func draw(in: NSBezierPath, relativeCenterPosition: NSPoint)](nsgradient/draw(in:relativecenterposition:)-502cc.md)
  Draws a radial gradient starting at the center point of the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgradient/draw(in:relativecenterposition:)-3a83)*