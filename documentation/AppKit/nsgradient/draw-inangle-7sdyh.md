# draw(in:angle:)

**Framework**: AppKit  
**Kind**: method

Fills the specified rectangle with a linear gradient.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func draw(in rect: NSRect, angle: CGFloat)
```

#### Discussion

This convenience method draws a linear gradient inside the specified rectangle. The gradient is drawn so that the start and end colors are guaranteed to be visible in opposite corners of the rectangle. The angle of rotation determines which corner contains the start color; see the table below.

| Rotation angle | Start corner |
| --- | --- |
| 0-89 degrees | Lower-left |
| 90-179 degrees | Lower-right |
| 180-269 degrees | Upper-right |
| 270-359 degrees | Upper-left |

The gradient’s color transitions occur along the line formed by the angle of rotation. For example, a rotation of 0 degrees results in colors changing from left-to-right across the rectangle, while a rotation of 90 degrees results in colors changing from bottom to top.

The gradient drawn by this method is clipped to `rect`.

## Parameters

- `rect`: The rectangle to fill.
- `angle`: The angle of the linear gradient, specified in degrees. Positive values indicate rotation in the counter-clockwise direction relative to the horizontal axis.

## See Also

- [func draw(from: NSPoint, to: NSPoint, options: NSGradient.DrawingOptions)](nsgradient/draw(from:to:options:).md)
  Draws a linear gradient between the specified start and end points.
- [func draw(in: NSBezierPath, angle: CGFloat)](nsgradient/draw(in:angle:)-68adz.md)
  Fills the specified path with a linear gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgradient/draw(in:angle:)-7sdyh)*