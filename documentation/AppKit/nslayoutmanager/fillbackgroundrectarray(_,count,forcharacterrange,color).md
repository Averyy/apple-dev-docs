# fillBackgroundRectArray(_:count:forCharacterRange:color:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Fills background rectangles with a color.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func fillBackgroundRectArray(_ rectArray: UnsafePointer<NSRect>, count rectCount: Int, forCharacterRange charRange: NSRange, color: NSColor)
```

```objc
- (void) fillBackgroundRectArray:(const NSRect *) rectArray count:(NSUInteger) rectCount forCharacterRange:(NSRange) charRange color:(NSColor *) color;
```

## Discussion

This is the primitive method used by [`drawBackground(forGlyphRange:at:)`](./drawbackground%28forglyphrange,at%29.md), providing a finer-grained override point for actually filling rectangles with a particular background color for a background color attribute, a selected or marked range highlight, a block decoration, or any other rectangle fill needed by that method. As with [`showPackedGlyphs:length:glyphRange:atPoint:font:color:printingAdjustment:`](./showpackedglyphs_length_glyphrange_atpoint_font_color_printingadjustment_.md), the `charRange` and `color` parameters are passed in merely for informational purposes; the color is already set in the graphics state. If for any reason you modify it, you must restore it before returning from this method.

This method operates in terms of character ranges, because the relevant attributes are expressed on characters, and they don’t always lie on glyph boundaries—for example, when one character of an “fi” ligature is highlighted.

You should never call this method, but you might override it. The default implementation simply fills the rectangles in the specified array. The graphics operation used for this fill is controlled by a link check; for compatibility reasons, it is [`NSCompositeCopy`](../nscompositecopy.md) for applications linked prior to OS X v10.6 and [`NSCompositeSourceOver`](../nscompositesourceover.md) for applications linked on macOS 10.6 or later. Applications can control the operation used, or modify the drawing, by overriding this method in an `NSLayoutManager` subclass.

## Parameters

- `rectArray`: The array of rectangles to fill.
- `rectCount`: The number of rectangles in `rectArray`.
- `charRange`: The range of characters whose background rectangles are filled.
- `color`: The fill color.

## See Also

### Drawing
- [func drawBackground(forGlyphRange: NSRange, at: NSPoint)](./drawbackground%28forglyphrange,at%29.md)
  Draws background marks for the specified glyphs, which must lie completely within a single text container.
- [func drawGlyphs(forGlyphRange: NSRange, at: NSPoint)](./drawglyphs%28forglyphrange,at%29.md)
  Draws the specified glyphs, which must lie completely within a single text container.
- [func drawStrikethrough(forGlyphRange: NSRange, strikethroughType: NSUnderlineStyle, baselineOffset: CGFloat, lineFragmentRect: NSRect, lineFragmentGlyphRange: NSRange, containerOrigin: NSPoint)](./drawstrikethrough%28forglyphrange,strikethroughtype,baselineoffset,linefragmentrect,linefragmentglyphrange,containerorigin%29.md)
  Draws a strikethrough for the specified glyphs.
- [func drawUnderline(forGlyphRange: NSRange, underlineType: NSUnderlineStyle, baselineOffset: CGFloat, lineFragmentRect: NSRect, lineFragmentGlyphRange: NSRange, containerOrigin: NSPoint)](./drawunderline%28forglyphrange,underlinetype,baselineoffset,linefragmentrect,linefragmentglyphrange,containerorigin%29.md)
  Draws underlining for the glyphs in a specified range.
- [func showCGGlyphs(UnsafePointer<CGGlyph>, positions: UnsafePointer<CGPoint>, count: Int, font: NSFont, textMatrix: CGAffineTransform, attributes: [NSAttributedString.Key : Any], in: CGContext)](./showcgglyphs%28_,positions,count,font,textmatrix,attributes,in%29.md)
  Renders the glyphs at the specified positions, using the specified attributes.
- [func strikethroughGlyphRange(NSRange, strikethroughType: NSUnderlineStyle, lineFragmentRect: NSRect, lineFragmentGlyphRange: NSRange, containerOrigin: NSPoint)](./strikethroughglyphrange%28_,strikethroughtype,linefragmentrect,linefragmentglyphrange,containerorigin%29.md)
  Calculates and draws strikethrough for the specified glyphs.
- [func underlineGlyphRange(NSRange, underlineType: NSUnderlineStyle, lineFragmentRect: NSRect, lineFragmentGlyphRange: NSRange, containerOrigin: NSPoint)](./underlineglyphrange%28_,underlinetype,linefragmentrect,linefragmentglyphrange,containerorigin%29.md)
  Calculates subranges to underline for the specified glyphs and draws the underlining as appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/fillbackgroundrectarray(_:count:forcharacterrange:color:))*