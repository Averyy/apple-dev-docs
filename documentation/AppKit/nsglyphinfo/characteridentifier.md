# characterIdentifier

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s character identifier (CID).

**Availability**:
- macOS

## Declaration

```swift
var characterIdentifier: Int { get }
```

```objc
@property (readonly) NSUInteger characterIdentifier;
```

## See Also

### Deprecated
- [init?(characterIdentifier: Int, collection: NSCharacterCollection, baseString: String)](./init%28characteridentifier,collection,basestring%29.md)
  Instantiates and returns an `NSGlyphInfo` object using a character identifier and a character collection.
- [init?(glyph: NSGlyph, forFont: NSFont, baseString: String)](./init%28glyph,forfont,basestring%29.md)
  Instantiates and returns a glyph information object using a glyph index and a specified font.
- [init?(glyphName: String, forFont: NSFont, baseString: String)](./init%28glyphname,forfont,basestring%29.md)
  Instantiates and returns a glyph information object using a glyph name and a specified font.
- [var characterCollection: NSCharacterCollection](./charactercollection.md)
  A value specifying the glyph–to–character identifier mapping of the receiver.
- [var glyphName: String?](./glyphname.md)
  The receiver’s glyph name.
- [enum NSCharacterCollection](../nscharactercollection.md)
  Values that map character identifiers to glyphs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsglyphinfo/characteridentifier)*