# drawStrikethrough(forGlyphRange:strikethroughType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Draws a strikethrough for the specified glyphs.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func drawStrikethrough(forGlyphRange glyphRange: NSRange, strikethroughType strikethroughVal: NSUnderlineStyle, baselineOffset: CGFloat, lineFragmentRect lineRect: CGRect, lineFragmentGlyphRange lineGlyphRange: NSRange, containerOrigin: CGPoint)
```

```objc
- (void) drawStrikethroughForGlyphRange:(NSRange) glyphRange strikethroughType:(NSUnderlineStyle) strikethroughVal baselineOffset:(CGFloat) baselineOffset lineFragmentRect:(CGRect) lineRect lineFragmentGlyphRange:(NSRange) lineGlyphRange containerOrigin:(CGPoint) containerOrigin;
```

## Discussion

This method is invoked automatically by [`strikethroughGlyphRange(_:strikethroughType:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:)`](./strikethroughglyphrange%28_,strikethroughtype,linefragmentrect,linefragmentglyphrange,containerorigin%29.md); you should rarely need to invoke it directly. This method’s `strikethroughVal` parameter does not take account of any setting for[`NSUnderlineByWordMask`](../../AppKit/nsunderlinebywordmask.md) because that’s taken care of by [`underlineGlyphRange(_:underlineType:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:)`](./underlineglyphrange%28_,underlinetype,linefragmentrect,linefragmentglyphrange,containerorigin%29.md).

## Parameters

- `glyphRange`: The range of glyphs for which to draw a strikethrough. The range must belong to a single line fragment rectangle (as returned by [`lineFragmentRect(forGlyphAt:effectiveRange:)`](./linefragmentrect%28forglyphat,effectiverange%29.md)).
- `strikethroughVal`: The style of strikethrough to draw. This value is a mask derived from the value for [`NSUnderlineStyleAttributeName`](../nsunderlinestyleattributename.md)—for example, `(NSUnderlinePatternDash | NSUnderlineStyleThick)`. Subclasses can define custom strikethrough styles.
- `baselineOffset`: Indicates how far above the text baseline the underline should be drawn.
- `lineRect`: The line fragment rectangle containing the glyphs to draw strikethrough for.
- `lineGlyphRange`: The range of all glyphs within `lineRect`.
- `containerOrigin`: The origin of the line fragment rectangle’s `NSTextContainer` in its `NSTextView`.

## See Also

### Drawing
- [func drawBackground(forGlyphRange: NSRange, at: CGPoint)](./drawbackground%28forglyphrange,at%29.md)
  Draws background marks for the specified glyphs, which must lie completely within a single text container.
- [func drawGlyphs(forGlyphRange: NSRange, at: CGPoint)](./drawglyphs%28forglyphrange,at%29.md)
  Draws the specified glyphs, which must lie completely within a single text container.
- [func drawUnderline(forGlyphRange: NSRange, underlineType: NSUnderlineStyle, baselineOffset: CGFloat, lineFragmentRect: CGRect, lineFragmentGlyphRange: NSRange, containerOrigin: CGPoint)](./drawunderline%28forglyphrange,underlinetype,baselineoffset,linefragmentrect,linefragmentglyphrange,containerorigin%29.md)
  Draws underlining for the glyphs in a specified range.
- [func fillBackgroundRectArray(UnsafePointer<CGRect>, count: Int, forCharacterRange: NSRange, color: UIColor)](./fillbackgroundrectarray%28_,count,forcharacterrange,color%29.md)
  Fills background rectangles with a color.
- [func showCGGlyphs(UnsafePointer<CGGlyph>, positions: UnsafePointer<CGPoint>, count: Int, font: UIFont, textMatrix: CGAffineTransform, attributes: [NSAttributedString.Key : Any], in: CGContext)](./showcgglyphs%28_,positions,count,font,textmatrix,attributes,in%29.md)
  Renders the glyphs at the specified positions, using the specified attributes.
- [func strikethroughGlyphRange(NSRange, strikethroughType: NSUnderlineStyle, lineFragmentRect: CGRect, lineFragmentGlyphRange: NSRange, containerOrigin: CGPoint)](./strikethroughglyphrange%28_,strikethroughtype,linefragmentrect,linefragmentglyphrange,containerorigin%29.md)
  Calculates and draws strikethrough for the specified glyphs.
- [func underlineGlyphRange(NSRange, underlineType: NSUnderlineStyle, lineFragmentRect: CGRect, lineFragmentGlyphRange: NSRange, containerOrigin: CGPoint)](./underlineglyphrange%28_,underlinetype,linefragmentrect,linefragmentglyphrange,containerorigin%29.md)
  Calculates subranges to underline for the specified glyphs and draws the underlining as appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanager/drawstrikethrough(forglyphrange:strikethroughtype:baselineoffset:linefragmentrect:linefragmentglyphrange:containerorigin:))*