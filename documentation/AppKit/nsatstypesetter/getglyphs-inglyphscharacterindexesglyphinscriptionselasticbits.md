# getGlyphs(in:glyphs:characterIndexes:glyphInscriptions:elasticBits:)

**Framework**: AppKit  
**Kind**: method

Extracts the information needed to lay out the glyphs in the given glyph buffer from the given glyph range.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func getGlyphs(in glyphsRange: NSRange, glyphs glyphBuffer: UnsafeMutablePointer<NSGlyph>!, characterIndexes charIndexBuffer: UnsafeMutablePointer<Int>!, glyphInscriptions inscribeBuffer: UnsafeMutablePointer<NSGlyphInscription>!, elasticBits elasticBuffer: UnsafeMutablePointer<ObjCBool>!) -> Int
```

#### Discussion

The `charIndexBuffer` contains the original characters for the glyphs. Note that a glyph at index 1 is not necessarily mapped to the character at index 1, since a glyph may be for a ligature or accent.

The `inscribeBuffer` contains the inscription attributes for each glyph, which are used to layout characters that are combined together. The possible values are described in the `Constants` section of the NSLayoutManager reference.

The `elasticBuffer` contains a Boolean value indicating whether a glyph is elastic for each glyph. An elastic glyph can be made longer at the end of a line or when needed for justification.

A subclass can override this method to interact with custom glyph storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsatstypesetter/getglyphs(in:glyphs:characterindexes:glyphinscriptions:elasticbits:))*