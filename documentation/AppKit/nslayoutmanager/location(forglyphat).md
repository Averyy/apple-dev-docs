# location(forGlyphAt:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the location for the specified glyph within its line fragment.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func location(forGlyphAt glyphIndex: Int) -> NSPoint
```

```objc
- (NSPoint) locationForGlyphAtIndex:(NSUInteger) glyphIndex;
```

## Return Value

The location of the given glyph.

## Discussion

If the given glyph does not have an explicit location set for it (for example, if it is part of (but not first in) a sequence of nominally spaced characters), the location is calculated by glyph advancements from the location of the most recent preceding glyph with a location set.

Glyph locations are relative to their line fragment rectangle’s origin. The line fragment rectangle in turn is defined in the coordinate system of the text container where it resides.

This method causes glyph generation and layout for the line fragment containing the specified glyph, or if noncontiguous layout is not enabled, up to and including that line fragment.

## Parameters

- `glyphIndex`: The glyph whose location is returned.

## See Also

### Getting layout information
- [func attachmentSize(forGlyphAt: Int) -> NSSize](./attachmentsize%28forglyphat%29.md)
  Returns the size of the attachment glyph at the specified index.
- [func drawsOutsideLineFragment(forGlyphAt: Int) -> Bool](./drawsoutsidelinefragment%28forglyphat%29.md)
  Indicates whether the glyph draws outside its line fragment rectangle.
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
- [func notShownAttribute(forGlyphAt: Int) -> Bool](./notshownattribute%28forglyphat%29.md)
  Indicates whether the glyph at the specified index has a visible representation.
- [func truncatedGlyphRange(inLineFragmentForGlyphAt: Int) -> NSRange](./truncatedglyphrange%28inlinefragmentforglyphat%29.md)
  Returns the range of truncated glyphs for a line fragment that contains the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/location(forglyphat:))*