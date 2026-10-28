# setShouldSmoothFonts(_:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Enables or disables font smoothing in a graphics context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setShouldSmoothFonts(_ shouldSmoothFonts: Bool)
```

```c
extern void CGContextSetShouldSmoothFonts(CGContextRef c, bool shouldSmoothFonts);
```

## Discussion

There are cases, such as rendering to a bitmap, when font smoothing is not appropriate and should be disabled. Note that some contexts (such as PostScript contexts) do not support font smoothing.

This parameter is part of the graphics state. Because of this, you use this when you want to temporarily override this setting in a drawing method.

## Parameters

- `shouldSmoothFonts`: A Boolean value that specifies whether to enable font smoothing.

## See Also

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
- [func setShouldSubpixelPositionFonts(Bool)](./setshouldsubpixelpositionfonts%28_%29.md)
  Enables or disables subpixel positioning in a graphics context.
- [func setShouldSubpixelQuantizeFonts(Bool)](./setshouldsubpixelquantizefonts%28_%29.md)
  Enables or disables subpixel quantization in a graphics context.
- [func showGlyphs(g: UnsafePointer<CGGlyph>?, count: Int)](./showglyphs%28g,count%29.md)
  Displays an array of glyphs at the current text position.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/setshouldsmoothfonts(_:))*