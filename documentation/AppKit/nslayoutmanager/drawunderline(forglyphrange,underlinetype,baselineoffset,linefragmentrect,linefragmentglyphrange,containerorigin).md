# drawUnderline(forGlyphRange:underlineType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws underlining for the glyphs in a specified range.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func drawUnderline(forGlyphRange glyphRange: NSRange, underlineType underlineVal: NSUnderlineStyle, baselineOffset: CGFloat, lineFragmentRect lineRect: NSRect, lineFragmentGlyphRange lineGlyphRange: NSRange, containerOrigin: NSPoint)
```

```objc
- (void) drawUnderlineForGlyphRange:(NSRange) glyphRange underlineType:(NSUnderlineStyle) underlineVal baselineOffset:(CGFloat) baselineOffset lineFragmentRect:(NSRect) lineRect lineFragmentGlyphRange:(NSRange) lineGlyphRange containerOrigin:(NSPoint) containerOrigin;
```

#### Discussion

This method is invoked automatically by [`underlineGlyphRange(_:underlineType:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:)`](./underlineglyphrange%28_,underlinetype,linefragmentrect,linefragmentglyphrange,containerorigin%29.md); you should rarely need to invoke it directly. This method’s `underlineVal` parameter does not take account of any setting for[`NSUnderlineByWordMask`](../nsunderlinebywordmask.md) because that’s taken care of by [`underlineGlyphRange(_:underlineType:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:)`](./underlineglyphrange%28_,underlinetype,linefragmentrect,linefragmentglyphrange,containerorigin%29.md).

## Parameters

- `glyphRange`: A range of glyphs, which must belong to a single line fragment rectangle (as returned by [`lineFragmentRect(forGlyphAt:effectiveRange:)`](./linefragmentrect%28forglyphat,effectiverange%29.md)).
- `underlineVal`: The style of underlining to draw. This value is a mask derived from the value for [`underlineStyle`](../../Foundation/nsattributedstring/key/underlinestyle.md)—for example, `(NSUnderlinePatternDash | NSUnderlineStyleThick)`. Subclasses can define custom underlining styles.
- `baselineOffset`: Specifies the distance from the bottom of the bounding box of the specified glyphs in the specified range to their baseline.
- `lineRect`: The line fragment rectangle containing the glyphs to draw underlining for.
- `lineGlyphRange`: The range of all glyphs within `lineRect`.
- `containerOrigin`: The origin of the `lineRectNSTextContainer` in its `NSTextView`.

## See Also

### Drawing
- [func drawBackground(forGlyphRange: NSRange, at: NSPoint)](./drawbackground%28forglyphrange,at%29.md)
  Draws background marks for the specified glyphs, which must lie completely within a single text container.
- [func drawGlyphs(forGlyphRange: NSRange, at: NSPoint)](./drawglyphs%28forglyphrange,at%29.md)
  Draws the specified glyphs, which must lie completely within a single text container.
- [func drawStrikethrough(forGlyphRange: NSRange, strikethroughType: NSUnderlineStyle, baselineOffset: CGFloat, lineFragmentRect: NSRect, lineFragmentGlyphRange: NSRange, containerOrigin: NSPoint)](./drawstrikethrough%28forglyphrange,strikethroughtype,baselineoffset,linefragmentrect,linefragmentglyphrange,containerorigin%29.md)
  Draws a strikethrough for the specified glyphs.
- [func fillBackgroundRectArray(UnsafePointer<NSRect>, count: Int, forCharacterRange: NSRange, color: NSColor)](./fillbackgroundrectarray%28_,count,forcharacterrange,color%29.md)
  Fills background rectangles with a color.
- [func showCGGlyphs(UnsafePointer<CGGlyph>, positions: UnsafePointer<CGPoint>, count: Int, font: NSFont, textMatrix: CGAffineTransform, attributes: [NSAttributedString.Key : Any], in: CGContext)](./showcgglyphs%28_,positions,count,font,textmatrix,attributes,in%29.md)
  Renders the glyphs at the specified positions, using the specified attributes.
- [func strikethroughGlyphRange(NSRange, strikethroughType: NSUnderlineStyle, lineFragmentRect: NSRect, lineFragmentGlyphRange: NSRange, containerOrigin: NSPoint)](./strikethroughglyphrange%28_,strikethroughtype,linefragmentrect,linefragmentglyphrange,containerorigin%29.md)
  Calculates and draws strikethrough for the specified glyphs.
- [func underlineGlyphRange(NSRange, underlineType: NSUnderlineStyle, lineFragmentRect: NSRect, lineFragmentGlyphRange: NSRange, containerOrigin: NSPoint)](./underlineglyphrange%28_,underlinetype,linefragmentrect,linefragmentglyphrange,containerorigin%29.md)
  Calculates subranges to underline for the specified glyphs and draws the underlining as appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/drawunderline(forglyphrange:underlinetype:baselineoffset:linefragmentrect:linefragmentglyphrange:containerorigin:))*