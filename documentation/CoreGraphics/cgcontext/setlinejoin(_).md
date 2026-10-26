# setLineJoin(_:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Sets the style for the joins of connected lines in a graphics context.

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
func setLineJoin(_ join: CGLineJoin)
```

```c
extern void CGContextSetLineJoin(CGContextRef c, CGLineJoin join);
```

## Parameters

- `join`: A line join value—[`CGLineJoin.miter`](../cglinejoin/miter.md) (the default), [`CGLineJoin.round`](../cglinejoin/round.md), or [`CGLineJoin.bevel`](../cglinejoin/bevel.md). See [`CGPath`](../cgpath.md).

## See Also

### Setting Path Drawing Options
- [func setAllowsAntialiasing(Bool)](./setallowsantialiasing%28_%29.md)
  Sets whether or not to allow antialiasing for a graphics context.
- [func setFlatness(CGFloat)](./setflatness%28_%29.md)
  Sets the accuracy of curved paths in a graphics context.
- [func setLineCap(CGLineCap)](./setlinecap%28_%29.md)
  Sets the style for the endpoints of lines drawn in a graphics context.
- [func setLineDash(phase: CGFloat, lengths: [CGFloat])](./setlinedash%28phase,lengths%29.md)
  Sets the pattern for drawing dashed lines.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/setlinejoin(_:))*