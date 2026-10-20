# init(characterIdentifier:collection:baseString:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Instantiates and returns an `NSGlyphInfo` object using a character identifier and a character collection.

**Availability**:
- macOS

## Declaration

```swift
init?(characterIdentifier cid: Int, collection characterCollection: NSCharacterCollection, baseString string: String)
```

```objc
+ (NSGlyphInfo *) glyphInfoWithCharacterIdentifier:(NSUInteger) cid collection:(NSCharacterCollection) characterCollection baseString:(NSString *) string;
```

#### Return Value

The created `NSGlyphInfo` object or `nil` if the object couldn’t be created.

## Parameters

- `cid`: A character identifier.
- `characterCollection`: A string constant representing a character collection. Possible values are described in [`NSCharacterCollection`](../nscharactercollection.md).
- `string`: The part of the attributed string the returned instance is intended to override.

## See Also

### Deprecated
- [init?(glyph: NSGlyph, forFont: NSFont, baseString: String)](./init%28glyph,forfont,basestring%29.md)
  Instantiates and returns a glyph information object using a glyph index and a specified font.
- [init?(glyphName: String, forFont: NSFont, baseString: String)](./init%28glyphname,forfont,basestring%29.md)
  Instantiates and returns a glyph information object using a glyph name and a specified font.
- [var characterIdentifier: Int](./characteridentifier.md)
  The receiver’s character identifier (CID).
- [var characterCollection: NSCharacterCollection](./charactercollection.md)
  A value specifying the glyph–to–character identifier mapping of the receiver.
- [var glyphName: String?](./glyphname.md)
  The receiver’s glyph name.
- [enum NSCharacterCollection](../nscharactercollection.md)
  Values that map character identifiers to glyphs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsglyphinfo/init(characteridentifier:collection:basestring:))*