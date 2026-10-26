# CGContextSetTextMatrix

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Sets the current text matrix.

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
extern void CGContextSetTextMatrix(CGContextRef c, CGAffineTransform t);
```

#### Discussion

The text matrix specifies the transform from text space to user space. To produce the final text rendering matrix that is used to actually draw the text on the page, Core Graphics concatenates the text matrix with the current transformation matrix and other parameters from the graphics state.

Note that the text matrix is *not* a part of the graphics state—saving or restoring the graphics state has no effect on the text matrix. The text matrix is an attribute of the graphics context, not of the current font.

## Parameters

- `c`: A graphics context.
- `t`: The text matrix to set.

## See Also

### Drawing Text
- [var textMatrix: CGAffineTransform](./cgcontext/textmatrix.md)
  Returns the current text matrix.
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
- [func showGlyphs(g: UnsafePointer<CGGlyph>?, count: Int)](./cgcontext/showglyphs%28g,count%29.md)
  Displays an array of glyphs at the current text position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontextsettextmatrix)*