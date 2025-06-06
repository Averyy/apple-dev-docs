# CTTextTab

**Framework**: Core Text  
**Kind**: class

A tab in a paragraph style, storing an alignment type and location.

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
class CTTextTab
```

#### Overview

Core Text supports five alignment types: [`CTTextAlignment.left`](cttextalignment/left.md), [`CTTextAlignment.center`](cttextalignment/center.md), [`CTTextAlignment.right`](cttextalignment/right.md), [`CTTextAlignment.justified`](cttextalignment/justified.md) and [`CTTextAlignment.natural`](cttextalignment/natural.md). These alignment types are absolute, not based on the line sweep direction of text.

For example, tabbed text is always positioned to the left of a right-aligned tab, whether the line sweep direction is left to right or right to left. A tab’s location, on the other hand, is relative to the back margin. A tab set at 1.5 inches, for example, is at 1.5 inches from the right in right-to-left text.

## Topics

### Creating Text Tabs
- [func CTTextTabCreate(CTTextAlignment, Double, CFDictionary?) -> CTTextTab](cttexttabcreate(_:_:_:).md)
  Creates and initializes a new text tab object.
### Getting Text Tab Data
- [func CTTextTabGetAlignment(CTTextTab) -> CTTextAlignment](cttexttabgetalignment(_:).md)
  Returns the text alignment of the tab.
- [func CTTextTabGetLocation(CTTextTab) -> Double](cttexttabgetlocation(_:).md)
  Returns the tab’s ruler location.
- [func CTTextTabGetOptions(CTTextTab) -> CFDictionary?](cttexttabgetoptions(_:).md)
  Returns the dictionary of attributes associated with the tab.
### Getting the Type Identifier
- [func CTTextTabGetTypeID() -> CFTypeID](cttexttabgettypeid().md)
  Returns the Core Foundation type identifier of the text tab object.
### Constants
- [kCTTabColumnTerminatorsAttributeName](kcttabcolumnterminatorsattributename.md)
  Specifies the terminating character for a tab column.

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
- [class CTTypesetter](cttypesetter.md)
  A typesetter which performs line layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/cttexttab)*