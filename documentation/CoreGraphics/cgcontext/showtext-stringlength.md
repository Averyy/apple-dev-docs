# showText(string:length:)

**Framework**: Core Graphics  
**Kind**: method

Displays a character array at the current text position, a point specified by the current text matrix.

**Availability**:
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func showText(string: UnsafePointer<CChar>, length: Int)
```

#### Discussion

Core Graphics uses font data provided by the system to map each byte of the array through the encoding vector of the current font to obtain the glyph to display. Note that the font must have been set using [`selectFont(name:size:textEncoding:)`](cgcontext/selectfont(name:size:textencoding:).md). Don’t use `CGContextShowText` in conjunction with [`setFont(_:)`](cgcontext/setfont(_:).md).

## Parameters

- `string`: An array of characters to draw.
- `length`: The length of the array specified in the   parameter.

## See Also

- [func showGlyphsAtPoint(x: CGFloat, y: CGFloat, glyphs: UnsafePointer<CGGlyph>?, count: Int)](cgcontext/showglyphsatpoint(x:y:glyphs:count:).md)
  Displays an array of glyphs at a position you specify.
- [func showGlyphs(g: UnsafePointer<CGGlyph>?, count: Int)](cgcontext/showglyphs(g:count:).md)
  Displays an array of glyphs at the current text position.
- [func showGlyphsWithAdvances(glyphs: UnsafePointer<CGGlyph>?, advances: UnsafePointer<CGSize>?, count: Int)](cgcontext/showglyphswithadvances(glyphs:advances:count:).md)
  Draws an array of glyphs with varying offsets.
- [var textMatrix: CGAffineTransform](cgcontext/textmatrix.md)
  Returns the current text matrix.
- [var textPosition: CGPoint](cgcontext/textposition.md)
- [func selectFont(name: UnsafePointer<CChar>, size: CGFloat, textEncoding: CGTextEncoding)](cgcontext/selectfont(name:size:textencoding:).md)
  Sets the font and font size in a graphics context.
- [func setCharacterSpacing(CGFloat)](cgcontext/setcharacterspacing(_:).md)
  Sets the current character spacing.
- [func setFont(CGFont)](cgcontext/setfont(_:).md)
  Sets the platform font in a graphics context.
- [func setFontSize(CGFloat)](cgcontext/setfontsize(_:).md)
  Sets the current font size.
- [func setTextDrawingMode(CGTextDrawingMode)](cgcontext/settextdrawingmode(_:).md)
  Sets the current text drawing mode.
- [func setAllowsFontSmoothing(Bool)](cgcontext/setallowsfontsmoothing(_:).md)
  Sets whether or not to allow font smoothing for a graphics context.
- [func setAllowsFontSubpixelPositioning(Bool)](cgcontext/setallowsfontsubpixelpositioning(_:).md)
  Sets whether or not to allow subpixel positioning for a graphics context.
- [func setAllowsFontSubpixelQuantization(Bool)](cgcontext/setallowsfontsubpixelquantization(_:).md)
  Sets whether or not to allow subpixel quantization for a graphics context.
- [func setShouldSmoothFonts(Bool)](cgcontext/setshouldsmoothfonts(_:).md)
  Enables or disables font smoothing in a graphics context.
- [func setShouldSubpixelPositionFonts(Bool)](cgcontext/setshouldsubpixelpositionfonts(_:).md)
  Enables or disables subpixel positioning in a graphics context.
- [func setShouldSubpixelQuantizeFonts(Bool)](cgcontext/setshouldsubpixelquantizefonts(_:).md)
  Enables or disables subpixel quantization in a graphics context.
- [func showGlyphs(g: UnsafePointer<CGGlyph>?, count: Int)](cgcontext/showglyphs(g:count:).md)
  Displays an array of glyphs at the current text position.
- [func showGlyphs([CGGlyph], at: [CGPoint])](cgcontext/showglyphs(_:at:).md)
  Draws a set of glyphs at a set of corresponding positions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/showtext(string:length:))*