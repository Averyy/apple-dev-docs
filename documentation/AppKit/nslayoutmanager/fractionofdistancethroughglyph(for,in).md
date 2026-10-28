# fractionOfDistanceThroughGlyph(for:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the fraction of the distance between the glyph at the specified point and the next glyph.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func fractionOfDistanceThroughGlyph(for point: NSPoint, in container: NSTextContainer) -> CGFloat
```

```objc
- (CGFloat) fractionOfDistanceThroughGlyphForPoint:(NSPoint) point inTextContainer:(NSTextContainer *) container;
```

## Discussion

This method is a primitive for [`glyphIndex(for:in:fractionOfDistanceThroughGlyph:)`](./glyphindex%28for,in,fractionofdistancethroughglyph%29.md). You should always call the main method, not the primitives.

Overriding should be done for the primitive methods. Existing subclasses that do not do this overriding will not have their implementations available to Java developers.

## See Also

### Performing advanced layout queries
- [func boundingRect(forGlyphRange: NSRange, in: NSTextContainer) -> NSRect](./boundingrect%28forglyphrange,in%29.md)
  Returns the bounding rectangle for the specified glyphs in a container.
- [func characterIndex(for: NSPoint, in: NSTextContainer, fractionOfDistanceBetweenInsertionPoints: UnsafeMutablePointer<CGFloat>?) -> Int](./characterindex%28for,in,fractionofdistancebetweeninsertionpoints%29.md)
  Returns the index of the character that lies beneath the specified point using the specified container’s coordinate system.
- [func characterRange(forGlyphRange: NSRange, actualGlyphRange: NSRangePointer?) -> NSRange](./characterrange%28forglyphrange,actualglyphrange%29.md)
  Returns the range of characters that correspond to the glyphs in the specified glyph range.
- [func enumerateEnclosingRects(forGlyphRange: NSRange, withinSelectedGlyphRange: NSRange, in: NSTextContainer, using: (NSRect, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerateenclosingrects%28forglyphrange,withinselectedglyphrange,in,using%29.md)
  Enumerates enclosing rectangles for the specified glyph range in a text container.
- [func enumerateLineFragments(forGlyphRange: NSRange, using: (NSRect, NSRect, NSTextContainer, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratelinefragments%28forglyphrange,using%29.md)
  Enumerates line fragments intersecting with the specified glyph range.
- [func getLineFragmentInsertionPoints(forCharacterAt: Int, alternatePositions: Bool, inDisplayOrder: Bool, positions: UnsafeMutablePointer<CGFloat>?, characterIndexes: UnsafeMutablePointer<Int>?) -> Int](./getlinefragmentinsertionpoints%28forcharacterat,alternatepositions,indisplayorder,positions,characterindexes%29.md)
  Returns insertion points in bulk for a specified line fragment.
- [func glyphIndex(for: NSPoint, in: NSTextContainer) -> Int](./glyphindex%28for,in%29.md)
  Returns the index of the glyph at the specified location in a text container.
- [func glyphIndex(for: NSPoint, in: NSTextContainer, fractionOfDistanceThroughGlyph: UnsafeMutablePointer<CGFloat>?) -> Int](./glyphindex%28for,in,fractionofdistancethroughglyph%29.md)
  Returns the index of the glyph at the specified point using the container’s coordinate system.
- [func glyphRange(forBoundingRect: NSRect, in: NSTextContainer) -> NSRange](./glyphrange%28forboundingrect,in%29.md)
  Returns the smallest contiguous range for glyphs lying wholly or partially within the specified rectangle of the text container.
- [func glyphRange(forBoundingRectWithoutAdditionalLayout: NSRect, in: NSTextContainer) -> NSRange](./glyphrange%28forboundingrectwithoutadditionallayout,in%29.md)
  Returns the smallest contiguous range for glyphs lying wholly or partially within the specified rectangle of the text container.
- [func glyphRange(for: NSTextContainer) -> NSRange](./glyphrange%28for%29.md)
  Returns the range of glyphs lying within the specified text container.
- [func glyphRange(forCharacterRange: NSRange, actualCharacterRange: NSRangePointer?) -> NSRange](./glyphrange%28forcharacterrange,actualcharacterrange%29.md)
  Returns the range of glyphs that the specified range of characters generates.
- [func range(ofNominallySpacedGlyphsContaining: Int) -> NSRange](./range%28ofnominallyspacedglyphscontaining%29.md)
  Returns the range of displayable glyphs that surround the glyph at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/fractionofdistancethroughglyph(for:in:))*