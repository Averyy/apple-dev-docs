# getFirstUnlaidCharacterIndex(_:glyphIndex:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the indexes for the first character and glyph that have invalid layout information.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func getFirstUnlaidCharacterIndex(_ charIndex: UnsafeMutablePointer<Int>?, glyphIndex: UnsafeMutablePointer<Int>?)
```

```objc
- (void) getFirstUnlaidCharacterIndex:(NSUInteger *) charIndex glyphIndex:(NSUInteger *) glyphIndex;
```

## Discussion

Either parameter may be `NULL`, in which case the receiver simply ignores it.

As part of its implementation, this method calls [`firstUnlaidCharacterIndex()`](./firstunlaidcharacterindex%28%29.md) and [`firstUnlaidGlyphIndex()`](./firstunlaidglyphindex%28%29.md). To change this method’s behavior, override those two methods instead of this one.

## Parameters

- `charIndex`: On return, if not `NULL`, the index of the first character that has invalid layout information
- `glyphIndex`: On return, if not `NULL`, the index of the first glyph that has invalid layout information.

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/getfirstunlaidcharacterindex(_:glyphindex:))*