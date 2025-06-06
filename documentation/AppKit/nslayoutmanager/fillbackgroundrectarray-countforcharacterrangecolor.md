# fillBackgroundRectArray(_:count:forCharacterRange:color:)

**Framework**: AppKit  
**Kind**: method

Fills background rectangles with a color.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func fillBackgroundRectArray(_ rectArray: UnsafePointer<NSRect>, count rectCount: Int, forCharacterRange charRange: NSRange, color: NSColor)
```

#### Discussion

This is the primitive method used by [`drawBackground(forGlyphRange:at:)`](nslayoutmanager/drawbackground(forglyphrange:at:).md), providing a finer-grained override point for actually filling rectangles with a particular background color for a background color attribute, a selected or marked range highlight, a block decoration, or any other rectangle fill needed by that method. As with [`showPackedGlyphs:length:glyphRange:atPoint:font:color:printingAdjustment:`](nslayoutmanager/showpackedglyphs:length:glyphrange:atpoint:font:color:printingadjustment:.md), the `charRange` and `color` parameters are passed in merely for informational purposes; the color is already set in the graphics state. If for any reason you modify it, you must restore it before returning from this method.

This method operates in terms of character ranges, because the relevant attributes are expressed on characters, and they don’t always lie on glyph boundaries—for example, when one character of an “fi” ligature is highlighted.

You should never call this method, but you might override it. The default implementation simply fills the rectangles in the specified array. The graphics operation used for this fill is controlled by a link check; for compatibility reasons, it is [`NSCompositeCopy`](nscompositecopy.md) for applications linked prior to OS X v10.6 and [`NSCompositeSourceOver`](nscompositesourceover.md) for applications linked on macOS 10.6 or later. Applications can control the operation used, or modify the drawing, by overriding this method in an `NSLayoutManager` subclass.

## Parameters

- `rectArray`: The array of rectangles to fill.
- `rectCount`: The number of rectangles in  .
- `charRange`: The range of characters whose background rectangles are filled.
- `color`: The fill color.

## See Also

- [func drawBackground(forGlyphRange: NSRange, at: NSPoint)](nslayoutmanager/drawbackground(forglyphrange:at:).md)
  Draws background marks for the specified glyphs, which must lie completely within a single text container.
- [func drawGlyphs(forGlyphRange: NSRange, at: NSPoint)](nslayoutmanager/drawglyphs(forglyphrange:at:).md)
  Draws the specified glyphs, which must lie completely within a single text container.
- [func drawStrikethrough(forGlyphRange: NSRange, strikethroughType: NSUnderlineStyle, baselineOffset: CGFloat, lineFragmentRect: NSRect, lineFragmentGlyphRange: NSRange, containerOrigin: NSPoint)](nslayoutmanager/drawstrikethrough(forglyphrange:strikethroughtype:baselineoffset:linefragmentrect:linefragmentglyphrange:containerorigin:).md)
  Draws a strikethrough for the specified glyphs.
- [func drawUnderline(forGlyphRange: NSRange, underlineType: NSUnderlineStyle, baselineOffset: CGFloat, lineFragmentRect: NSRect, lineFragmentGlyphRange: NSRange, containerOrigin: NSPoint)](nslayoutmanager/drawunderline(forglyphrange:underlinetype:baselineoffset:linefragmentrect:linefragmentglyphrange:containerorigin:).md)
  Draws underlining for the glyphs in a specified range.
- [func showCGGlyphs(UnsafePointer<CGGlyph>, positions: UnsafePointer<CGPoint>, count: Int, font: NSFont, textMatrix: CGAffineTransform, attributes: [NSAttributedString.Key : Any], in: CGContext)](nslayoutmanager/showcgglyphs(_:positions:count:font:textmatrix:attributes:in:).md)
  Renders the glyphs at the specified positions, using the specified attributes.
- [func strikethroughGlyphRange(NSRange, strikethroughType: NSUnderlineStyle, lineFragmentRect: NSRect, lineFragmentGlyphRange: NSRange, containerOrigin: NSPoint)](nslayoutmanager/strikethroughglyphrange(_:strikethroughtype:linefragmentrect:linefragmentglyphrange:containerorigin:).md)
  Calculates and draws strikethrough for the specified glyphs.
- [func underlineGlyphRange(NSRange, underlineType: NSUnderlineStyle, lineFragmentRect: NSRect, lineFragmentGlyphRange: NSRange, containerOrigin: NSPoint)](nslayoutmanager/underlineglyphrange(_:underlinetype:linefragmentrect:linefragmentglyphrange:containerorigin:).md)
  Calculates subranges to underline for the specified glyphs and draws the underlining as appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/fillbackgroundrectarray(_:count:forcharacterrange:color:))*