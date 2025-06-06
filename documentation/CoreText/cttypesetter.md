# CTTypesetter

**Framework**: Core Text  
**Kind**: class

A typesetter which performs line layout.

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
class CTTypesetter
```

#### Overview

Line layout includes word wrapping, hyphenation, and line breaking in either vertical or horizontal rectangles. A typesetter object takes as input an attributed string and produces a line of typeset glyphs (composed into glyph runs) in a [`CTLine`](ctline.md) object. The typesetter performs character-to-glyph encoding, glyph ordering, and positional operations, such as kerning, tracking, and baseline adjustments. If multiline layout is needed, it is performed by a [`CTFramesetter`](ctframesetter.md) object, which calls into the typesetter to generate the typeset lines to fill the frame.

A [`CTFramesetter`](ctframesetter.md) encapsulates a typesetter and provides a reference to it as a convenience, but a caller may also choose to create a freestanding typesetter.

## Topics

### Creating a Typesetter
- [func CTTypesetterCreateWithAttributedString(CFAttributedString) -> CTTypesetter](cttypesettercreatewithattributedstring(_:).md)
  Creates an immutable typesetter object using an attributed string.
- [func CTTypesetterCreateWithAttributedStringAndOptions(CFAttributedString, CFDictionary?) -> CTTypesetter?](cttypesettercreatewithattributedstringandoptions(_:_:).md)
  Creates an immutable typesetter object using an attributed string and a dictionary of options.
### Creating Lines
- [func CTTypesetterCreateLine(CTTypesetter, CFRange) -> CTLine](cttypesettercreateline(_:_:).md)
  Creates an immutable line from the typesetter.
- [func CTTypesetterCreateLineWithOffset(CTTypesetter, CFRange, Double) -> CTLine](cttypesettercreatelinewithoffset(_:_:_:).md)
  Creates an immutable line from the typesetter at a specified line offset.
### Breaking Lines
- [func CTTypesetterSuggestLineBreak(CTTypesetter, CFIndex, Double) -> CFIndex](cttypesettersuggestlinebreak(_:_:_:).md)
  Suggests a contextual line breakpoint based on the width provided.
- [func CTTypesetterSuggestLineBreakWithOffset(CTTypesetter, CFIndex, Double, Double) -> CFIndex](cttypesettersuggestlinebreakwithoffset(_:_:_:_:).md)
  Suggests a contextual line breakpoint based on the width provided and the specified offset.
- [func CTTypesetterSuggestClusterBreak(CTTypesetter, CFIndex, Double) -> CFIndex](cttypesettersuggestclusterbreak(_:_:_:).md)
  Suggests a cluster line breakpoint based on the width provided.
- [func CTTypesetterSuggestClusterBreakWithOffset(CTTypesetter, CFIndex, Double, Double) -> CFIndex](cttypesettersuggestclusterbreakwithoffset(_:_:_:_:).md)
  Suggests a cluster line breakpoint based on the specified width and line offset.
### Getting the Type Identifier
- [func CTTypesetterGetTypeID() -> CFTypeID](cttypesettergettypeid().md)
  Returns the Core Foundation type identifier of the typesetter object.
### Constants
- [Typesetter Options](typesetter-options.md)
  Control aspects of the typesetter’s text processing.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/cttypesetter)*