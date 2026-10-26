# showTextAtPoint(x:y:string:length:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Displays a character string at a position you specify.

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
func showTextAtPoint(x: CGFloat, y: CGFloat, string: UnsafePointer<CChar>, length: Int)
```

```c
extern void CGContextShowTextAtPoint(CGContextRef c, CGFloat x, CGFloat y, const char *string, size_t length);
```

#### Discussion

Core Graphics uses font data provided by the system to map each byte of the array through the encoding vector of the current font to obtain the glyph to display. Note that the font must have been set using [`selectFont(name:size:textEncoding:)`](./selectfont%28name,size,textencoding%29.md). Don’t use `CGContextShowTextAtPoint` in conjunction with [`setFont(_:)`](./setfont%28_%29.md).

## Parameters

- `x`: A value for the x-coordinate (in user space) at which to display the text.
- `y`: A value for the y-coordinate (in user space) at which to display the text.
- `string`: An array of characters to draw.
- `length`: The length of the array specified in the `string` parameter.

## See Also

### Related Documentation
- [func showGlyphsAtPoint(x: CGFloat, y: CGFloat, glyphs: UnsafePointer<CGGlyph>?, count: Int)](./showglyphsatpoint%28x,y,glyphs,count%29.md)
  Displays an array of glyphs at a position you specify.
- [func showGlyphs(g: UnsafePointer<CGGlyph>?, count: Int)](./showglyphs%28g,count%29.md)
  Displays an array of glyphs at the current text position.
- [func showGlyphsWithAdvances(glyphs: UnsafePointer<CGGlyph>?, advances: UnsafePointer<CGSize>?, count: Int)](./showglyphswithadvances%28glyphs,advances,count%29.md)
  Draws an array of glyphs with varying offsets.
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
- [func showGlyphs(g: UnsafePointer<CGGlyph>?, count: Int)](./showglyphs%28g,count%29.md)
  Displays an array of glyphs at the current text position.
- [func showGlyphs([CGGlyph], at: [CGPoint])](./showglyphs%28_,at%29.md)
  Draws a set of glyphs at a set of corresponding positions.
- [CGContextSetTextMatrix](../cgcontextsettextmatrix.md)
  Sets the current text matrix.
- [CGContextSetTextPosition](../cgcontextsettextposition.md)
  Sets the location at which text is drawn.
- [CGContextGetTextPosition](../cgcontextgettextposition.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/showtextatpoint(x:y:string:length:))*