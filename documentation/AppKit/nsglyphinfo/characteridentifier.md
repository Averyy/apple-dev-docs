# characterIdentifier

**Framework**: AppKit  
**Kind**: property

The receiver’s character identifier (CID).

**Availability**:
- macOS ?+

## Declaration

```swift
var characterIdentifier: Int { get }
```

## See Also

- [init?(characterIdentifier: Int, collection: NSCharacterCollection, baseString: String)](nsglyphinfo/init(characteridentifier:collection:basestring:).md)
  Instantiates and returns an `NSGlyphInfo` object using a character identifier and a character collection.
- [init?(glyph: NSGlyph, forFont: NSFont, baseString: String)](nsglyphinfo/init(glyph:forfont:basestring:).md)
  Instantiates and returns a glyph information object using a glyph index and a specified font.
- [init?(glyphName: String, forFont: NSFont, baseString: String)](nsglyphinfo/init(glyphname:forfont:basestring:).md)
  Instantiates and returns a glyph information object using a glyph name and a specified font.
- [var characterCollection: NSCharacterCollection](nsglyphinfo/charactercollection.md)
  A value specifying the glyph–to–character identifier mapping of the receiver.
- [var glyphName: String?](nsglyphinfo/glyphname.md)
  The receiver’s glyph name.
- [enum NSCharacterCollection](nscharactercollection.md)
  Values that map character identifiers to glyphs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsglyphinfo/characteridentifier)*