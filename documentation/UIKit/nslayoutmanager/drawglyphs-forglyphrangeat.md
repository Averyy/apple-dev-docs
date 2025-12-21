# drawGlyphs(forGlyphRange:at:)

**Framework**: UIKit  
**Kind**: method

Draws the specified glyphs, which must lie completely within a single text container.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func drawGlyphs(forGlyphRange glyphsToShow: NSRange, at origin: CGPoint)
```

#### Discussion

This method is called by `NSTextView` for drawing. You can override it to perform additional drawing, or to replace text drawing entirely, but not to change layout. You can call this method directly, but focus must already be locked on the destination view or image. This method expects the coordinate system of the view to be flipped.

This method draws the actual glyphs, including attachments, as well as any underlines or strikethoughs.

Performs glyph generation and layout if needed.

## Parameters

- `glyphsToShow`: The range of glyphs that are drawn.
- `origin`: The position of the text container in the coordinate system of the currently focused view.

## See Also

- [var textContainerOrigin: NSPoint](../AppKit/NSTextView/textContainerOrigin.md)
  The origin of the receiver’s text container.
- [func glyphRange(for: NSTextContainer) -> NSRange](nslayoutmanager/glyphrange(for:).md)
  Returns the range of glyphs lying within the specified text container.
- [func drawBackground(forGlyphRange: NSRange, at: CGPoint)](nslayoutmanager/drawbackground(forglyphrange:at:).md)
  Draws background marks for the specified glyphs, which must lie completely within a single text container.
- [func drawStrikethrough(forGlyphRange: NSRange, strikethroughType: NSUnderlineStyle, baselineOffset: CGFloat, lineFragmentRect: CGRect, lineFragmentGlyphRange: NSRange, containerOrigin: CGPoint)](nslayoutmanager/drawstrikethrough(forglyphrange:strikethroughtype:baselineoffset:linefragmentrect:linefragmentglyphrange:containerorigin:).md)
  Draws a strikethrough for the specified glyphs.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanager/drawglyphs(forglyphrange:at:))*