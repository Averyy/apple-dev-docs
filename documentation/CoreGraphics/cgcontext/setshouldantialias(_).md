# setShouldAntialias(_:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Sets antialiasing on or off for a graphics context.

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
func setShouldAntialias(_ shouldAntialias: Bool)
```

```c
extern void CGContextSetShouldAntialias(CGContextRef c, bool shouldAntialias);
```

#### Discussion

Antialiasing is a graphics state parameter.

## Parameters

- `shouldAntialias`: A Boolean value that specifies whether antialiasing should be turned on. Antialiasing is turned on by default when a window or bitmap context is created. It is turned off for other types of contexts.

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
- [func setFillPattern(CGPattern, colorComponents: UnsafePointer<CGFloat>)](./setfillpattern%28_,colorcomponents%29.md)
  Sets the fill pattern in the specified graphics context.
- [CGContextSetLineDash](../cgcontextsetlinedash.md)
  Sets the pattern for dashed lines in a graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/setshouldantialias(_:))*