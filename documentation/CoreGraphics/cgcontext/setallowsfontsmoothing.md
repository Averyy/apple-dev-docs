# setAllowsFontSmoothing(_:)

**Framework**: Core Graphics  
**Kind**: method

Sets whether or not to allow font smoothing for a graphics context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setAllowsFontSmoothing(_ allowsFontSmoothing: Bool)
```

#### Discussion

Font are smoothed if they are antialiased when drawn and if font smoothing is both allowed and enabled. For information on how to enable font smoothing, see the [`setShouldSmoothFonts(_:)`](cgcontext/setshouldsmoothfonts(_:).md) function. It is not usually necessary to make changes to both parameters at the same time; either can be used to disable font smoothing.

This parameter is not part of the graphics state.

## Parameters

- `allowsFontSmoothing`: A Boolean value that specifies whether font smoothing is allowed in the specified context.

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/setallowsfontsmoothing(_:))*