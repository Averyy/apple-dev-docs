# CGTextDrawingMode

**Framework**: Core Graphics  
**Kind**: enum

Modes for rendering text.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum CGTextDrawingMode
```

#### Overview

You provide a text drawing mode constant to the function [`setTextDrawingMode(_:)`](cgcontext/settextdrawingmode(_:).md) to set the current text drawing mode for a graphics context. Text drawing modes determine how Core Graphics renders individual glyphs onscreen. For example, you can set a text drawing mode to draw text filled in or outlined (stroked) or both. You can also create special effects with the text clipping drawing modes, such as clipping an image to a glyph shape.

## Topics

### Constants
- [CGTextDrawingMode.fill](cgtextdrawingmode/fill.md)
  Perform a fill operation on the text.
- [CGTextDrawingMode.stroke](cgtextdrawingmode/stroke.md)
  Perform a stroke operation on the text.
- [CGTextDrawingMode.fillStroke](cgtextdrawingmode/fillstroke.md)
  Perform fill, then stroke operations on the text.
- [CGTextDrawingMode.invisible](cgtextdrawingmode/invisible.md)
  Do not draw the text, but do update the text position.
- [CGTextDrawingMode.fillClip](cgtextdrawingmode/fillclip.md)
  Perform a fill operation, then intersect the text with the current clipping path.
- [CGTextDrawingMode.strokeClip](cgtextdrawingmode/strokeclip.md)
  Perform a stroke operation, then intersect the text with the current clipping path.
- [CGTextDrawingMode.fillStrokeClip](cgtextdrawingmode/fillstrokeclip.md)
  Perform fill then stroke operations, then intersect the text with the current clipping path.
- [CGTextDrawingMode.clip](cgtextdrawingmode/clip.md)
  Specifies to intersect the text with the current clipping path. This mode does not paint the text.
### Initializers
- [init?(rawValue: Int32)](cgtextdrawingmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var textMatrix: CGAffineTransform](cgcontext/textmatrix.md)
  Returns the current text matrix.
- [var textPosition: CGPoint](cgcontext/textposition.md)
  Returns the location at which text is drawn.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgtextdrawingmode)*