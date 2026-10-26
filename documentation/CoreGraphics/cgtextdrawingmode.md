# CGTextDrawingMode

**Framework**: Core Graphics  
**Kind**: enum  
**Role**: Enumeration

Modes for rendering text.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum CGTextDrawingMode
```

```c
enum CGTextDrawingMode : int32_t;
```

#### Overview

You provide a text drawing mode constant to the function [`setTextDrawingMode(_:)`](./cgcontext/settextdrawingmode%28_%29.md) to set the current text drawing mode for a graphics context. Text drawing modes determine how Core Graphics renders individual glyphs onscreen. For example, you can set a text drawing mode to draw text filled in or outlined (stroked) or both. You can also create special effects with the text clipping drawing modes, such as clipping an image to a glyph shape.

## Topics

### Constants
- [CGTextDrawingMode.fill](./cgtextdrawingmode/fill.md)
  Perform a fill operation on the text.
- [CGTextDrawingMode.stroke](./cgtextdrawingmode/stroke.md)
  Perform a stroke operation on the text.
- [CGTextDrawingMode.fillStroke](./cgtextdrawingmode/fillstroke.md)
  Perform fill, then stroke operations on the text.
- [CGTextDrawingMode.invisible](./cgtextdrawingmode/invisible.md)
  Do not draw the text, but do update the text position.
- [CGTextDrawingMode.fillClip](./cgtextdrawingmode/fillclip.md)
  Perform a fill operation, then intersect the text with the current clipping path.
- [CGTextDrawingMode.strokeClip](./cgtextdrawingmode/strokeclip.md)
  Perform a stroke operation, then intersect the text with the current clipping path.
- [CGTextDrawingMode.fillStrokeClip](./cgtextdrawingmode/fillstrokeclip.md)
  Perform fill then stroke operations, then intersect the text with the current clipping path.
- [CGTextDrawingMode.clip](./cgtextdrawingmode/clip.md)
  Specifies to intersect the text with the current clipping path. This mode does not paint the text.
### Initializers
- [init?(rawValue: Int32)](./cgtextdrawingmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Drawing Text
- [var textMatrix: CGAffineTransform](./cgcontext/textmatrix.md)
  Returns the current text matrix.
- [var textPosition: CGPoint](./cgcontext/textposition.md)
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
- [func showGlyphs([CGGlyph], at: [CGPoint])](./cgcontext/showglyphs%28_,at%29.md)
  Draws a set of glyphs at a set of corresponding positions.
- [CGContextSetTextMatrix](./cgcontextsettextmatrix.md)
  Sets the current text matrix.
- [CGContextSetTextPosition](./cgcontextsettextposition.md)
  Sets the location at which text is drawn.
- [CGContextGetTextPosition](./cgcontextgettextposition.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgtextdrawingmode)*