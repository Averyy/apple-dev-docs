# glyphRange(forCharacterRange:actualCharacterRange:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the range for the glyphs mapped to the characters of the text store in the specified range.

**Availability**:
- macOS

## Declaration

```swift
func glyphRange(forCharacterRange charRange: NSRange, actualCharacterRange actualCharRange: NSRangePointer?) -> NSRange
```

```objc
- (NSRange) glyphRangeForCharacterRange:(NSRange) charRange actualCharacterRange:(NSRangePointer) actualCharRange;
```

## Return Value

The range for the glyphs mapped to the characters of the text store in `charRange`.

## Discussion

A subclass can override this method to interact with custom glyph storage.

## Parameters

- `charRange`: The range of the characters whose glyph range is desired.
- `actualCharRange`: On return, all characters mapped to those glyphs; may be `NULL`.

## See Also

### Interfacing with Glyph Storage
- [func characterRange(forGlyphRange: NSRange, actualGlyphRange: NSRangePointer?) -> NSRange](./characterrange%28forglyphrange,actualglyphrange%29.md)
  Returns the range for the characters in the receiver’s text store that are mapped to the specified glyphs.
- [func setAttachmentSize(NSSize, forGlyphRange: NSRange)](./setattachmentsize%28_,forglyphrange%29.md)
  Sets the size the specified glyphs (assumed to be attachments) will be asked to draw themselves at.
- [func setBidiLevels(UnsafePointer<UInt8>!, forGlyphRange: NSRange)](./setbidilevels%28_,forglyphrange%29.md)
  Sets the direction of the specified glyphs for bidirectional text.
- [func setDrawsOutsideLineFragment(Bool, forGlyphRange: NSRange)](./setdrawsoutsidelinefragment%28_,forglyphrange%29.md)
  Sets whether the specified glyphs exceed the bounds of the line fragment in which they are laid out.
- [func setLineFragmentRect(NSRect, forGlyphRange: NSRange, usedRect: NSRect, baselineOffset: CGFloat)](./setlinefragmentrect%28_,forglyphrange,usedrect,baselineoffset%29.md)
  Sets the line fragment rectangle where the specified glyphs are laid out.
- [func setLocation(NSPoint, withAdvancements: UnsafePointer<CGFloat>!, forStartOfGlyphRange: NSRange)](./setlocation%28_,withadvancements,forstartofglyphrange%29.md)
  Sets the location where the specified glyphs are laid out.
- [func setNotShownAttribute(Bool, forGlyphRange: NSRange)](./setnotshownattribute%28_,forglyphrange%29.md)
  Sets whether the specified glyphs are not shown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/glyphrange(forcharacterrange:actualcharacterrange:))*