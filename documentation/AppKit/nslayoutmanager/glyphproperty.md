# NSLayoutManager.GlyphProperty

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Glyph properties.

**Availability**:
- macOS 10.11+

## Declaration

```swift
struct GlyphProperty
```

```c
enum NSGlyphProperty : NSInteger;
```

## Topics

### Glyph properties
- [static var null: NSLayoutManager.GlyphProperty](./glyphproperty/null.md)
  The null glyph, which the layout manager ignores.
- [static var controlCharacter: NSLayoutManager.GlyphProperty](./glyphproperty/controlcharacter.md)
  A glyph representing a control character.
- [static var elastic: NSLayoutManager.GlyphProperty](./glyphproperty/elastic.md)
  A glyph with a changeable width, such as a white space character.
- [static var nonBaseCharacter: NSLayoutManager.GlyphProperty](./glyphproperty/nonbasecharacter.md)
  A glyph that combines several properties.
### Initializers
- [init(rawValue: Int)](./glyphproperty/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Accessing glyphs
- [func getGlyphs(in: NSRange, glyphs: UnsafeMutablePointer<CGGlyph>?, properties: UnsafeMutablePointer<NSLayoutManager.GlyphProperty>?, characterIndexes: UnsafeMutablePointer<Int>?, bidiLevels: UnsafeMutablePointer<UInt8>?) -> Int](./getglyphs%28in,glyphs,properties,characterindexes,bidilevels%29.md)
  Fills a passed-in buffer with a sequence of glyphs.
- [func cgGlyph(at: Int) -> CGGlyph](./cgglyph%28at%29.md)
  Returns the glyph at the specified index.
- [func cgGlyph(at: Int, isValidIndex: UnsafeMutablePointer<ObjCBool>?) -> CGGlyph](./cgglyph%28at,isvalidindex%29.md)
  Returns the glyph at the specified index along with information about whether the glyph index is valid.
- [func setGlyphs(UnsafePointer<CGGlyph>, properties: UnsafePointer<NSLayoutManager.GlyphProperty>, characterIndexes: UnsafePointer<Int>, font: NSFont, forGlyphRange: NSRange)](./setglyphs%28_,properties,characterindexes,font,forglyphrange%29.md)
  Stores the initial glyphs and glyph properties for a character range.
- [func characterIndexForGlyph(at: Int) -> Int](./characterindexforglyph%28at%29.md)
  Returns the index in the text storage for the first character of the specified glyph.
- [func glyphIndexForCharacter(at: Int) -> Int](./glyphindexforcharacter%28at%29.md)
  Returns the index of the first glyph of the character at the specified index.
- [func isValidGlyphIndex(Int) -> Bool](./isvalidglyphindex%28_%29.md)
  Indicates whether the specified index refers to a valid glyph.
- [var numberOfGlyphs: Int](./numberofglyphs.md)
  The number of glyphs in the layout manager.
- [func propertyForGlyph(at: Int) -> NSLayoutManager.GlyphProperty](./propertyforglyph%28at%29.md)
  Returns the glyph property of the glyph at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/glyphproperty)*