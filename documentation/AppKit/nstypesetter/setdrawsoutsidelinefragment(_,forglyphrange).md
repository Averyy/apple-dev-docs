# setDrawsOutsideLineFragment(_:forGlyphRange:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets whether the specified glyphs exceed the bounds of the line fragment in which they are laid out.

**Availability**:
- macOS

## Declaration

```swift
func setDrawsOutsideLineFragment(_ flag: Bool, forGlyphRange glyphRange: NSRange)
```

```objc
- (void) setDrawsOutsideLineFragment:(BOOL) flag forGlyphRange:(NSRange) glyphRange;
```

## Discussion

This can happen when text is set at a fixed line height. For example, if the user specifies a fixed line height of 12 points and sets the font size to 24 points, the glyphs will exceed their layout rectangles.

A subclass can override this method to interact with custom glyph storage.

## Parameters

- `flag`: [`true`](../../Swift/true.md) if the glyphs in `glyphRange` exceed the bounds of the line fragment in which they are laid out, [`false`](../../Swift/false.md) otherwise.
- `glyphRange`: The range of the glyphs in question.

## See Also

### Interfacing with Glyph Storage
- [func characterRange(forGlyphRange: NSRange, actualGlyphRange: NSRangePointer?) -> NSRange](./characterrange%28forglyphrange,actualglyphrange%29.md)
  Returns the range for the characters in the receiver’s text store that are mapped to the specified glyphs.
- [func glyphRange(forCharacterRange: NSRange, actualCharacterRange: NSRangePointer?) -> NSRange](./glyphrange%28forcharacterrange,actualcharacterrange%29.md)
  Returns the range for the glyphs mapped to the characters of the text store in the specified range.
- [func setAttachmentSize(NSSize, forGlyphRange: NSRange)](./setattachmentsize%28_,forglyphrange%29.md)
  Sets the size the specified glyphs (assumed to be attachments) will be asked to draw themselves at.
- [func setBidiLevels(UnsafePointer<UInt8>!, forGlyphRange: NSRange)](./setbidilevels%28_,forglyphrange%29.md)
  Sets the direction of the specified glyphs for bidirectional text.
- [func setLineFragmentRect(NSRect, forGlyphRange: NSRange, usedRect: NSRect, baselineOffset: CGFloat)](./setlinefragmentrect%28_,forglyphrange,usedrect,baselineoffset%29.md)
  Sets the line fragment rectangle where the specified glyphs are laid out.
- [func setLocation(NSPoint, withAdvancements: UnsafePointer<CGFloat>!, forStartOfGlyphRange: NSRange)](./setlocation%28_,withadvancements,forstartofglyphrange%29.md)
  Sets the location where the specified glyphs are laid out.
- [func setNotShownAttribute(Bool, forGlyphRange: NSRange)](./setnotshownattribute%28_,forglyphrange%29.md)
  Sets whether the specified glyphs are not shown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/setdrawsoutsidelinefragment(_:forglyphrange:))*