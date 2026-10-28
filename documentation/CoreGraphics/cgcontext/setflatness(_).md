# setFlatness(_:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Sets the accuracy of curved paths in a graphics context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setFlatness(_ flatness: CGFloat)
```

```c
extern void CGContextSetFlatness(CGContextRef c, CGFloat flatness);
```

## Discussion

This function controls how accurately curved paths are rendered. Setting the flatness value to less than `1.0` renders highly accurate curves, but lengthens rendering times.

In most cases, you should not change the flatness value. Customizing the flatness value for the capabilities of a particular output device impairs the ability of your application to render to other devices.

## Parameters

- `flatness`: The largest permissible distance, measured in device pixels, between a point on the true curve and a point on the approximated curve.

## See Also

### Setting Path Drawing Options
- [func setAllowsAntialiasing(Bool)](./setallowsantialiasing%28_%29.md)
  Sets whether or not to allow antialiasing for a graphics context.
- [func setLineCap(CGLineCap)](./setlinecap%28_%29.md)
  Sets the style for the endpoints of lines drawn in a graphics context.
- [func setLineDash(phase: CGFloat, lengths: [CGFloat])](./setlinedash%28phase,lengths%29.md)
  Sets the pattern for drawing dashed lines.
- [func setLineJoin(CGLineJoin)](./setlinejoin%28_%29.md)
  Sets the style for the joins of connected lines in a graphics context.
- [func setLineWidth(CGFloat)](./setlinewidth%28_%29.md)
  Sets the line width for a graphics context.
- [func setMiterLimit(CGFloat)](./setmiterlimit%28_%29.md)
  Sets the miter limit for the joins of connected lines in a graphics context.
- [func setPatternPhase(CGSize)](./setpatternphase%28_%29.md)
  Sets the pattern phase of a context.
- [func setFillPattern(CGPattern, colorComponents: UnsafePointer<CGFloat>)](./setfillpattern%28_,colorcomponents%29.md)
  Sets the fill pattern in the specified graphics context.
- [func setShouldAntialias(Bool)](./setshouldantialias%28_%29.md)
  Sets antialiasing on or off for a graphics context.
- [CGContextSetLineDash](../cgcontextsetlinedash.md)
  Sets the pattern for dashed lines in a graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/setflatness(_:))*