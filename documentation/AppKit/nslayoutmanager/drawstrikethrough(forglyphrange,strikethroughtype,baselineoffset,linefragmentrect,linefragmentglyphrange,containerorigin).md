# drawStrikethrough(forGlyphRange:strikethroughType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws a strikethrough for the specified glyphs.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func drawStrikethrough(forGlyphRange glyphRange: NSRange, strikethroughType strikethroughVal: NSUnderlineStyle, baselineOffset: CGFloat, lineFragmentRect lineRect: NSRect, lineFragmentGlyphRange lineGlyphRange: NSRange, containerOrigin: NSPoint)
```

```objc
- (void) drawStrikethroughForGlyphRange:(NSRange) glyphRange strikethroughType:(NSUnderlineStyle) strikethroughVal baselineOffset:(CGFloat) baselineOffset lineFragmentRect:(NSRect) lineRect lineFragmentGlyphRange:(NSRange) lineGlyphRange containerOrigin:(NSPoint) containerOrigin;
```

#### Discussion

This method is invoked automatically by [`strikethroughGlyphRange(_:strikethroughType:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:)`](./strikethroughglyphrange%28_,strikethroughtype,linefragmentrect,linefragmentglyphrange,containerorigin%29.md); you should rarely need to invoke it directly. This method’s `strikethroughVal` parameter does not take account of any setting for[`NSUnderlineByWordMask`](../nsunderlinebywordmask.md) because that’s taken care of by [`underlineGlyphRange(_:underlineType:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:)`](./underlineglyphrange%28_,underlinetype,linefragmentrect,linefragmentglyphrange,containerorigin%29.md).

## Parameters

- `glyphRange`: The range of glyphs for which to draw a strikethrough. The range must belong to a single line fragment rectangle (as returned by [`lineFragmentRect(forGlyphAt:effectiveRange:)`](./linefragmentrect%28forglyphat,effectiverange%29.md)).
- `strikethroughVal`: The style of strikethrough to draw. This value is a mask derived from the value for [`underlineStyle`](../../Foundation/nsattributedstring/key/underlinestyle.md)—for example, `(NSUnderlinePatternDash | NSUnderlineStyleThick)`. Subclasses can define custom strikethrough styles.
- `baselineOffset`: Indicates how far above the text baseline the underline should be drawn.
- `lineRect`: The line fragment rectangle containing the glyphs to draw strikethrough for.
- `lineGlyphRange`: The range of all glyphs within `lineRect`.
- `containerOrigin`: The origin of the line fragment rectangle’s `NSTextContainer` in its `NSTextView`.

## See Also

### Drawing
- [func drawBackground(forGlyphRange: NSRange, at: NSPoint)](./drawbackground%28forglyphrange,at%29.md)
  Draws background marks for the specified glyphs, which must lie completely within a single text container.
- [func drawGlyphs(forGlyphRange: NSRange, at: NSPoint)](./drawglyphs%28forglyphrange,at%29.md)
  Draws the specified glyphs, which must lie completely within a single text container.
- [func drawUnderline(forGlyphRange: NSRange, underlineType: NSUnderlineStyle, baselineOffset: CGFloat, lineFragmentRect: NSRect, lineFragmentGlyphRange: NSRange, containerOrigin: NSPoint)](./drawunderline%28forglyphrange,underlinetype,baselineoffset,linefragmentrect,linefragmentglyphrange,containerorigin%29.md)
  Draws underlining for the glyphs in a specified range.
- [func fillBackgroundRectArray(UnsafePointer<NSRect>, count: Int, forCharacterRange: NSRange, color: NSColor)](./fillbackgroundrectarray%28_,count,forcharacterrange,color%29.md)
  Fills background rectangles with a color.
- [func showCGGlyphs(UnsafePointer<CGGlyph>, positions: UnsafePointer<CGPoint>, count: Int, font: NSFont, textMatrix: CGAffineTransform, attributes: [NSAttributedString.Key : Any], in: CGContext)](./showcgglyphs%28_,positions,count,font,textmatrix,attributes,in%29.md)
  Renders the glyphs at the specified positions, using the specified attributes.
- [func strikethroughGlyphRange(NSRange, strikethroughType: NSUnderlineStyle, lineFragmentRect: NSRect, lineFragmentGlyphRange: NSRange, containerOrigin: NSPoint)](./strikethroughglyphrange%28_,strikethroughtype,linefragmentrect,linefragmentglyphrange,containerorigin%29.md)
  Calculates and draws strikethrough for the specified glyphs.
- [func underlineGlyphRange(NSRange, underlineType: NSUnderlineStyle, lineFragmentRect: NSRect, lineFragmentGlyphRange: NSRange, containerOrigin: NSPoint)](./underlineglyphrange%28_,underlinetype,linefragmentrect,linefragmentglyphrange,containerorigin%29.md)
  Calculates subranges to underline for the specified glyphs and draws the underlining as appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/drawstrikethrough(forglyphrange:strikethroughtype:baselineoffset:linefragmentrect:linefragmentglyphrange:containerorigin:))*