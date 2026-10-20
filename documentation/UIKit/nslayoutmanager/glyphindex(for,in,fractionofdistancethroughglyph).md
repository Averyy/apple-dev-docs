# glyphIndex(for:in:fractionOfDistanceThroughGlyph:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the index of the glyph at the specified point using the container’s coordinate system.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func glyphIndex(for point: CGPoint, in container: NSTextContainer, fractionOfDistanceThroughGlyph partialFraction: UnsafeMutablePointer<CGFloat>?) -> Int
```

```objc
- (NSUInteger) glyphIndexForPoint:(CGPoint) point inTextContainer:(NSTextContainer *) container fractionOfDistanceThroughGlyph:(CGFloat *) partialFraction;
```

#### Return Value

The index of the glyph falling under the given point, expressed in the given container’s coordinate system.

#### Discussion

If no glyph is under `point`, the nearest glyph is returned, where nearest is defined according to the requirements of selection by mouse. Clients who wish to determine whether the the point actually lies within the bounds of the glyph returned should follow this with a call to [`boundingRect(forGlyphRange:in:)`](./boundingrect%28forglyphrange,in%29.md) and test whether the point falls in the rectangle returned by that method. If `partialFraction` is non-NULL, it returns by reference the fraction of the distance between the location of the glyph returned and the location of the next glyph.

For purposes such as dragging out a selection or placing the insertion point, a partial percentage less than or equal to 0.5 indicates that `point` should be considered as falling before the glyph index returned; a partial percentage greater than 0.5 indicates that it should be considered as falling after the glyph index returned. If the nearest glyph doesn’t lie under `point` at all (for example, if `point` is beyond the beginning or end of a line), this ratio is 0 or 1.

If the glyph stream contains the glyphs “A” and “b”, with the width of “A” being 13 points, and the user clicks at a location 8 points into “A”, `partialFraction` is 8/13, or 0.615. In this case, the point given should be considered as falling between “A” and “b” for purposes such as dragging out a selection or placing the insertion point.

Performs glyph generation and layout if needed.

As part of its implementation, this method calls [`fractionOfDistanceThroughGlyph(for:in:)`](./fractionofdistancethroughglyph%28for,in%29.md) and [`glyphIndex(for:in:)`](./glyphindex%28for,in%29.md). To change this method’s behavior, override those two methods instead of this one.

## Parameters

- `point`: The point for which to return the glyph, in coordinates of `container`.
- `container`: The container in which the returned glyph is laid out.
- `partialFraction`: If not `NULL`, on output, the fraction of the distance between the location of the glyph returned and the location of the next glyph.

## See Also

### Performing advanced layout queries
- [func boundingRect(forGlyphRange: NSRange, in: NSTextContainer) -> CGRect](./boundingrect%28forglyphrange,in%29.md)
  Returns the bounding rectangle for the specified glyphs in a container.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanager/glyphindex(for:in:fractionofdistancethroughglyph:))*