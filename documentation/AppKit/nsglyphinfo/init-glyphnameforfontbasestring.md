# init(glyphName:forFont:baseString:)

**Framework**: AppKit  
**Kind**: init

Instantiates and returns a glyph information object using a glyph name and a specified font.

**Availability**:
- macOS ?+

## Declaration

```swift
init?(glyphName: String, for font: NSFont, baseString string: String)
```

#### Return Value

The created `NSGlyphInfo` object or `nil` if the object couldn’t be created.

## Parameters

- `glyphName`: The name of the glyph.
- `font`: The font object to be associated with the returned   object,
- `string`: The part of the attributed string the returned instance is intended to override.

## See Also

- [init?(characterIdentifier: Int, collection: NSCharacterCollection, baseString: String)](nsglyphinfo/init(characteridentifier:collection:basestring:).md)
  Instantiates and returns an `NSGlyphInfo` object using a character identifier and a character collection.
- [init?(glyph: NSGlyph, forFont: NSFont, baseString: String)](nsglyphinfo/init(glyph:forfont:basestring:).md)
  Instantiates and returns a glyph information object using a glyph index and a specified font.
- [var characterIdentifier: Int](nsglyphinfo/characteridentifier.md)
  The receiver’s character identifier (CID).
- [var characterCollection: NSCharacterCollection](nsglyphinfo/charactercollection.md)
  A value specifying the glyph–to–character identifier mapping of the receiver.
- [var glyphName: String?](nsglyphinfo/glyphname.md)
  The receiver’s glyph name.
- [enum NSCharacterCollection](nscharactercollection.md)
  Values that map character identifiers to glyphs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsglyphinfo/init(glyphname:forfont:basestring:))*