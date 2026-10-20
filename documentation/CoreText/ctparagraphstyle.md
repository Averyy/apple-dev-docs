# CTParagraphStyle

**Framework**: Core Text  
**Kind**: class  
**Role**: Class

Paragraph or ruler attributes in an attributed string.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
class CTParagraphStyle
```

```c
typedef const struct __CTParagraphStyle * CTParagraphStyleRef;
```

#### Overview

A paragraph style object represents a complex attribute value in an attributed string, storing a number of subattributes that affect paragraph layout for the characters of the string. Among these subattributes are alignment, tab stops, writing direction, line-breaking mode, and indentation settings.

## Topics

### Creating Paragraph Styles
- [func CTParagraphStyleCreate(UnsafePointer<CTParagraphStyleSetting>?, Int) -> CTParagraphStyle](./ctparagraphstylecreate%28_,_%29.md)
  Creates an immutable paragraph style.
- [func CTParagraphStyleCreateCopy(CTParagraphStyle) -> CTParagraphStyle](./ctparagraphstylecreatecopy%28_%29.md)
  Creates an immutable copy of a paragraph style.
### Getting the Value of a Style Specifier
- [func CTParagraphStyleGetValueForSpecifier(CTParagraphStyle, CTParagraphStyleSpecifier, Int, UnsafeMutableRawPointer) -> Bool](./ctparagraphstylegetvalueforspecifier%28_,_,_,_%29.md)
  Obtains the current value for a single setting specifier.
### Getting the Type Identifier
- [func CTParagraphStyleGetTypeID() -> CFTypeID](./ctparagraphstylegettypeid%28%29.md)
  Returns the Core Foundation type identifier of the paragraph style object.
### Data Types
- [struct CTParagraphStyleSetting](./ctparagraphstylesetting.md)
  This structure is used to alter the paragraph style.
### Constants
- [enum CTTextAlignment](./cttextalignment.md)
  Constants that specify text alignment.
- [enum CTLineBreakMode](./ctlinebreakmode.md)
  These constants specify what happens when a line is too long for its frame.
- [enum CTWritingDirection](./ctwritingdirection.md)
  These constants specify the writing direction.
- [enum CTParagraphStyleSpecifier](./ctparagraphstylespecifier.md)
  Constants used to query and modify a paragraph style object.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Opaque Types
- [class CTFont](./ctfont.md)
  A font object.
- [class CTFontCollection](./ctfontcollection.md)
  A font collection.
- [class CTFontDescriptor](./ctfontdescriptor.md)
  A font descriptor.
- [class CTFrame](./ctframe.md)
  A frame.
- [class CTFramesetter](./ctframesetter.md)
  Generate text frames.
- [class CTGlyphInfo](./ctglyphinfo.md)
  Override a font’s specified mapping from Unicode to the glyph ID.
- [class CTLine](./ctline.md)
  A line of text.
- [class CTRun](./ctrun.md)
  A glyph run.
- [class CTRunDelegate](./ctrundelegate.md)
  A run delegate.
- [class CTTextTab](./cttexttab.md)
  A tab in a paragraph style, storing an alignment type and location.
- [class CTTypesetter](./cttypesetter.md)
  A typesetter which performs line layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctparagraphstyle)*