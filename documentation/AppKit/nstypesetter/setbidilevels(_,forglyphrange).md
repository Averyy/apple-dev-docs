# setBidiLevels(_:forGlyphRange:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the direction of the specified glyphs for bidirectional text.

**Availability**:
- macOS

## Declaration

```swift
func setBidiLevels(_ levels: UnsafePointer<UInt8>!, forGlyphRange glyphRange: NSRange)
```

```objc
- (void) setBidiLevels:(const uint8_t *) levels forGlyphRange:(NSRange) glyphRange;
```

#### Discussion

A subclass can override this method to interact with custom glyph storage.

## Parameters

- `levels`: Values in `levels` can range from 0 to 61 as defined by Unicode Standard Annex #9.
- `glyphRange`: The range of glyphs for which the bidirectional text levels are desired.

## See Also

### Interfacing with Glyph Storage
- [func characterRange(forGlyphRange: NSRange, actualGlyphRange: NSRangePointer?) -> NSRange](./characterrange%28forglyphrange,actualglyphrange%29.md)
  Returns the range for the characters in the receiver’s text store that are mapped to the specified glyphs.
- [func glyphRange(forCharacterRange: NSRange, actualCharacterRange: NSRangePointer?) -> NSRange](./glyphrange%28forcharacterrange,actualcharacterrange%29.md)
  Returns the range for the glyphs mapped to the characters of the text store in the specified range.
- [func setAttachmentSize(NSSize, forGlyphRange: NSRange)](./setattachmentsize%28_,forglyphrange%29.md)
  Sets the size the specified glyphs (assumed to be attachments) will be asked to draw themselves at.
- [func setDrawsOutsideLineFragment(Bool, forGlyphRange: NSRange)](./setdrawsoutsidelinefragment%28_,forglyphrange%29.md)
  Sets whether the specified glyphs exceed the bounds of the line fragment in which they are laid out.
- [func setLineFragmentRect(NSRect, forGlyphRange: NSRange, usedRect: NSRect, baselineOffset: CGFloat)](./setlinefragmentrect%28_,forglyphrange,usedrect,baselineoffset%29.md)
  Sets the line fragment rectangle where the specified glyphs are laid out.
- [func setLocation(NSPoint, withAdvancements: UnsafePointer<CGFloat>!, forStartOfGlyphRange: NSRange)](./setlocation%28_,withadvancements,forstartofglyphrange%29.md)
  Sets the location where the specified glyphs are laid out.
- [func setNotShownAttribute(Bool, forGlyphRange: NSRange)](./setnotshownattribute%28_,forglyphrange%29.md)
  Sets whether the specified glyphs are not shown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/setbidilevels(_:forglyphrange:))*