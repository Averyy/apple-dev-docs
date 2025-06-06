# drawStrikethrough(forGlyphRange:strikethroughType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:)

**Framework**: UIKit  
**Kind**: method

Draws a strikethrough for the specified glyphs.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func drawStrikethrough(forGlyphRange glyphRange: NSRange, strikethroughType strikethroughVal: NSUnderlineStyle, baselineOffset: CGFloat, lineFragmentRect lineRect: CGRect, lineFragmentGlyphRange lineGlyphRange: NSRange, containerOrigin: CGPoint)
```

#### Discussion

This method is invoked automatically by [`strikethroughGlyphRange(_:strikethroughType:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:)`](nslayoutmanager/strikethroughglyphrange(_:strikethroughtype:linefragmentrect:linefragmentglyphrange:containerorigin:).md); you should rarely need to invoke it directly. This method’s `strikethroughVal` parameter does not take account of any setting for[`NSUnderlineByWordMask`](https://developer.apple.com/documentation/AppKit/NSUnderlineByWordMask) because that’s taken care of by [`underlineGlyphRange(_:underlineType:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:)`](nslayoutmanager/underlineglyphrange(_:underlinetype:linefragmentrect:linefragmentglyphrange:containerorigin:).md).

## Parameters

- `glyphRange`: The range of glyphs for which to draw a strikethrough. The range must belong to a single line fragment rectangle (as returned by  ).
- `strikethroughVal`: The style of strikethrough to draw. This value is a mask derived from the value for  —for example,  . Subclasses can define custom strikethrough styles.
- `baselineOffset`: Indicates how far above the text baseline the underline should be drawn.
- `lineRect`: The line fragment rectangle containing the glyphs to draw strikethrough for.
- `lineGlyphRange`: The range of all glyphs within  .
- `containerOrigin`: The origin of the line fragment rectangle’s   in its  .

## See Also

- [func drawBackground(forGlyphRange: NSRange, at: CGPoint)](nslayoutmanager/drawbackground(forglyphrange:at:).md)
  Draws background marks for the specified glyphs, which must lie completely within a single text container.
- [func drawGlyphs(forGlyphRange: NSRange, at: CGPoint)](nslayoutmanager/drawglyphs(forglyphrange:at:).md)
  Draws the specified glyphs, which must lie completely within a single text container.
- [func drawUnderline(forGlyphRange: NSRange, underlineType: NSUnderlineStyle, baselineOffset: CGFloat, lineFragmentRect: CGRect, lineFragmentGlyphRange: NSRange, containerOrigin: CGPoint)](nslayoutmanager/drawunderline(forglyphrange:underlinetype:baselineoffset:linefragmentrect:linefragmentglyphrange:containerorigin:).md)
  Draws underlining for the glyphs in a specified range.
- [func fillBackgroundRectArray(UnsafePointer<CGRect>, count: Int, forCharacterRange: NSRange, color: UIColor)](nslayoutmanager/fillbackgroundrectarray(_:count:forcharacterrange:color:).md)
  Fills background rectangles with a color.
- [func showCGGlyphs(UnsafePointer<CGGlyph>, positions: UnsafePointer<CGPoint>, count: Int, font: UIFont, textMatrix: CGAffineTransform, attributes: [NSAttributedString.Key : Any], in: CGContext)](nslayoutmanager/showcgglyphs(_:positions:count:font:textmatrix:attributes:in:).md)
  Renders the glyphs at the specified positions, using the specified attributes.
- [func strikethroughGlyphRange(NSRange, strikethroughType: NSUnderlineStyle, lineFragmentRect: CGRect, lineFragmentGlyphRange: NSRange, containerOrigin: CGPoint)](nslayoutmanager/strikethroughglyphrange(_:strikethroughtype:linefragmentrect:linefragmentglyphrange:containerorigin:).md)
  Calculates and draws strikethrough for the specified glyphs.
- [func underlineGlyphRange(NSRange, underlineType: NSUnderlineStyle, lineFragmentRect: CGRect, lineFragmentGlyphRange: NSRange, containerOrigin: CGPoint)](nslayoutmanager/underlineglyphrange(_:underlinetype:linefragmentrect:linefragmentglyphrange:containerorigin:).md)
  Calculates subranges to underline for the specified glyphs and draws the underlining as appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanager/drawstrikethrough(forglyphrange:strikethroughtype:baselineoffset:linefragmentrect:linefragmentglyphrange:containerorigin:))*