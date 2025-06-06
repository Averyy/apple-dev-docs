# init(characterIdentifier:collection:baseString:)

**Framework**: AppKit  
**Kind**: init

Instantiates and returns an `NSGlyphInfo` object using a character identifier and a character collection.

**Availability**:
- macOS ?+

## Declaration

```swift
init?(characterIdentifier cid: Int, collection characterCollection: NSCharacterCollection, baseString string: String)
```

#### Return Value

The created `NSGlyphInfo` object or `nil` if the object couldn’t be created.

## Parameters

- `cid`: A character identifier.
- `characterCollection`: A string constant representing a character collection. Possible values are described in  .
- `string`: The part of the attributed string the returned instance is intended to override.

## See Also

- [Cocoa Text Architecture Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/TextFonts/Conceptual/CocoaTextArchitecture/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009459)
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
- [enum NSCharacterCollection](nscharactercollection.md)
  Values that map character identifiers to glyphs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsglyphinfo/init(characteridentifier:collection:basestring:))*