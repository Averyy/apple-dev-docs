# CGContextSetTextPosition

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Sets the location at which text is drawn.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void CGContextSetTextPosition(CGContextRef c, CGFloat x, CGFloat y);
```

## Parameters

- `c`: A graphics context.
- `x`: A value for the x-coordinate at which to draw the text, in user space coordinates.
- `y`: A value for the y-coordinate at which to draw the text, in user space coordinates.

## See Also

### Drawing Text
- [var textMatrix: CGAffineTransform](./cgcontext/textmatrix.md)
  Returns the current text matrix.
- [CGContextSetTextMatrix](./cgcontextsettextmatrix.md)
  Sets the current text matrix.
- [CGContextGetTextPosition](./cgcontextgettextposition.md)
- [func selectFont(name: UnsafePointer<CChar>, size: CGFloat, textEncoding: CGTextEncoding)](./cgcontext/selectfont%28name,size,textencoding%29.md)
  Sets the font and font size in a graphics context.
- [func setCharacterSpacing(CGFloat)](./cgcontext/setcharacterspacing%28_%29.md)
  Sets the current character spacing.
- [func setFont(CGFont)](./cgcontext/setfont%28_%29.md)
  Sets the platform font in a graphics context.
- [func setFontSize(CGFloat)](./cgcontext/setfontsize%28_%29.md)
  Sets the current font size.
- [func setTextDrawingMode(CGTextDrawingMode)](./cgcontext/settextdrawingmode%28_%29.md)
  Sets the current text drawing mode.
- [func setAllowsFontSmoothing(Bool)](./cgcontext/setallowsfontsmoothing%28_%29.md)
  Sets whether or not to allow font smoothing for a graphics context.
- [func setAllowsFontSubpixelPositioning(Bool)](./cgcontext/setallowsfontsubpixelpositioning%28_%29.md)
  Sets whether or not to allow subpixel positioning for a graphics context.
- [func setAllowsFontSubpixelQuantization(Bool)](./cgcontext/setallowsfontsubpixelquantization%28_%29.md)
  Sets whether or not to allow subpixel quantization for a graphics context.
- [func setShouldSmoothFonts(Bool)](./cgcontext/setshouldsmoothfonts%28_%29.md)
  Enables or disables font smoothing in a graphics context.
- [func setShouldSubpixelPositionFonts(Bool)](./cgcontext/setshouldsubpixelpositionfonts%28_%29.md)
  Enables or disables subpixel positioning in a graphics context.
- [func setShouldSubpixelQuantizeFonts(Bool)](./cgcontext/setshouldsubpixelquantizefonts%28_%29.md)
  Enables or disables subpixel quantization in a graphics context.
- [func showGlyphs(g: UnsafePointer<CGGlyph>?, count: Int)](./cgcontext/showglyphs%28g,count%29.md)
  Displays an array of glyphs at the current text position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontextsettextposition)*