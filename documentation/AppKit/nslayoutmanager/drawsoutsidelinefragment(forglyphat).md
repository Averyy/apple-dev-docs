# drawsOutsideLineFragment(forGlyphAt:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Indicates whether the glyph draws outside its line fragment rectangle.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func drawsOutsideLineFragment(forGlyphAt glyphIndex: Int) -> Bool
```

```objc
- (BOOL) drawsOutsideLineFragmentForGlyphAtIndex:(NSUInteger) glyphIndex;
```

#### Return Value

[`true`](../../Swift/true.md) if the glyph at `glyphIndex` exceeds the bounds of the line fragment where it’s laid out, [`false`](../../Swift/false.md) otherwise.

#### Discussion

Exceeding bounds can happen when text is set at a fixed line height. For example, if the user specifies a fixed line height of 12 points and sets the font size to 24 points, the glyphs will exceed their layout rectangles.

This method causes glyph generation and layout for the line fragment containing the specified glyph, or if noncontiguous layout is not enabled, up to and including that line fragment.

Glyphs that draw outside their line fragment rectangles aren’t considered when calculating enclosing rectangles with the [`rectArray(forCharacterRange:withinSelectedCharacterRange:in:rectCount:)`](./rectarray%28forcharacterrange,withinselectedcharacterrange,in,rectcount%29.md) and [`rectArray(forGlyphRange:withinSelectedGlyphRange:in:rectCount:)`](./rectarray%28forglyphrange,withinselectedglyphrange,in,rectcount%29.md) methods. They are, however, considered by [`boundingRect(forGlyphRange:in:)`](./boundingrect%28forglyphrange,in%29.md).

## Parameters

- `glyphIndex`: Index of the glyph.

## See Also

### Getting layout information
- [func attachmentSize(forGlyphAt: Int) -> NSSize](./attachmentsize%28forglyphat%29.md)
  Returns the size of the attachment glyph at the specified index.
- [var extraLineFragmentRect: NSRect](./extralinefragmentrect.md)
  The rectangle for the extra line fragment at the end of a document.
- [var extraLineFragmentTextContainer: NSTextContainer?](./extralinefragmenttextcontainer.md)
  The text container for the extra line fragment rectangle.
- [var extraLineFragmentUsedRect: NSRect](./extralinefragmentusedrect.md)
  The rectangle that encloses the insertion point in the extra line fragment rectangle.
- [func firstUnlaidCharacterIndex() -> Int](./firstunlaidcharacterindex%28%29.md)
  Returns the index for the first character in the layout manager that isn’t in the layout.
- [func firstUnlaidGlyphIndex() -> Int](./firstunlaidglyphindex%28%29.md)
  Returns the index for the first glyph in the layout manager that isn’t in the layout.
- [func getFirstUnlaidCharacterIndex(UnsafeMutablePointer<Int>?, glyphIndex: UnsafeMutablePointer<Int>?)](./getfirstunlaidcharacterindex%28_,glyphindex%29.md)
  Returns the indexes for the first character and glyph that have invalid layout information.
- [func lineFragmentRect(forGlyphAt: Int, effectiveRange: NSRangePointer?) -> NSRect](./linefragmentrect%28forglyphat,effectiverange%29.md)
  Returns the rectangle for the line fragment where the glyph lies and (optionally), by reference, the entire range of glyphs in that fragment.
- [func lineFragmentRect(forGlyphAt: Int, effectiveRange: NSRangePointer?, withoutAdditionalLayout: Bool) -> NSRect](./linefragmentrect%28forglyphat,effectiverange,withoutadditionallayout%29.md)
  Returns the line fragment rectangle that contains the glyph at the specified glyph index.
- [func lineFragmentUsedRect(forGlyphAt: Int, effectiveRange: NSRangePointer?) -> NSRect](./linefragmentusedrect%28forglyphat,effectiverange%29.md)
  Returns the usage rectangle for the line fragment and (optionally) returns the entire range of glyphs in that fragment.
- [func lineFragmentUsedRect(forGlyphAt: Int, effectiveRange: NSRangePointer?, withoutAdditionalLayout: Bool) -> NSRect](./linefragmentusedrect%28forglyphat,effectiverange,withoutadditionallayout%29.md)
  Returns the usage rectangle for the line fragment and (optionally) returns the entire range of glyphs in that fragment.
- [func location(forGlyphAt: Int) -> NSPoint](./location%28forglyphat%29.md)
  Returns the location for the specified glyph within its line fragment.
- [func notShownAttribute(forGlyphAt: Int) -> Bool](./notshownattribute%28forglyphat%29.md)
  Indicates whether the glyph at the specified index has a visible representation.
- [func truncatedGlyphRange(inLineFragmentForGlyphAt: Int) -> NSRange](./truncatedglyphrange%28inlinefragmentforglyphat%29.md)
  Returns the range of truncated glyphs for a line fragment that contains the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/drawsoutsidelinefragment(forglyphat:))*