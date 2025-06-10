# NSLayoutManager.GlyphProperty

**Framework**: AppKit  
**Kind**: struct

Glyph properties.

**Availability**:
- macOS 10.11+

## Declaration

```swift
struct GlyphProperty
```

## Topics

### Glyph properties
- [static var null: NSLayoutManager.GlyphProperty](nslayoutmanager/glyphproperty/null.md)
  The null glyph, which the layout manager ignores.
- [static var controlCharacter: NSLayoutManager.GlyphProperty](nslayoutmanager/glyphproperty/controlcharacter.md)
  A glyph representing a control character.
- [static var elastic: NSLayoutManager.GlyphProperty](nslayoutmanager/glyphproperty/elastic.md)
  A glyph with a changeable width, such as a white space character.
- [static var nonBaseCharacter: NSLayoutManager.GlyphProperty](nslayoutmanager/glyphproperty/nonbasecharacter.md)
  A glyph that combines several properties.
### Initializers
- [init(rawValue: Int)](nslayoutmanager/glyphproperty/init(rawvalue:).md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func getGlyphs(in: NSRange, glyphs: UnsafeMutablePointer<CGGlyph>?, properties: UnsafeMutablePointer<NSLayoutManager.GlyphProperty>?, characterIndexes: UnsafeMutablePointer<Int>?, bidiLevels: UnsafeMutablePointer<UInt8>?) -> Int](nslayoutmanager/getglyphs(in:glyphs:properties:characterindexes:bidilevels:).md)
  Fills a passed-in buffer with a sequence of glyphs.
- [func cgGlyph(at: Int) -> CGGlyph](nslayoutmanager/cgglyph(at:).md)
  Returns the glyph at the specified index.
- [func cgGlyph(at: Int, isValidIndex: UnsafeMutablePointer<ObjCBool>?) -> CGGlyph](nslayoutmanager/cgglyph(at:isvalidindex:).md)
  Returns the glyph at the specified index along with information about whether the glyph index is valid.
- [func setGlyphs(UnsafePointer<CGGlyph>, properties: UnsafePointer<NSLayoutManager.GlyphProperty>, characterIndexes: UnsafePointer<Int>, font: NSFont, forGlyphRange: NSRange)](nslayoutmanager/setglyphs(_:properties:characterindexes:font:forglyphrange:).md)
  Stores the initial glyphs and glyph properties for a character range.
- [func characterIndexForGlyph(at: Int) -> Int](nslayoutmanager/characterindexforglyph(at:).md)
  Returns the index in the text storage for the first character of the specified glyph.
- [func glyphIndexForCharacter(at: Int) -> Int](nslayoutmanager/glyphindexforcharacter(at:).md)
  Returns the index of the first glyph of the character at the specified index.
- [func isValidGlyphIndex(Int) -> Bool](nslayoutmanager/isvalidglyphindex(_:).md)
  Indicates whether the specified index refers to a valid glyph.
- [var numberOfGlyphs: Int](nslayoutmanager/numberofglyphs.md)
  The number of glyphs in the layout manager.
- [func propertyForGlyph(at: Int) -> NSLayoutManager.GlyphProperty](nslayoutmanager/propertyforglyph(at:).md)
  Returns the glyph property of the glyph at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/glyphproperty)*