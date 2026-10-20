# underlineGlyphRange(_:underlineType:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Calculates subranges to underline for the specified glyphs and draws the underlining as appropriate.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func underlineGlyphRange(_ glyphRange: NSRange, underlineType underlineVal: NSUnderlineStyle, lineFragmentRect lineRect: NSRect, lineFragmentGlyphRange lineGlyphRange: NSRange, containerOrigin: NSPoint)
```

```objc
- (void) underlineGlyphRange:(NSRange) glyphRange underlineType:(NSUnderlineStyle) underlineVal lineFragmentRect:(NSRect) lineRect lineFragmentGlyphRange:(NSRange) lineGlyphRange containerOrigin:(NSPoint) containerOrigin;
```

#### Discussion

This method determines which glyphs actually need to be underlined based on `underlineVal`. With `NSUnderlineStyleSingle`, for example, leading and trailing whitespace isn’t underlined, but whitespace between visible glyphs is. A potential word-underline style would omit underlining on any whitespace. After determining which glyphs to draw underlining on, this method invokes [`drawUnderline(forGlyphRange:underlineType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:)`](./drawunderline%28forglyphrange,underlinetype,baselineoffset,linefragmentrect,linefragmentglyphrange,containerorigin%29.md) for each contiguous range of glyphs that requires it.

## Parameters

- `glyphRange`: A range of glyphs, which must belong to a single line fragment rectangle (as returned by [`lineFragmentRect(forGlyphAt:effectiveRange:)`](./linefragmentrect%28forglyphat,effectiverange%29.md)).
- `underlineVal`: The style of underlining to draw. This value is a mask derived from the value for [`underlineStyle`](../../Foundation/nsattributedstring/key/underlinestyle.md)—for example, `(NSUnderlinePatternDash | NSUnderlineStyleThick | NSUnderlineByWordMask)`. Subclasses can define custom underlining styles.
- `lineRect`: The line fragment rectangle containing the glyphs to draw underlining for.
- `lineGlyphRange`: The range of all glyphs within that line fragment rectangle.
- `containerOrigin`: The origin of the line fragment rectangle’s `NSTextContainer` in its `NSTextView`.

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
- [func fillBackgroundRectArray(UnsafePointer<NSRect>, count: Int, forCharacterRange: NSRange, color: NSColor)](./fillbackgroundrectarray%28_,count,forcharacterrange,color%29.md)
  Fills background rectangles with a color.
- [func showCGGlyphs(UnsafePointer<CGGlyph>, positions: UnsafePointer<CGPoint>, count: Int, font: NSFont, textMatrix: CGAffineTransform, attributes: [NSAttributedString.Key : Any], in: CGContext)](./showcgglyphs%28_,positions,count,font,textmatrix,attributes,in%29.md)
  Renders the glyphs at the specified positions, using the specified attributes.
- [func strikethroughGlyphRange(NSRange, strikethroughType: NSUnderlineStyle, lineFragmentRect: NSRect, lineFragmentGlyphRange: NSRange, containerOrigin: NSPoint)](./strikethroughglyphrange%28_,strikethroughtype,linefragmentrect,linefragmentglyphrange,containerorigin%29.md)
  Calculates and draws strikethrough for the specified glyphs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/underlineglyphrange(_:underlinetype:linefragmentrect:linefragmentglyphrange:containerorigin:))*