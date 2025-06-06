# deleteGlyphs(in:)

**Framework**: AppKit  
**Kind**: method

Deletes the specified glyphs from the glyph cache maintained by the layout manager.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func deleteGlyphs(in glyphRange: NSRange)
```

#### Discussion

A subclass can override this method to interact with custom glyph storage.

## Parameters

- `glyphRange`: The range of glyphs to be deleted.

## See Also

- [func actionForControlCharacter(at: Int) -> NSTypesetterControlCharacterAction](nstypesetter/actionforcontrolcharacter(at:).md)
  Returns the action associated with a control character.
- [func substituteGlyphs(in: NSRange, withGlyphs: UnsafeMutablePointer<NSGlyph>!)](nstypesetter/substituteglyphs(in:withglyphs:).md)
  Replaces the specified glyphs with specified replacement glyphs.
- [func getGlyphs(in: NSRange, glyphs: UnsafeMutablePointer<NSGlyph>!, characterIndexes: UnsafeMutablePointer<Int>!, glyphInscriptions: UnsafeMutablePointer<NSGlyphInscription>!, elasticBits: UnsafeMutablePointer<ObjCBool>!, bidiLevels: UnsafeMutablePointer<UInt8>!) -> Int](nstypesetter/getglyphs(in:glyphs:characterindexes:glyphinscriptions:elasticbits:bidilevels:).md)
  Extracts the information needed to lay out the provided glyphs from the provided range.
- [func insertGlyph(NSGlyph, atGlyphIndex: Int, characterIndex: Int)](nstypesetter/insertglyph(_:atglyphindex:characterindex:).md)
  Enables the typesetter to insert a new glyph into the stream.
- [struct NSTypesetterControlCharacterAction](nstypesettercontrolcharacteraction.md)
  The following constants are possible values returned by the [`actionForControlCharacter(at:)`](nstypesetter/actionforcontrolcharacter(at:).md) method to determine the action associated with a control character.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/deleteglyphs(in:))*