# lineFragmentUsedRect(forGlyphAt:effectiveRange:withoutAdditionalLayout:)

**Framework**: UIKit  
**Kind**: method

Returns the usage rectangle for the line fragment and (optionally) returns the entire range of glyphs in that fragment.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func lineFragmentUsedRect(forGlyphAt glyphIndex: Int, effectiveRange effectiveGlyphRange: NSRangePointer?, withoutAdditionalLayout flag: Bool) -> CGRect
```

#### Return Value

The used rectangle for the line fragment in which the given glyph is laid out.

#### Discussion

This method causes glyph generation and layout for the line fragment containing the specified glyph, or if noncontiguous layout is not enabled, up to and including that line fragment.

Line fragment used rectangles are always in container coordinates.

Overriding this method is not recommended. If the line fragment used rectangle needs to be modified, that should be done at the typesetter level or by calling [`setLineFragmentRect(_:forGlyphRange:usedRect:)`](nslayoutmanager/setlinefragmentrect(_:forglyphrange:usedrect:).md).

## Parameters

- `glyphIndex`: The glyph for which to return the line fragment used rectangle.
- `effectiveGlyphRange`: If not  , on output, the range for all glyphs in the line fragment.
- `flag`: If  , glyph generation and layout are not performed, so this option should not be used unless layout is known to be complete for the range in question, or unless noncontiguous layout is enabled; if  , both are performed as needed.

## See Also

- [func setLineFragmentRect(CGRect, forGlyphRange: NSRange, usedRect: CGRect)](nslayoutmanager/setlinefragmentrect(_:forglyphrange:usedrect:).md)
  Associates the line fragment bounds for the specified range of glyphs.
- [func attachmentSize(forGlyphAt: Int) -> CGSize](nslayoutmanager/attachmentsize(forglyphat:).md)
  Returns the size of the attachment glyph at the specified index.
- [func drawsOutsideLineFragment(forGlyphAt: Int) -> Bool](nslayoutmanager/drawsoutsidelinefragment(forglyphat:).md)
  Indicates whether the glyph draws outside its line fragment rectangle.
- [var extraLineFragmentRect: CGRect](nslayoutmanager/extralinefragmentrect.md)
  The rectangle for the extra line fragment at the end of a document.
- [var extraLineFragmentTextContainer: NSTextContainer?](nslayoutmanager/extralinefragmenttextcontainer.md)
  The text container for the extra line fragment rectangle.
- [var extraLineFragmentUsedRect: CGRect](nslayoutmanager/extralinefragmentusedrect.md)
  The rectangle that encloses the insertion point in the extra line fragment rectangle.
- [func firstUnlaidCharacterIndex() -> Int](nslayoutmanager/firstunlaidcharacterindex.md)
  Returns the index for the first character in the layout manager that isn’t in the layout.
- [func firstUnlaidGlyphIndex() -> Int](nslayoutmanager/firstunlaidglyphindex.md)
  Returns the index for the first glyph in the layout manager that isn’t in the layout.
- [func getFirstUnlaidCharacterIndex(UnsafeMutablePointer<Int>?, glyphIndex: UnsafeMutablePointer<Int>?)](nslayoutmanager/getfirstunlaidcharacterindex(_:glyphindex:).md)
  Returns the indexes for the first character and glyph that have invalid layout information.
- [func lineFragmentRect(forGlyphAt: Int, effectiveRange: NSRangePointer?) -> CGRect](nslayoutmanager/linefragmentrect(forglyphat:effectiverange:).md)
  Returns the rectangle for the line fragment where the glyph lies and (optionally), by reference, the entire range of glyphs in that fragment.
- [func lineFragmentRect(forGlyphAt: Int, effectiveRange: NSRangePointer?, withoutAdditionalLayout: Bool) -> CGRect](nslayoutmanager/linefragmentrect(forglyphat:effectiverange:withoutadditionallayout:).md)
  Returns the line fragment rectangle that contains the glyph at the specified glyph index.
- [func lineFragmentUsedRect(forGlyphAt: Int, effectiveRange: NSRangePointer?) -> CGRect](nslayoutmanager/linefragmentusedrect(forglyphat:effectiverange:).md)
  Returns the usage rectangle for the line fragment and (optionally) returns the entire range of glyphs in that fragment.
- [func location(forGlyphAt: Int) -> CGPoint](nslayoutmanager/location(forglyphat:).md)
  Returns the location for the specified glyph within its line fragment.
- [func notShownAttribute(forGlyphAt: Int) -> Bool](nslayoutmanager/notshownattribute(forglyphat:).md)
  Indicates whether the glyph at the specified index has a visible representation.
- [func truncatedGlyphRange(inLineFragmentForGlyphAt: Int) -> NSRange](nslayoutmanager/truncatedglyphrange(inlinefragmentforglyphat:).md)
  Returns the range of truncated glyphs for a line fragment that contains the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanager/linefragmentusedrect(forglyphat:effectiverange:withoutadditionallayout:))*