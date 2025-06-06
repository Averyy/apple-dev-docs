# layoutParagraph(at:)

**Framework**: AppKit  
**Kind**: method

Lays out glyphs in the current glyph range until the next paragraph separator is reached.

**Availability**:
- macOS ?+

## Declaration

```swift
func layoutParagraph(at lineFragmentOrigin: NSPointPointer) -> Int
```

#### Return Value

The next glyph index; usually the index right after the paragraph separator, but it can be inside the paragraph range if, for example, the end of the text container is reached before the paragraph separator.

#### Discussion

Concrete subclasses must implement this method. A concrete implementation must invoke [`beginParagraph()`](nstypesetter/beginparagraph().md), [`beginLine(withGlyphAt:)`](nstypesetter/beginline(withglyphat:).md), [`endLine(withGlyphRange:)`](nstypesetter/endline(withglyphrange:).md), and [`endParagraph()`](nstypesetter/endparagraph().md).

## Parameters

- `lineFragmentOrigin`: The upper-left corner of line fragment rectangle. On return,   contains the next origin.

## See Also

- [func beginParagraph()](nstypesetter/beginparagraph.md)
  Sets up layout parameters at the beginning of a paragraph.
- [func endParagraph()](nstypesetter/endparagraph.md)
  Sets up layout parameters at the end of a paragraph.
- [func beginLine(withGlyphAt: Int)](nstypesetter/beginline(withglyphat:).md)
  Sets up layout parameters at the beginning of a line during typesetting.
- [func endLine(withGlyphRange: NSRange)](nstypesetter/endline(withglyphrange:).md)
  Sets up layout parameters at the end of a line during typesetting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/layoutparagraph(at:))*