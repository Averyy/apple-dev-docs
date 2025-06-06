# NSGlyphInfo

**Framework**: AppKit  
**Kind**: class

A glyph attribute in an attributed string.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSGlyphInfo
```

#### Overview

Glyphs are the graphic representations of characters, stored in a font, that the text system draws on a display or printed page. Before text can be laid out, the layout manager (<[`NSLayoutManager`](nslayoutmanager.md)) generates a stream of glyphs, using the character and font information specified by the attributed string and contained in the font file. [`NSGlyphInfo`](nsglyphinfo.md) represents a glyph attribute value ([`NSGlyphInfoAttributeName`](nsglyphinfoattributename.md)) in an attributed string ([`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString)) and provides a means to override the standard glyph generation process and substitute a specified glyph over the attribute’s range.

Glyph attributes are integer values that the layout manager uses to denote special handling for particular glyphs during rendering. [`NSGlyphInfo`](nsglyphinfo.md) enables you to override a font’s built-in mapping from a Unicode character code to a corresponding glyph ID. Overriding the mapping allows you to specify a variant glyph for a given character if the font contains multiple variations for that character or to specify a glyph that doesn’t have a standard mapping (such as some ligature glyphs).

## Topics

### Creating a glyph info object
- [init?(cgGlyph: CGGlyph, for: NSFont, baseString: String)](nsglyphinfo/init(cgglyph:for:basestring:).md)
  Creates a glyph info object from the specified glyph identifier and font informaton.
### Getting information about a glyph info object
- [var baseString: String](nsglyphinfo/basestring.md)
  The string containing the character represented by the glyph.
- [var glyphID: CGGlyph](nsglyphinfo/glyphid.md)
  The glyph identifier, specified as the index into the internal glyph table of the font.
### Deprecated
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
- [enum NSCharacterCollection](nscharactercollection.md)
  Values that map character identifiers to glyphs.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [typealias NSGlyph](nsglyph.md)
  The type used to specify glyphs.
- [protocol NSGlyphStorage](nsglyphstorage.md)
  A set of methods that a glyph storage object must implement to interact properly with [`NSGlyphGenerator`](nsglyphgenerator.md).
- [class NSGlyphGenerator](nsglyphgenerator.md)
  An object that performs the initial, nominal glyph generation phase in the layout process.
- [Reserved Glyph Codes](reserved-glyph-codes.md)
  These constants define reserved glyph codes.
- [enum NSFontRenderingMode](nsfontrenderingmode.md)
  The font rendering mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsglyphinfo)*