# boundingRect(forGlyphRange:in:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the bounding rectangle for the specified glyphs in a container.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func boundingRect(forGlyphRange glyphRange: NSRange, in container: NSTextContainer) -> CGRect
```

```objc
- (CGRect) boundingRectForGlyphRange:(NSRange) glyphRange inTextContainer:(NSTextContainer *) container;
```

## Return Value

The bounding rectangle enclosing the given range of glyphs.

## Discussion

This method returns a single bounding rectangle (in container coordinates) enclosing all glyphs and other marks drawn in the given text container for the given glyph range, including glyphs that draw outside their line fragment rectangles and text attributes such as underlining.

The range is intersected with the container’s range before computing the bounding rectangle. This method can be used to translate glyph ranges into display rectangles for invalidation and redrawing  when a range of glyphs changes. Bounding rectangles are always in container coordinates.

Performs glyph generation and layout if needed.

## Parameters

- `glyphRange`: The range of glyphs for which to return the bounding rectangle.
- `container`: The text container in which the glyphs are laid out.

## See Also

### Related Documentation
- [func drawsOutsideLineFragment(forGlyphAt: Int) -> Bool](./drawsoutsidelinefragment%28forglyphat%29.md)
  Indicates whether the glyph draws outside its line fragment rectangle.
### Performing advanced layout queries
- [func characterIndex(for: CGPoint, in: NSTextContainer, fractionOfDistanceBetweenInsertionPoints: UnsafeMutablePointer<CGFloat>?) -> Int](./characterindex%28for,in,fractionofdistancebetweeninsertionpoints%29.md)
  Returns the index of the character that lies beneath the specified point using the specified container’s coordinate system.
- [func characterRange(forGlyphRange: NSRange, actualGlyphRange: NSRangePointer?) -> NSRange](./characterrange%28forglyphrange,actualglyphrange%29.md)
  Returns the range of characters that correspond to the glyphs in the specified glyph range.
- [func enumerateEnclosingRects(forGlyphRange: NSRange, withinSelectedGlyphRange: NSRange, in: NSTextContainer, using: (CGRect, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerateenclosingrects%28forglyphrange,withinselectedglyphrange,in,using%29.md)
  Enumerates enclosing rectangles for the specified glyph range in a text container.
- [func enumerateLineFragments(forGlyphRange: NSRange, using: (CGRect, CGRect, NSTextContainer, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratelinefragments%28forglyphrange,using%29.md)
  Enumerates line fragments intersecting with the specified glyph range.
- [func fractionOfDistanceThroughGlyph(for: CGPoint, in: NSTextContainer) -> CGFloat](./fractionofdistancethroughglyph%28for,in%29.md)
  Returns the fraction of the distance between the glyph at the specified point and the next glyph.
- [func getLineFragmentInsertionPoints(forCharacterAt: Int, alternatePositions: Bool, inDisplayOrder: Bool, positions: UnsafeMutablePointer<CGFloat>?, characterIndexes: UnsafeMutablePointer<Int>?) -> Int](./getlinefragmentinsertionpoints%28forcharacterat,alternatepositions,indisplayorder,positions,characterindexes%29.md)
  Returns insertion points in bulk for a specified line fragment.
- [func glyphIndex(for: CGPoint, in: NSTextContainer) -> Int](./glyphindex%28for,in%29.md)
  Returns the index of the glyph at the specified location in a text container.
- [func glyphIndex(for: CGPoint, in: NSTextContainer, fractionOfDistanceThroughGlyph: UnsafeMutablePointer<CGFloat>?) -> Int](./glyphindex%28for,in,fractionofdistancethroughglyph%29.md)
  Returns the index of the glyph at the specified point using the container’s coordinate system.
- [func glyphRange(forBoundingRect: CGRect, in: NSTextContainer) -> NSRange](./glyphrange%28forboundingrect,in%29.md)
  Returns the smallest contiguous range for glyphs lying wholly or partially within the specified rectangle of the text container.
- [func glyphRange(forBoundingRectWithoutAdditionalLayout: CGRect, in: NSTextContainer) -> NSRange](./glyphrange%28forboundingrectwithoutadditionallayout,in%29.md)
  Returns the smallest contiguous range for glyphs lying wholly or partially within the specified rectangle of the text container.
- [func glyphRange(for: NSTextContainer) -> NSRange](./glyphrange%28for%29.md)
  Returns the range of glyphs lying within the specified text container.
- [func glyphRange(forCharacterRange: NSRange, actualCharacterRange: NSRangePointer?) -> NSRange](./glyphrange%28forcharacterrange,actualcharacterrange%29.md)
  Returns the range of glyphs that the specified range of characters generates.
- [func range(ofNominallySpacedGlyphsContaining: Int) -> NSRange](./range%28ofnominallyspacedglyphscontaining%29.md)
  Returns the range of displayable glyphs that surround the glyph at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanager/boundingrect(forglyphrange:in:))*