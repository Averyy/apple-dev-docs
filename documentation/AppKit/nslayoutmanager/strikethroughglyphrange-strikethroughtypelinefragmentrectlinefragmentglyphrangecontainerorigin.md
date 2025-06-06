# strikethroughGlyphRange(_:strikethroughType:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:)

**Framework**: AppKit  
**Kind**: method

Calculates and draws strikethrough for the specified glyphs.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func strikethroughGlyphRange(_ glyphRange: NSRange, strikethroughType strikethroughVal: NSUnderlineStyle, lineFragmentRect lineRect: NSRect, lineFragmentGlyphRange lineGlyphRange: NSRange, containerOrigin: NSPoint)
```

#### Discussion

This method determines which glyphs actually need to have a strikethrough drawn based on `strikethroughVal`. After determining which glyphs to draw strikethrough on, this method invokes [`drawStrikethrough(forGlyphRange:strikethroughType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:)`](nslayoutmanager/drawstrikethrough(forglyphrange:strikethroughtype:baselineoffset:linefragmentrect:linefragmentglyphrange:containerorigin:).md) for each contiguous range of glyphs that requires it.

## Parameters

- `glyphRange`: The range of glyphs for which to draw a strikethrough. The range must belong to a single line fragment rectangle (as returned by  ).
- `strikethroughVal`: The style of underlining to draw. This value is a mask derived from the value for  —for example,  . Subclasses can define custom underlining styles.
- `lineRect`: The line fragment rectangle containing the glyphs to draw strikethrough for.
- `lineGlyphRange`: The range of all glyphs within  .
- `containerOrigin`: The origin of the line fragment rectangle’s   in its  .

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
- [func showCGGlyphs(UnsafePointer<CGGlyph>, positions: UnsafePointer<CGPoint>, count: Int, font: NSFont, textMatrix: CGAffineTransform, attributes: [NSAttributedString.Key : Any], in: CGContext)](nslayoutmanager/showcgglyphs(_:positions:count:font:textmatrix:attributes:in:).md)
  Renders the glyphs at the specified positions, using the specified attributes.
- [func underlineGlyphRange(NSRange, underlineType: NSUnderlineStyle, lineFragmentRect: NSRect, lineFragmentGlyphRange: NSRange, containerOrigin: NSPoint)](nslayoutmanager/underlineglyphrange(_:underlinetype:linefragmentrect:linefragmentglyphrange:containerorigin:).md)
  Calculates subranges to underline for the specified glyphs and draws the underlining as appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/strikethroughglyphrange(_:strikethroughtype:linefragmentrect:linefragmentglyphrange:containerorigin:))*