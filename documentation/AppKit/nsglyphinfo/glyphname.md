# glyphName

**Framework**: AppKit  
**Kind**: property

The receiver’s glyph name.

**Availability**:
- macOS ?+

## Declaration

```swift
var glyphName: String? { get }
```

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
- [enum NSCharacterCollection](nscharactercollection.md)
  Values that map character identifiers to glyphs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsglyphinfo/glyphname)*