# NSCharacterCollection

**Framework**: AppKit  
**Kind**: enum

Values that map character identifiers to glyphs.

**Availability**:
- macOS ?+

## Declaration

```swift
enum NSCharacterCollection
```

## Topics

### Collections
- [NSCharacterCollection.identityMappingCharacterCollection](nscharactercollection/identitymappingcharactercollection.md)
  Indicates that the character identifier is equal to the glyph index.
- [NSCharacterCollection.adobeCNS1CharacterCollection](nscharactercollection/adobecns1charactercollection.md)
  Indicates the Adobe-CNS1 mapping.
- [NSCharacterCollection.adobeGB1CharacterCollection](nscharactercollection/adobegb1charactercollection.md)
  Indicates the Adobe-GB1 mapping.
- [NSCharacterCollection.adobeJapan1CharacterCollection](nscharactercollection/adobejapan1charactercollection.md)
  Indicates the Adobe-Japan1 mapping.
- [NSCharacterCollection.adobeJapan2CharacterCollection](nscharactercollection/adobejapan2charactercollection.md)
  Indicates the Adobe-Japan2 mapping.
- [NSCharacterCollection.adobeKorea1CharacterCollection](nscharactercollection/adobekorea1charactercollection.md)
  Indicates the Adobe-Korea1 mapping.
### Initializers
- [init?(rawValue: UInt)](nscharactercollection/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [init?(characterIdentifier: Int, collection: NSCharacterCollection, baseString: String)](nsglyphinfo/init(characteridentifier:collection:basestring:).md)
  Instantiates and returns an `NSGlyphInfo` object using a character identifier and a character collection.
- [init?(glyph: NSGlyph, forFont: NSFont, baseString: String)](nsglyphinfo/init(glyph:forfont:basestring:).md)
  Instantiates and returns a glyph information object using a glyph index and a specified font.
- [init?(glyphName: String, forFont: NSFont, baseString: String)](nsglyphinfo/init(glyphname:forfont:basestring:).md)
  Instantiates and returns a glyph information object using a glyph name and a specified font.
- [var characterIdentifier: Int](nsglyphinfo/characteridentifier.md)
  The receiver’s character identifier (CID).
- [var characterCollection: NSCharacterCollection](nsglyphinfo/charactercollection.md)
  A value specifying the glyph–to–character identifier mapping of the receiver.
- [var glyphName: String?](nsglyphinfo/glyphname.md)
  The receiver’s glyph name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscharactercollection)*