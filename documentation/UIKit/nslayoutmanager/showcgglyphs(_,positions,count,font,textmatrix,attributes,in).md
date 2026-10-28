# showCGGlyphs(_:positions:count:font:textMatrix:attributes:in:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Renders the glyphs at the specified positions, using the specified attributes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func showCGGlyphs(_ glyphs: UnsafePointer<CGGlyph>, positions: UnsafePointer<CGPoint>, count glyphCount: Int, font: UIFont, textMatrix: CGAffineTransform, attributes: [NSAttributedString.Key : Any] = [:], in CGContext: CGContext)
```

```objc
- (void) showCGGlyphs:(const CGGlyph *) glyphs positions:(const CGPoint *) positions count:(NSInteger) glyphCount font:(UIFont *) font textMatrix:(CGAffineTransform) textMatrix attributes:(NSDictionary<NSString *,id> *) attributes inContext:(CGContextRef) CGContext;
```

## Discussion

The layout manager calls this primitive method when it is time to lay out a set of glyphs in the specified graphics context.

## Parameters

- `glyphs`: The glyphs to draw, which may include embedded `NULL` bytes.
- `positions`: The positions at which to draw the glyphs in the user space coordinate system.
- `glyphCount`: The number of glyphs to draw.
- `font`: The font to apply to the graphics state. This value can be different from the [`NSFontAttributeName`](../nsfontattributename.md) value in the `attributes` argument because of various font substitutions that the system automatically executes.
- `textMatrix`: The affine transform mapping the text space coordinate system to the user space coordinate system. The `tx` and `ty` components of `textMatrix` are ignored because Quartz overrides them with the glyph positions.
- `attributes`: A dictionary of glyph attributes. For a list of possible keys and values, see [Glyph Attributes](../../AppKit/glyph-attributes.md).
- `CGContext`: A graphics context object already configured with the information in the `font`, `textMatrix`, and `attributes` parameters

## See Also

### Drawing
- [func drawBackground(forGlyphRange: NSRange, at: CGPoint)](./drawbackground%28forglyphrange,at%29.md)
  Draws background marks for the specified glyphs, which must lie completely within a single text container.
- [func drawGlyphs(forGlyphRange: NSRange, at: CGPoint)](./drawglyphs%28forglyphrange,at%29.md)
  Draws the specified glyphs, which must lie completely within a single text container.
- [func drawStrikethrough(forGlyphRange: NSRange, strikethroughType: NSUnderlineStyle, baselineOffset: CGFloat, lineFragmentRect: CGRect, lineFragmentGlyphRange: NSRange, containerOrigin: CGPoint)](./drawstrikethrough%28forglyphrange,strikethroughtype,baselineoffset,linefragmentrect,linefragmentglyphrange,containerorigin%29.md)
  Draws a strikethrough for the specified glyphs.
- [func drawUnderline(forGlyphRange: NSRange, underlineType: NSUnderlineStyle, baselineOffset: CGFloat, lineFragmentRect: CGRect, lineFragmentGlyphRange: NSRange, containerOrigin: CGPoint)](./drawunderline%28forglyphrange,underlinetype,baselineoffset,linefragmentrect,linefragmentglyphrange,containerorigin%29.md)
  Draws underlining for the glyphs in a specified range.
- [func fillBackgroundRectArray(UnsafePointer<CGRect>, count: Int, forCharacterRange: NSRange, color: UIColor)](./fillbackgroundrectarray%28_,count,forcharacterrange,color%29.md)
  Fills background rectangles with a color.
- [func strikethroughGlyphRange(NSRange, strikethroughType: NSUnderlineStyle, lineFragmentRect: CGRect, lineFragmentGlyphRange: NSRange, containerOrigin: CGPoint)](./strikethroughglyphrange%28_,strikethroughtype,linefragmentrect,linefragmentglyphrange,containerorigin%29.md)
  Calculates and draws strikethrough for the specified glyphs.
- [func underlineGlyphRange(NSRange, underlineType: NSUnderlineStyle, lineFragmentRect: CGRect, lineFragmentGlyphRange: NSRange, containerOrigin: CGPoint)](./underlineglyphrange%28_,underlinetype,linefragmentrect,linefragmentglyphrange,containerorigin%29.md)
  Calculates subranges to underline for the specified glyphs and draws the underlining as appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanager/showcgglyphs(_:positions:count:font:textmatrix:attributes:in:))*