# insertGlyph(_:atGlyphIndex:characterIndex:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Enables the typesetter to insert a new glyph into the stream.

**Availability**:
- macOS 10.3+ - Deprecated in 10.13

## Declaration

```swift
func insertGlyph(_ glyph: NSGlyph, atGlyphIndex glyphIndex: Int, characterIndex: Int)
```

```objc
- (void) insertGlyph:(NSGlyph) glyph atGlyphIndex:(NSUInteger) glyphIndex characterIndex:(NSUInteger) characterIndex;
```

## Discussion

The standard typesetter uses this method for inserting hyphenation glyphs. Because this method keeps the glyph caches synchronized, subclasses should always use this method to insert glyphs instead of calling [`layoutManager`](./layoutmanager.md) directly.

A subclass can override this method to interact with custom glyph storage.

## Parameters

- `glyph`: The glyph to insert into the glyph cache.
- `glyphIndex`: The index at which to insert `glyph`.
- `characterIndex`: The index of the character that `glyph` maps to. If the glyph is mapped to several characters, `charIndex` should indicate the first character to which it’s mapped.

## See Also

### Deprecated
- [func actionForControlCharacter(at: Int) -> NSTypesetterControlCharacterAction](./actionforcontrolcharacter%28at%29.md)
  Returns the action associated with a control character.
- [func deleteGlyphs(in: NSRange)](./deleteglyphs%28in%29.md)
  Deletes the specified glyphs from the glyph cache maintained by the layout manager.
- [func substituteGlyphs(in: NSRange, withGlyphs: UnsafeMutablePointer<NSGlyph>!)](./substituteglyphs%28in,withglyphs%29.md)
  Replaces the specified glyphs with specified replacement glyphs.
- [func getGlyphs(in: NSRange, glyphs: UnsafeMutablePointer<NSGlyph>!, characterIndexes: UnsafeMutablePointer<Int>!, glyphInscriptions: UnsafeMutablePointer<NSGlyphInscription>!, elasticBits: UnsafeMutablePointer<ObjCBool>!, bidiLevels: UnsafeMutablePointer<UInt8>!) -> Int](./getglyphs%28in,glyphs,characterindexes,glyphinscriptions,elasticbits,bidilevels%29.md)
  Extracts the information needed to lay out the provided glyphs from the provided range.
- [struct NSTypesetterControlCharacterAction](../nstypesettercontrolcharacteraction.md)
  The following constants are possible values returned by the [`actionForControlCharacter(at:)`](./actionforcontrolcharacter%28at%29.md) method to determine the action associated with a control character.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/insertglyph(_:atglyphindex:characterindex:))*