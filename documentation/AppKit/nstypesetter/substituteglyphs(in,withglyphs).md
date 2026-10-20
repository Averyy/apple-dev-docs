# substituteGlyphs(in:withGlyphs:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Replaces the specified glyphs with specified replacement glyphs.

**Availability**:
- macOS 10.3+ - Deprecated in 10.13

## Declaration

```swift
func substituteGlyphs(in glyphRange: NSRange, withGlyphs glyphs: UnsafeMutablePointer<NSGlyph>!)
```

```objc
- (void) substituteGlyphsInRange:(NSRange) glyphRange withGlyphs:(NSGlyph *) glyphs;
```

#### Discussion

This method does not alter the glyph-to-character mapping or invalidate layout information.

A subclass can override this method to interact with custom glyph storage.

## Parameters

- `glyphRange`: The range of glyphs to be substituted.
- `glyphs`: The glyphs to substitute for the glyphs in `glyphRange`.

## See Also

### Deprecated
- [func actionForControlCharacter(at: Int) -> NSTypesetterControlCharacterAction](./actionforcontrolcharacter%28at%29.md)
  Returns the action associated with a control character.
- [func deleteGlyphs(in: NSRange)](./deleteglyphs%28in%29.md)
  Deletes the specified glyphs from the glyph cache maintained by the layout manager.
- [func getGlyphs(in: NSRange, glyphs: UnsafeMutablePointer<NSGlyph>!, characterIndexes: UnsafeMutablePointer<Int>!, glyphInscriptions: UnsafeMutablePointer<NSGlyphInscription>!, elasticBits: UnsafeMutablePointer<ObjCBool>!, bidiLevels: UnsafeMutablePointer<UInt8>!) -> Int](./getglyphs%28in,glyphs,characterindexes,glyphinscriptions,elasticbits,bidilevels%29.md)
  Extracts the information needed to lay out the provided glyphs from the provided range.
- [func insertGlyph(NSGlyph, atGlyphIndex: Int, characterIndex: Int)](./insertglyph%28_,atglyphindex,characterindex%29.md)
  Enables the typesetter to insert a new glyph into the stream.
- [struct NSTypesetterControlCharacterAction](../nstypesettercontrolcharacteraction.md)
  The following constants are possible values returned by the [`actionForControlCharacter(at:)`](./actionforcontrolcharacter%28at%29.md) method to determine the action associated with a control character.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/substituteglyphs(in:withglyphs:))*