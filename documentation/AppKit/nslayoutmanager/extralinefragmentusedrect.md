# extraLineFragmentUsedRect

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The rectangle that encloses the insertion point in the extra line fragment rectangle.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var extraLineFragmentUsedRect: NSRect { get }
```

```objc
@property (readonly) NSRect extraLineFragmentUsedRect;
```

#### Discussion

The rectangle is defined in the coordinate system of its `NSTextContainer`. `NSZeroRect` if there is no extra line fragment rectangle.

The extra line fragment used rectangle is twice as wide (or tall) as the text container’s line fragment padding, with the insertion point itself in the middle.

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/extralinefragmentusedrect)*