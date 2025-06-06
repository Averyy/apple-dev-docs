# substituteGlyphs(in:withGlyphs:)

**Framework**: AppKit  
**Kind**: method

Replaces the specified glyphs with specified replacement glyphs.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func substituteGlyphs(in glyphRange: NSRange, withGlyphs glyphs: UnsafeMutablePointer<NSGlyph>!)
```

#### Discussion

This method does not alter the glyph-to-character mapping or invalidate layout information.

A subclass can override this method to interact with custom glyph storage.

## Parameters

- `glyphRange`: The range of glyphs to be substituted.
- `glyphs`: The glyphs to substitute for the glyphs in  .

## See Also

- [func actionForControlCharacter(at: Int) -> NSTypesetterControlCharacterAction](nstypesetter/actionforcontrolcharacter(at:).md)
  Returns the action associated with a control character.
- [func deleteGlyphs(in: NSRange)](nstypesetter/deleteglyphs(in:).md)
  Deletes the specified glyphs from the glyph cache maintained by the layout manager.
- [func getGlyphs(in: NSRange, glyphs: UnsafeMutablePointer<NSGlyph>!, characterIndexes: UnsafeMutablePointer<Int>!, glyphInscriptions: UnsafeMutablePointer<NSGlyphInscription>!, elasticBits: UnsafeMutablePointer<ObjCBool>!, bidiLevels: UnsafeMutablePointer<UInt8>!) -> Int](nstypesetter/getglyphs(in:glyphs:characterindexes:glyphinscriptions:elasticbits:bidilevels:).md)
  Extracts the information needed to lay out the provided glyphs from the provided range.
- [func insertGlyph(NSGlyph, atGlyphIndex: Int, characterIndex: Int)](nstypesetter/insertglyph(_:atglyphindex:characterindex:).md)
  Enables the typesetter to insert a new glyph into the stream.
- [struct NSTypesetterControlCharacterAction](nstypesettercontrolcharacteraction.md)
  The following constants are possible values returned by the [`actionForControlCharacter(at:)`](nstypesetter/actionforcontrolcharacter(at:).md) method to determine the action associated with a control character.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/substituteglyphs(in:withglyphs:))*