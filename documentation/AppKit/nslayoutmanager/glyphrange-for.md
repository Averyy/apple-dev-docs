# glyphRange(for:)

**Framework**: AppKit  
**Kind**: method

Returns the range of glyphs lying within the specified text container.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func glyphRange(for container: NSTextContainer) -> NSRange
```

#### Discussion

This is a less efficient method than the similar [`textContainer(forGlyphAt:effectiveRange:)`](nslayoutmanager/textcontainer(forglyphat:effectiverange:).md).

Performs glyph generation and layout if needed.

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
- [func glyphIndex(for: NSPoint, in: NSTextContainer, fractionOfDistanceThroughGlyph: UnsafeMutablePointer<CGFloat>?) -> Int](nslayoutmanager/glyphindex(for:in:fractionofdistancethroughglyph:).md)
  Returns the index of the glyph at the specified point using the container’s coordinate system.
- [func glyphRange(forBoundingRect: NSRect, in: NSTextContainer) -> NSRange](nslayoutmanager/glyphrange(forboundingrect:in:).md)
  Returns the smallest contiguous range for glyphs lying wholly or partially within the specified rectangle of the text container.
- [func glyphRange(forBoundingRectWithoutAdditionalLayout: NSRect, in: NSTextContainer) -> NSRange](nslayoutmanager/glyphrange(forboundingrectwithoutadditionallayout:in:).md)
  Returns the smallest contiguous range for glyphs lying wholly or partially within the specified rectangle of the text container.
- [func glyphRange(forCharacterRange: NSRange, actualCharacterRange: NSRangePointer?) -> NSRange](nslayoutmanager/glyphrange(forcharacterrange:actualcharacterrange:).md)
  Returns the range of glyphs that the specified range of characters generates.
- [func range(ofNominallySpacedGlyphsContaining: Int) -> NSRange](nslayoutmanager/range(ofnominallyspacedglyphscontaining:).md)
  Returns the range of displayable glyphs that surround the glyph at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/glyphrange(for:))*