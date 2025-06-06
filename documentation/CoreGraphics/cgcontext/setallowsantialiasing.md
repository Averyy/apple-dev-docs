# setAllowsAntialiasing(_:)

**Framework**: Core Graphics  
**Kind**: method

Sets whether or not to allow antialiasing for a graphics context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setAllowsAntialiasing(_ allowsAntialiasing: Bool)
```

#### Discussion

Core Graphics performs antialiasing for a graphics context if both the `allowsAntialiasing` parameter and the graphics state parameter `shouldAntialias` are `true`.

This parameter is not part of the graphics state.

## Parameters

- `allowsAntialiasing`: A Boolean value that specifies whether or not to allow antialiasing. Pass   to allow antialiasing;   otherwise. This parameter is not part of the graphics state.

## See Also

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
- [func setPatternPhase(CGSize)](cgcontext/setpatternphase(_:).md)
  Sets the pattern phase of a context.
- [func setFillPattern(CGPattern, colorComponents: UnsafePointer<CGFloat>)](cgcontext/setfillpattern(_:colorcomponents:).md)
  Sets the fill pattern in the specified graphics context.
- [func setShouldAntialias(Bool)](cgcontext/setshouldantialias(_:).md)
  Sets antialiasing on or off for a graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/setallowsantialiasing(_:))*