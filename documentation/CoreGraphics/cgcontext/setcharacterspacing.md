# setCharacterSpacing(_:)

**Framework**: Core Graphics  
**Kind**: method

Sets the current character spacing.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setCharacterSpacing(_ spacing: CGFloat)
```

#### Discussion

Core Graphics adds the additional space to the advance between the origin of one character and the origin of the next character. For information about the text coordinate system, see [`CGContextSetTextMatrix`](cgcontextsettextmatrix.md).

## Parameters

- `spacing`: A value that represents the amount of additional space to place between glyphs, in text space coordinates.

## See Also

- [var textMatrix: CGAffineTransform](cgcontext/textmatrix.md)
  Returns the current text matrix.
- [var textPosition: CGPoint](cgcontext/textposition.md)
- [func selectFont(name: UnsafePointer<CChar>, size: CGFloat, textEncoding: CGTextEncoding)](cgcontext/selectfont(name:size:textencoding:).md)
  Sets the font and font size in a graphics context.
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
- [func showGlyphsAtPoint(x: CGFloat, y: CGFloat, glyphs: UnsafePointer<CGGlyph>?, count: Int)](cgcontext/showglyphsatpoint(x:y:glyphs:count:).md)
  Displays an array of glyphs at a position you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/setcharacterspacing(_:))*