# CTGlyphInfo

**Framework**: Core Text  
**Kind**: class

Override a font’s specified mapping from Unicode to the glyph ID.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class CTGlyphInfo
```

## Topics

### Getting the GlyphInfo Type
- [func CTGlyphInfoGetTypeID() -> CFTypeID](ctglyphinfogettypeid().md)
  Returns the Core Foundation type identifier of the glyph info object
### Creating GlyphInfo Objects
- [func CTGlyphInfoCreateWithGlyphName(CFString, CTFont, CFString) -> CTGlyphInfo?](ctglyphinfocreatewithglyphname(_:_:_:).md)
  Creates an immutable glyph info object with a glyph name.
- [func CTGlyphInfoCreateWithGlyph(CGGlyph, CTFont, CFString) -> CTGlyphInfo?](ctglyphinfocreatewithglyph(_:_:_:).md)
  Creates an immutable glyph info object with a glyph index.
- [func CTGlyphInfoCreateWithCharacterIdentifier(CGFontIndex, CTCharacterCollection, CFString) -> CTGlyphInfo?](ctglyphinfocreatewithcharacteridentifier(_:_:_:).md)
  Creates an immutable glyph info object with a character identifier.
### Getting GlyphInfo Data
- [func CTGlyphInfoGetGlyphName(CTGlyphInfo) -> CFString?](ctglyphinfogetglyphname(_:).md)
  Retrieves the glyph name for a glyph info object, if that object exists.
- [func CTGlyphInfoGetCharacterIdentifier(CTGlyphInfo) -> CGFontIndex](ctglyphinfogetcharacteridentifier(_:).md)
  Gets the character identifier for a glyph info object.
- [func CTGlyphInfoGetCharacterCollection(CTGlyphInfo) -> CTCharacterCollection](ctglyphinfogetcharactercollection(_:).md)
  Gets the character collection for a glyph info object.
- [func CTGlyphInfoGetGlyph(CTGlyphInfo) -> CGGlyph](ctglyphinfogetglyph(_:).md)
  Retrieves the glyph for a glyph info, if that object exists.
### Constants
- [enum CTCharacterCollection](ctcharactercollection.md)
  Constants that specify character collections.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [class CTFont](ctfont.md)
  A font object.
- [class CTFontCollection](ctfontcollection.md)
  A font collection.
- [class CTFontDescriptor](ctfontdescriptor.md)
  A font descriptor.
- [class CTFrame](ctframe.md)
  A frame.
- [class CTFramesetter](ctframesetter.md)
  Generate text frames.
- [class CTLine](ctline.md)
  A line of text.
- [class CTParagraphStyle](ctparagraphstyle.md)
  Paragraph or ruler attributes in an attributed string.
- [class CTRun](ctrun.md)
  A glyph run.
- [class CTRunDelegate](ctrundelegate.md)
  A run delegate.
- [class CTTextTab](cttexttab.md)
  A tab in a paragraph style, storing an alignment type and location.
- [class CTTypesetter](cttypesetter.md)
  A typesetter which performs line layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctglyphinfo)*