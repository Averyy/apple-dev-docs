# showGlyphs(g:count:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Displays an array of glyphs at the current text position.

**Availability**:
- iOS 2.0+ - Deprecated in 7.0
- iPadOS 2.0+ - Deprecated in 7.0
- Mac Catalyst 2.0+ - Deprecated in 7.0
- tvOS
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use [Core Text](../../CoreText/CoreText.md) instead.

## Declaration

```swift
func showGlyphs(g: UnsafePointer<CGGlyph>?, count: Int)
```

```c
extern void CGContextShowGlyphs(CGContextRef c, const CGGlyph *g, size_t count);
```

#### Discussion

This function displays an array of glyphs at the current text position, a point specified by the current text matrix.

## Parameters

- `g`: An array of glyphs to display.
- `count`: The total number of glyphs passed in the `g` parameter.

## See Also

### Related Documentation
- [func showText(string: UnsafePointer<CChar>, length: Int)](./showtext%28string,length%29.md)
  Displays a character array at the current text position, a point specified by the current text matrix.
- [func showTextAtPoint(x: CGFloat, y: CGFloat, string: UnsafePointer<CChar>, length: Int)](./showtextatpoint%28x,y,string,length%29.md)
  Displays a character string at a position you specify.
### Drawing Text
- [var textMatrix: CGAffineTransform](./textmatrix.md)
  Returns the current text matrix.
- [var textPosition: CGPoint](./textposition.md)
- [func selectFont(name: UnsafePointer<CChar>, size: CGFloat, textEncoding: CGTextEncoding)](./selectfont%28name,size,textencoding%29.md)
  Sets the font and font size in a graphics context.
- [func setCharacterSpacing(CGFloat)](./setcharacterspacing%28_%29.md)
  Sets the current character spacing.
- [func setFont(CGFont)](./setfont%28_%29.md)
  Sets the platform font in a graphics context.
- [func setFontSize(CGFloat)](./setfontsize%28_%29.md)
  Sets the current font size.
- [func setTextDrawingMode(CGTextDrawingMode)](./settextdrawingmode%28_%29.md)
  Sets the current text drawing mode.
- [func setAllowsFontSmoothing(Bool)](./setallowsfontsmoothing%28_%29.md)
  Sets whether or not to allow font smoothing for a graphics context.
- [func setAllowsFontSubpixelPositioning(Bool)](./setallowsfontsubpixelpositioning%28_%29.md)
  Sets whether or not to allow subpixel positioning for a graphics context.
- [func setAllowsFontSubpixelQuantization(Bool)](./setallowsfontsubpixelquantization%28_%29.md)
  Sets whether or not to allow subpixel quantization for a graphics context.
- [func setShouldSmoothFonts(Bool)](./setshouldsmoothfonts%28_%29.md)
  Enables or disables font smoothing in a graphics context.
- [func setShouldSubpixelPositionFonts(Bool)](./setshouldsubpixelpositionfonts%28_%29.md)
  Enables or disables subpixel positioning in a graphics context.
- [func setShouldSubpixelQuantizeFonts(Bool)](./setshouldsubpixelquantizefonts%28_%29.md)
  Enables or disables subpixel quantization in a graphics context.
- [func showGlyphs([CGGlyph], at: [CGPoint])](./showglyphs%28_,at%29.md)
  Draws a set of glyphs at a set of corresponding positions.
- [func showGlyphsAtPoint(x: CGFloat, y: CGFloat, glyphs: UnsafePointer<CGGlyph>?, count: Int)](./showglyphsatpoint%28x,y,glyphs,count%29.md)
  Displays an array of glyphs at a position you specify.
- [CGContextSetTextMatrix](../cgcontextsettextmatrix.md)
  Sets the current text matrix.
- [CGContextSetTextPosition](../cgcontextsettextposition.md)
  Sets the location at which text is drawn.
- [CGContextGetTextPosition](../cgcontextgettextposition.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/showglyphs(g:count:))*