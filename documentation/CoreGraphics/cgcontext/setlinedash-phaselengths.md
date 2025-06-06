# setLineDash(phase:lengths:)

**Framework**: Core Graphics  
**Kind**: method

Sets the pattern for drawing dashed lines.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst ?+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setLineDash(phase: CGFloat, lengths: [CGFloat])
```

## Parameters

- `phase`: A value that specifies how far into the dash pattern the line starts, in units of the user space. For example, a value of   draws a line starting with the beginning of a dash pattern, and a value of   means the line is drawn with the dash pattern starting at three units from its beginning.
- `lengths`: For example, the array   sets a dash pattern that alternates between a 2-unit-long painted segment and a 3-unit-long unpainted segment. The array   sets the pattern to a 1-unit painted segment, a 3-unit unpainted segment, a 4-unit painted segment, and a 2-unit unpainted segment.Pass an empty array to clear the dash pattern so that all stroke drawing in the context uses solid lines.

## See Also

- [func setAllowsAntialiasing(Bool)](cgcontext/setallowsantialiasing(_:).md)
  Sets whether or not to allow antialiasing for a graphics context.
- [func setFlatness(CGFloat)](cgcontext/setflatness(_:).md)
  Sets the accuracy of curved paths in a graphics context.
- [func setLineCap(CGLineCap)](cgcontext/setlinecap(_:).md)
  Sets the style for the endpoints of lines drawn in a graphics context.
- [func setLineJoin(CGLineJoin)](cgcontext/setlinejoin(_:).md)
  Sets the style for the joins of connected lines in a graphics context.
- [func setLineWidth(CGFloat)](cgcontext/setlinewidth(_:).md)
  Sets the line width for a graphics context.
- [func setMiterLimit(CGFloat)](cgcontext/setmiterlimit(_:).md)
  Sets the miter limit for the joins of connected lines in a graphics context.
- [func setPatternPhase(CGSize)](cgcontext/setpatternphase(_:).md)
  Sets the pattern phase of a context.
- [func setFillPattern(CGPattern, colorComponents: UnsafePointer<CGFloat>)](cgcontext/setfillpattern(_:colorcomponents:).md)
  Sets the fill pattern in the specified graphics context.
- [func setShouldAntialias(Bool)](cgcontext/setshouldantialias(_:).md)
  Sets antialiasing on or off for a graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/setlinedash(phase:lengths:))*