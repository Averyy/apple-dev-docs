# glyphIndex(for:in:fractionOfDistanceThroughGlyph:)

**Framework**: AppKit  
**Kind**: method

Returns the index of the glyph at the specified point using the container’s coordinate system.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func glyphIndex(for point: NSPoint, in container: NSTextContainer, fractionOfDistanceThroughGlyph partialFraction: UnsafeMutablePointer<CGFloat>?) -> Int
```

#### Return Value

The index of the glyph falling under the given point, expressed in the given container’s coordinate system.

#### Discussion

If no glyph is under `point`, the nearest glyph is returned, where nearest is defined according to the requirements of selection by mouse. Clients who wish to determine whether the the point actually lies within the bounds of the glyph returned should follow this with a call to [`boundingRect(forGlyphRange:in:)`](nslayoutmanager/boundingrect(forglyphrange:in:).md) and test whether the point falls in the rectangle returned by that method. If `partialFraction` is non-NULL, it returns by reference the fraction of the distance between the location of the glyph returned and the location of the next glyph.

For purposes such as dragging out a selection or placing the insertion point, a partial percentage less than or equal to 0.5 indicates that `point` should be considered as falling before the glyph index returned; a partial percentage greater than 0.5 indicates that it should be considered as falling after the glyph index returned. If the nearest glyph doesn’t lie under `point` at all (for example, if `point` is beyond the beginning or end of a line), this ratio is 0 or 1.

If the glyph stream contains the glyphs “A” and “b”, with the width of “A” being 13 points, and the user clicks at a location 8 points into “A”, `partialFraction` is 8/13, or 0.615. In this case, the point given should be considered as falling between “A” and “b” for purposes such as dragging out a selection or placing the insertion point.

Performs glyph generation and layout if needed.

As part of its implementation, this method calls [`fractionOfDistanceThroughGlyph(for:in:)`](nslayoutmanager/fractionofdistancethroughglyph(for:in:).md) and [`glyphIndex(for:in:)`](nslayoutmanager/glyphindex(for:in:).md). To change this method’s behavior, override those two methods instead of this one.

## Parameters

- `point`: The point for which to return the glyph, in coordinates of  .
- `container`: The container in which the returned glyph is laid out.
- `partialFraction`: If not  , on output, the fraction of the distance between the location of the glyph returned and the location of the next glyph.

## See Also

- [func boundingRect(forGlyphRange: NSRange, in: NSTextContainer) -> NSRect](nslayoutmanager/boundingrect(forglyphrange:in:).md)
  Returns the bounding rectangle for the specified glyphs in a container.
- [func characterIndex(for: NSPoint, in: NSTextContainer, fractionOfDistanceBetweenInsertionPoints: UnsafeMutablePointer<CGFloat>?) -> Int](nslayoutmanager/characterindex(for:in:fractionofdistancebetweeninsertionpoints:).md)
  Returns the index of the character that lies beneath the specified point using the specified container’s coordinate system.
- [func characterRange(forGlyphRange: NSRange, actualGlyphRange: NSRangePointer?) -> NSRange](nslayoutmanager/characterrange(forglyphrange:actualglyphrange:).md)
  Returns the range of characters that correspond to the glyphs in the specified glyph range.
- [func enumerateEnclosingRects(forGlyphRange: NSRange, withinSelectedGlyphRange: NSRange, in: NSTextContainer, using: (NSRect, UnsafeMutablePointer<ObjCBool>) -> Void)](nslayoutmanager/enumerateenclosingrects(forglyphrange:withinselectedglyphrange:in:using:).md)
  Enumerates enclosing rectangles for the specified glyph range in a text container.
- [func enumerateLineFragments(forGlyphRange: NSRange, using: (NSRect, NSRect, NSTextContainer, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nslayoutmanager/enumeratelinefragments(forglyphrange:using:).md)
  Enumerates line fragments intersecting with the specified glyph range.
- [func fractionOfDistanceThroughGlyph(for: NSPoint, in: NSTextContainer) -> CGFloat](nslayoutmanager/fractionofdistancethroughglyph(for:in:).md)
  Returns the fraction of the distance between the glyph at the specified point and the next glyph.
- [func getLineFragmentInsertionPoints(forCharacterAt: Int, alternatePositions: Bool, inDisplayOrder: Bool, positions: UnsafeMutablePointer<CGFloat>?, characterIndexes: UnsafeMutablePointer<Int>?) -> Int](nslayoutmanager/getlinefragmentinsertionpoints(forcharacterat:alternatepositions:indisplayorder:positions:characterindexes:).md)
  Returns insertion points in bulk for a specified line fragment.
- [func glyphIndex(for: NSPoint, in: NSTextContainer) -> Int](nslayoutmanager/glyphindex(for:in:).md)
  Returns the index of the glyph at the specified location in a text container.
- [func glyphRange(forBoundingRect: NSRect, in: NSTextContainer) -> NSRange](nslayoutmanager/glyphrange(forboundingrect:in:).md)
  Returns the smallest contiguous range for glyphs lying wholly or partially within the specified rectangle of the text container.
- [func glyphRange(forBoundingRectWithoutAdditionalLayout: NSRect, in: NSTextContainer) -> NSRange](nslayoutmanager/glyphrange(forboundingrectwithoutadditionallayout:in:).md)
  Returns the smallest contiguous range for glyphs lying wholly or partially within the specified rectangle of the text container.
- [func glyphRange(for: NSTextContainer) -> NSRange](nslayoutmanager/glyphrange(for:).md)
  Returns the range of glyphs lying within the specified text container.
- [func glyphRange(forCharacterRange: NSRange, actualCharacterRange: NSRangePointer?) -> NSRange](nslayoutmanager/glyphrange(forcharacterrange:actualcharacterrange:).md)
  Returns the range of glyphs that the specified range of characters generates.
- [func range(ofNominallySpacedGlyphsContaining: Int) -> NSRange](nslayoutmanager/range(ofnominallyspacedglyphscontaining:).md)
  Returns the range of displayable glyphs that surround the glyph at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/glyphindex(for:in:fractionofdistancethroughglyph:))*