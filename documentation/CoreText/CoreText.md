# Core Text

**Framework**: Coretext  
**Kind**: module

Create text layouts, optimize font handling, and access font metrics and glyph data.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

#### Overview

Core Text provides a low-level programming interface for laying out text and handling fonts. The Core Text layout engine is designed for high performance, ease of use, and close integration with [`Core Foundation`](https://developer.apple.com/documentation/CoreFoundation). The text layout API provides high-quality typesetting, including character-to-glyph conversion, with ligatures, kerning, and so on. The complementary Core Text font technology provides automatic font substitution (cascading), font descriptors and collections, easy access to font metrics and glyph data, and many other features.

> **Note**: All individual functions in Core Text are thread-safe. Font objects ([`CTFont`](ctfont.md), [`CTFontDescriptor`](ctfontdescriptor.md), and associated objects) can be used simultaneously by multiple operations, work queues, or threads. However, the layout objects ([`CTTypesetter`](cttypesetter.md), [`CTFramesetter`](ctframesetter.md), [`CTRun`](ctrun.md), [`CTLine`](ctline.md), [`CTFrame`](ctframe.md), and associated objects) should be used in a single operation, work queue, or thread.

## Topics

### Opaque Types
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
- [class CTGlyphInfo](ctglyphinfo.md)
  Override a font’s specified mapping from Unicode to the glyph ID.
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
### Reference
- [Styling Attributed Strings](styling-attributed-strings.md)
  Attributes to which Core Text responds when placed in a `CFAttributedString` object.
- [Core Text Structures](core-text-structures.md)
- [Core Text Enumerations](core-text-enumerations.md)
- [Core Text Constants](core-text-constants.md)
- [Core Text Functions](core-text-functions.md)
- [Core Text Data Types](core-text-data-types.md)
- [SFNT Support](sfnt-support.md)
### Macros
- [Macros](coretext-macros.md)
### Classes
- [class CTRubyAnnotation](ctrubyannotation.md)
### Protocols
- [protocol CTAdaptiveImageProviding](ctadaptiveimageproviding.md)

## See Also

- [Core Text Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/StringsTextFonts/Conceptual/CoreText_Programming/Introduction/Introduction.html#//apple_ref/doc/uid/TP40005533)


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreText)*