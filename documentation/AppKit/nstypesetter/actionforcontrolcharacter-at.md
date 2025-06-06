# actionForControlCharacter(at:)

**Framework**: AppKit  
**Kind**: method

Returns the action associated with a control character.

**Availability**:
- macOS ?+

## Declaration

```swift
func actionForControlCharacter(at charIndex: Int) -> NSTypesetterControlCharacterAction
```

#### Return Value

The action associated with the control character at `charIndex`.

## Parameters

- `charIndex`: The index of the control character.

## See Also

- [func deleteGlyphs(in: NSRange)](nstypesetter/deleteglyphs(in:).md)
  Deletes the specified glyphs from the glyph cache maintained by the layout manager.
- [func substituteGlyphs(in: NSRange, withGlyphs: UnsafeMutablePointer<NSGlyph>!)](nstypesetter/substituteglyphs(in:withglyphs:).md)
  Replaces the specified glyphs with specified replacement glyphs.
- [func getGlyphs(in: NSRange, glyphs: UnsafeMutablePointer<NSGlyph>!, characterIndexes: UnsafeMutablePointer<Int>!, glyphInscriptions: UnsafeMutablePointer<NSGlyphInscription>!, elasticBits: UnsafeMutablePointer<ObjCBool>!, bidiLevels: UnsafeMutablePointer<UInt8>!) -> Int](nstypesetter/getglyphs(in:glyphs:characterindexes:glyphinscriptions:elasticbits:bidilevels:).md)
  Extracts the information needed to lay out the provided glyphs from the provided range.
- [func insertGlyph(NSGlyph, atGlyphIndex: Int, characterIndex: Int)](nstypesetter/insertglyph(_:atglyphindex:characterindex:).md)
  Enables the typesetter to insert a new glyph into the stream.
- [struct NSTypesetterControlCharacterAction](nstypesettercontrolcharacteraction.md)
  The following constants are possible values returned by the [`actionForControlCharacter(at:)`](nstypesetter/actionforcontrolcharacter(at:).md) method to determine the action associated with a control character.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/actionforcontrolcharacter(at:))*