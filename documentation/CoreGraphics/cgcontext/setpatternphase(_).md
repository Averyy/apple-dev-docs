# setPatternPhase(_:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Sets the pattern phase of a context.

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
func setPatternPhase(_ phase: CGSize)
```

```c
extern void CGContextSetPatternPhase(CGContextRef c, CGSize phase);
```

#### Discussion

The pattern phase is a translation that Core Graphics applies prior to drawing a pattern in the context. The pattern phase is part of the graphics state of a context, and the default pattern phase is `(0,0)`. Setting the pattern phase has the effect of temporarily changing the pattern matrix of any pattern you draw. For example, setting the context’s pattern phase to `(2,3)` has the effect of moving the start of pattern cell tiling to the point `(2,3)` in default user space.

## Parameters

- `phase`: A pattern phase, specified in user space.

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
- [func setLineJoin(CGLineJoin)](./setlinejoin%28_%29.md)
  Sets the style for the joins of connected lines in a graphics context.
- [func setLineWidth(CGFloat)](./setlinewidth%28_%29.md)
  Sets the line width for a graphics context.
- [func setMiterLimit(CGFloat)](./setmiterlimit%28_%29.md)
  Sets the miter limit for the joins of connected lines in a graphics context.
- [func setFillPattern(CGPattern, colorComponents: UnsafePointer<CGFloat>)](./setfillpattern%28_,colorcomponents%29.md)
  Sets the fill pattern in the specified graphics context.
- [func setShouldAntialias(Bool)](./setshouldantialias%28_%29.md)
  Sets antialiasing on or off for a graphics context.
- [CGContextSetLineDash](../cgcontextsetlinedash.md)
  Sets the pattern for dashed lines in a graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/setpatternphase(_:))*