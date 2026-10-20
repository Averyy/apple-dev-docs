# enumerateEnclosingRects(forGlyphRange:withinSelectedGlyphRange:in:using:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Enumerates enclosing rectangles for the specified glyph range in a text container.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func enumerateEnclosingRects(forGlyphRange glyphRange: NSRange, withinSelectedGlyphRange selectedRange: NSRange, in textContainer: NSTextContainer, using block: @escaping (CGRect, UnsafeMutablePointer<ObjCBool>) -> Void)
```

```objc
- (void) enumerateEnclosingRectsForGlyphRange:(NSRange) glyphRange withinSelectedGlyphRange:(NSRange) selectedRange inTextContainer:(NSTextContainer *) textContainer usingBlock:(void (^)(CGRect rect, BOOL *stop)) block;
```

#### Discussion

These rectangles are always in container coordinates. They can be used to draw the text background or highlight for the given range of characters. The rectangles don’t necessarily enclose glyphs that draw outside their line fragment rectangles; use [`boundingRect(forGlyphRange:in:)`](./boundingrect%28forglyphrange,in%29.md) to determine the area that contains all drawing performed for a range of glyphs.

If a selected range is given in the second argument, the rectangles returned are correct for drawing the selection.  Selection rectangles are generally more complicated than enclosing rectangles, and supplying a selected range determines whether the method does this extra work. This method does the minimum amount of work required to answer the question.

Performs glyph generation and layout if needed.

## Parameters

- `glyphRange`: The glyph range for which to return enclosing rectangles.
- `selectedRange`: Selected glyphs within `glyphRange`, which can affect the size of the rectangles. If not interested in selection rectangles, pass `{NSNotFound, 0}` as the selected range.
- `textContainer`: The text container in which the glyphs are laid out.
- `block`: The block to apply to the glyph range. The block has two arguments:

  - **rect**: The current enclosing rectangle.
  - **stop**: A reference to a Boolean value. The block can set the value to [`true`](../../Swift/true.md) to stop further processing of the array. The stop argument is an out-only argument. You should only set this Boolean to [`true`](../../Swift/true.md) within the block.

## See Also

### Performing advanced layout queries
- [func boundingRect(forGlyphRange: NSRange, in: NSTextContainer) -> CGRect](./boundingrect%28forglyphrange,in%29.md)
  Returns the bounding rectangle for the specified glyphs in a container.
- [func characterIndex(for: CGPoint, in: NSTextContainer, fractionOfDistanceBetweenInsertionPoints: UnsafeMutablePointer<CGFloat>?) -> Int](./characterindex%28for,in,fractionofdistancebetweeninsertionpoints%29.md)
  Returns the index of the character that lies beneath the specified point using the specified container’s coordinate system.
- [func characterRange(forGlyphRange: NSRange, actualGlyphRange: NSRangePointer?) -> NSRange](./characterrange%28forglyphrange,actualglyphrange%29.md)
  Returns the range of characters that correspond to the glyphs in the specified glyph range.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanager/enumerateenclosingrects(forglyphrange:withinselectedglyphrange:in:using:))*