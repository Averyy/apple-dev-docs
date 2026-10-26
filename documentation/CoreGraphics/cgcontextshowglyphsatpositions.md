# CGContextShowGlyphsAtPositions

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Draws glyphs at the provided position.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void CGContextShowGlyphsAtPositions(CGContextRef c, const CGGlyph *glyphs, const CGPoint *Lpositions, size_t count);
```

## Parameters

- `c`: The graphics context in which to display the glyphs.
- `glyphs`: An array of glyphs.
- `Lpositions`: The positions for the glyphs. Each item in this array matches with the glyph at the corresponding index in the `glyphs` array. The position of each glyph is specified in text space, and, as a consequence, is transformed through the text matrix to user space.
- `count`: The number of items in the `glyphs` array.

## See Also

### Drawing Text
- [var textMatrix: CGAffineTransform](./cgcontext/textmatrix.md)
  Returns the current text matrix.
- [CGContextSetTextMatrix](./cgcontextsettextmatrix.md)
  Sets the current text matrix.
- [CGContextSetTextPosition](./cgcontextsettextposition.md)
  Sets the location at which text is drawn.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontextshowglyphsatpositions)*