# showCGGlyphs(_:positions:count:font:textMatrix:attributes:in:)

**Framework**: AppKit  
**Kind**: method

Renders the glyphs at the specified positions, using the specified attributes.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func showCGGlyphs(_ glyphs: UnsafePointer<CGGlyph>, positions: UnsafePointer<CGPoint>, count glyphCount: Int, font: NSFont, textMatrix: CGAffineTransform, attributes: [NSAttributedString.Key : Any] = [:], in CGContext: CGContext)
```

#### Discussion

The layout manager calls this primitive method when it is time to lay out a set of glyphs in the specified graphics context.

## Parameters

- `glyphs`: The glyphs to draw, which may include embedded   bytes.
- `positions`: The positions at which to draw the glyphs in the user space coordinate system.
- `glyphCount`: The number of glyphs to draw.
- `font`: The font to apply to the graphics state. This value can be different from the   value in the   argument because of various font substitutions that the system automatically executes.
- `textMatrix`: The affine transform mapping the text space coordinate system to the user space coordinate system. The   and   components of   are ignored because Quartz overrides them with the glyph positions.
- `attributes`: A dictionary of glyph attributes. For a list of possible keys and values, see  .
- `CGContext`: A graphics context object already configured with the information in the  ,  , and   parameters

## See Also

- [func drawBackground(forGlyphRange: NSRange, at: NSPoint)](nslayoutmanager/drawbackground(forglyphrange:at:).md)
  Draws background marks for the specified glyphs, which must lie completely within a single text container.
- [func drawGlyphs(forGlyphRange: NSRange, at: NSPoint)](nslayoutmanager/drawglyphs(forglyphrange:at:).md)
  Draws the specified glyphs, which must lie completely within a single text container.
- [func drawStrikethrough(forGlyphRange: NSRange, strikethroughType: NSUnderlineStyle, baselineOffset: CGFloat, lineFragmentRect: NSRect, lineFragmentGlyphRange: NSRange, containerOrigin: NSPoint)](nslayoutmanager/drawstrikethrough(forglyphrange:strikethroughtype:baselineoffset:linefragmentrect:linefragmentglyphrange:containerorigin:).md)
  Draws a strikethrough for the specified glyphs.
- [func drawUnderline(forGlyphRange: NSRange, underlineType: NSUnderlineStyle, baselineOffset: CGFloat, lineFragmentRect: NSRect, lineFragmentGlyphRange: NSRange, containerOrigin: NSPoint)](nslayoutmanager/drawunderline(forglyphrange:underlinetype:baselineoffset:linefragmentrect:linefragmentglyphrange:containerorigin:).md)
  Draws underlining for the glyphs in a specified range.
- [func fillBackgroundRectArray(UnsafePointer<NSRect>, count: Int, forCharacterRange: NSRange, color: NSColor)](nslayoutmanager/fillbackgroundrectarray(_:count:forcharacterrange:color:).md)
  Fills background rectangles with a color.
- [func strikethroughGlyphRange(NSRange, strikethroughType: NSUnderlineStyle, lineFragmentRect: NSRect, lineFragmentGlyphRange: NSRange, containerOrigin: NSPoint)](nslayoutmanager/strikethroughglyphrange(_:strikethroughtype:linefragmentrect:linefragmentglyphrange:containerorigin:).md)
  Calculates and draws strikethrough for the specified glyphs.
- [func underlineGlyphRange(NSRange, underlineType: NSUnderlineStyle, lineFragmentRect: NSRect, lineFragmentGlyphRange: NSRange, containerOrigin: NSPoint)](nslayoutmanager/underlineglyphrange(_:underlinetype:linefragmentrect:linefragmentglyphrange:containerorigin:).md)
  Calculates subranges to underline for the specified glyphs and draws the underlining as appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/showcgglyphs(_:positions:count:font:textmatrix:attributes:in:))*