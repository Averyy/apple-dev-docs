# actionForControlCharacter(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the action associated with a control character.

**Availability**:
- macOS

## Declaration

```swift
func actionForControlCharacter(at charIndex: Int) -> NSTypesetterControlCharacterAction
```

```objc
- (NSTypesetterControlCharacterAction) actionForControlCharacterAtIndex:(NSUInteger) charIndex;
```

#### Return Value

The action associated with the control character at `charIndex`.

## Parameters

- `charIndex`: The index of the control character.

## See Also

### Deprecated
- [func deleteGlyphs(in: NSRange)](./deleteglyphs%28in%29.md)
  Deletes the specified glyphs from the glyph cache maintained by the layout manager.
- [func substituteGlyphs(in: NSRange, withGlyphs: UnsafeMutablePointer<NSGlyph>!)](./substituteglyphs%28in,withglyphs%29.md)
  Replaces the specified glyphs with specified replacement glyphs.
- [func getGlyphs(in: NSRange, glyphs: UnsafeMutablePointer<NSGlyph>!, characterIndexes: UnsafeMutablePointer<Int>!, glyphInscriptions: UnsafeMutablePointer<NSGlyphInscription>!, elasticBits: UnsafeMutablePointer<ObjCBool>!, bidiLevels: UnsafeMutablePointer<UInt8>!) -> Int](./getglyphs%28in,glyphs,characterindexes,glyphinscriptions,elasticbits,bidilevels%29.md)
  Extracts the information needed to lay out the provided glyphs from the provided range.
- [func insertGlyph(NSGlyph, atGlyphIndex: Int, characterIndex: Int)](./insertglyph%28_,atglyphindex,characterindex%29.md)
  Enables the typesetter to insert a new glyph into the stream.
- [struct NSTypesetterControlCharacterAction](../nstypesettercontrolcharacteraction.md)
  The following constants are possible values returned by the [`actionForControlCharacter(at:)`](./actionforcontrolcharacter%28at%29.md) method to determine the action associated with a control character.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/actionforcontrolcharacter(at:))*