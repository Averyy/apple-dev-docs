# setPatternPhase(_:)

**Framework**: Core Graphics  
**Kind**: method

Sets the pattern phase of a context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setPatternPhase(_ phase: CGSize)
```

#### Discussion

The pattern phase is a translation that Core Graphics applies prior to drawing a pattern in the context. The pattern phase is part of the graphics state of a context, and the default pattern phase is `(0,0)`. Setting the pattern phase has the effect of temporarily changing the pattern matrix of any pattern you draw. For example, setting the context’s pattern phase to `(2,3)` has the effect of moving the start of pattern cell tiling to the point `(2,3)` in default user space.

## Parameters

- `phase`: A pattern phase, specified in user space.

## See Also

- [func setAllowsAntialiasing(Bool)](cgcontext/setallowsantialiasing(_:).md)
  Sets whether or not to allow antialiasing for a graphics context.
- [func setFlatness(CGFloat)](cgcontext/setflatness(_:).md)
  Sets the accuracy of curved paths in a graphics context.
- [func setLineCap(CGLineCap)](cgcontext/setlinecap(_:).md)
  Sets the style for the endpoints of lines drawn in a graphics context.
- [func setLineDash(phase: CGFloat, lengths: [CGFloat])](cgcontext/setlinedash(phase:lengths:).md)
  Sets the pattern for drawing dashed lines.
- [func setLineJoin(CGLineJoin)](cgcontext/setlinejoin(_:).md)
  Sets the style for the joins of connected lines in a graphics context.
- [func setLineWidth(CGFloat)](cgcontext/setlinewidth(_:).md)
  Sets the line width for a graphics context.
- [func setMiterLimit(CGFloat)](cgcontext/setmiterlimit(_:).md)
  Sets the miter limit for the joins of connected lines in a graphics context.
- [func setFillPattern(CGPattern, colorComponents: UnsafePointer<CGFloat>)](cgcontext/setfillpattern(_:colorcomponents:).md)
  Sets the fill pattern in the specified graphics context.
- [func setShouldAntialias(Bool)](cgcontext/setshouldantialias(_:).md)
  Sets antialiasing on or off for a graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/setpatternphase(_:))*