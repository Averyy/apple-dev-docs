# setFillPattern(_:colorComponents:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Sets the fill pattern in the specified graphics context.

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
func setFillPattern(_ pattern: CGPattern, colorComponents components: UnsafePointer<CGFloat>)
```

```c
extern void CGContextSetFillPattern(CGContextRef c, CGPatternRef pattern, const CGFloat *components);
```

#### Discussion

The current fill color space must be a pattern color space. Otherwise, the result of calling this function is undefined. If you want to set a fill color, not a pattern, use [`setFillColor(_:)`](./setfillcolor%28_%29-8lhn8.md).

## Parameters

- `pattern`: A fill pattern. The object is retained; upon return, you may safely release it.
- `components`: If the pattern is an uncolored (or a masking) pattern, pass an array of intensity values that specify the color to use when the pattern is painted. The number of array elements must equal the number of components in the base space of the fill pattern color space, plus an additional component for the alpha value.

  If the pattern is a colored pattern, pass an alpha value.

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
- [func setPatternPhase(CGSize)](./setpatternphase%28_%29.md)
  Sets the pattern phase of a context.
- [func setShouldAntialias(Bool)](./setshouldantialias%28_%29.md)
  Sets antialiasing on or off for a graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/setfillpattern(_:colorcomponents:))*