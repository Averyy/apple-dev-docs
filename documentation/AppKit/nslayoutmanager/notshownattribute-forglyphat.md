# notShownAttribute(forGlyphAt:)

**Framework**: AppKit  
**Kind**: method

Indicates whether the glyph at the specified index has a visible representation.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func notShownAttribute(forGlyphAt glyphIndex: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the glyph at `glyphIndex` is not shown; otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Some glyphs are not shown.  For example, a tab, newline, or attachment glyph is not shown; it just affects the layout of following glyphs or locates the attachment graphic. Space characters, however, typically are shown as glyphs with a displacement, although they leave no visible marks.

This method causes glyph generation and layout for the line fragment containing the specified glyph, or if noncontiguous layout is not enabled, up to and including that line fragment.

Raises an `NSRangeException` if `glyphIndex` is out of bounds.

## Parameters

- `glyphIndex`: Index of the glyph.

## See Also

- [func attachmentSize(forGlyphAt: Int) -> NSSize](nslayoutmanager/attachmentsize(forglyphat:).md)
  Returns the size of the attachment glyph at the specified index.
- [func drawsOutsideLineFragment(forGlyphAt: Int) -> Bool](nslayoutmanager/drawsoutsidelinefragment(forglyphat:).md)
  Indicates whether the glyph draws outside its line fragment rectangle.
- [var extraLineFragmentRect: NSRect](nslayoutmanager/extralinefragmentrect.md)
  The rectangle for the extra line fragment at the end of a document.
- [var extraLineFragmentTextContainer: NSTextContainer?](nslayoutmanager/extralinefragmenttextcontainer.md)
  The text container for the extra line fragment rectangle.
- [var extraLineFragmentUsedRect: NSRect](nslayoutmanager/extralinefragmentusedrect.md)
  The rectangle that encloses the insertion point in the extra line fragment rectangle.
- [func firstUnlaidCharacterIndex() -> Int](nslayoutmanager/firstunlaidcharacterindex.md)
  Returns the index for the first character in the layout manager that isn’t in the layout.
- [func firstUnlaidGlyphIndex() -> Int](nslayoutmanager/firstunlaidglyphindex.md)
  Returns the index for the first glyph in the layout manager that isn’t in the layout.
- [func getFirstUnlaidCharacterIndex(UnsafeMutablePointer<Int>?, glyphIndex: UnsafeMutablePointer<Int>?)](nslayoutmanager/getfirstunlaidcharacterindex(_:glyphindex:).md)
  Returns the indexes for the first character and glyph that have invalid layout information.
- [func lineFragmentRect(forGlyphAt: Int, effectiveRange: NSRangePointer?) -> NSRect](nslayoutmanager/linefragmentrect(forglyphat:effectiverange:).md)
  Returns the rectangle for the line fragment where the glyph lies and (optionally), by reference, the entire range of glyphs in that fragment.
- [func lineFragmentRect(forGlyphAt: Int, effectiveRange: NSRangePointer?, withoutAdditionalLayout: Bool) -> NSRect](nslayoutmanager/linefragmentrect(forglyphat:effectiverange:withoutadditionallayout:).md)
  Returns the line fragment rectangle that contains the glyph at the specified glyph index.
- [func lineFragmentUsedRect(forGlyphAt: Int, effectiveRange: NSRangePointer?) -> NSRect](nslayoutmanager/linefragmentusedrect(forglyphat:effectiverange:).md)
  Returns the usage rectangle for the line fragment and (optionally) returns the entire range of glyphs in that fragment.
- [func lineFragmentUsedRect(forGlyphAt: Int, effectiveRange: NSRangePointer?, withoutAdditionalLayout: Bool) -> NSRect](nslayoutmanager/linefragmentusedrect(forglyphat:effectiverange:withoutadditionallayout:).md)
  Returns the usage rectangle for the line fragment and (optionally) returns the entire range of glyphs in that fragment.
- [func location(forGlyphAt: Int) -> NSPoint](nslayoutmanager/location(forglyphat:).md)
  Returns the location for the specified glyph within its line fragment.
- [func truncatedGlyphRange(inLineFragmentForGlyphAt: Int) -> NSRange](nslayoutmanager/truncatedglyphrange(inlinefragmentforglyphat:).md)
  Returns the range of truncated glyphs for a line fragment that contains the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/notshownattribute(forglyphat:))*