# draw(in:angle:)

**Framework**: AppKit  
**Kind**: method

Fills the specified path with a linear gradient.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func draw(in path: NSBezierPath, angle: CGFloat)
```

#### Discussion

This convenience method behaves in a similar way to the [`draw(in:angle:)`](nsgradient/draw(in:angle:)-7sdyh.md) method, with the path object replacing the rectangle as the clipping region. Like the other method, the start and end colors are guaranteed to be visible at the farthest ends of the path.

The gradient formed by this method is clipped to `path`.

## Parameters

- `path`: The path object to fill.
- `angle`: The angle of the linear gradient, specified in degrees. Positive values indicate rotation in the counter-clockwise direction relative to the horizontal axis.

## See Also

- [func draw(from: NSPoint, to: NSPoint, options: NSGradient.DrawingOptions)](nsgradient/draw(from:to:options:).md)
  Draws a linear gradient between the specified start and end points.
- [func draw(in: NSRect, angle: CGFloat)](nsgradient/draw(in:angle:)-7sdyh.md)
  Fills the specified rectangle with a linear gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgradient/draw(in:angle:)-68adz)*