# endLine(withGlyphRange:)

**Framework**: AppKit  
**Kind**: method

Sets up layout parameters at the end of a line during typesetting.

**Availability**:
- macOS ?+

## Declaration

```swift
func endLine(withGlyphRange lineGlyphRange: NSRange)
```

#### Discussion

Concrete subclass implementations of [`layoutParagraph(at:)`](nstypesetter/layoutparagraph(at:).md) should invoke this method at the end of each line.

## Parameters

- `lineGlyphRange`: The range of glyphs laid out in the line.

## See Also

- [func layoutParagraph(at: NSPointPointer) -> Int](nstypesetter/layoutparagraph(at:).md)
  Lays out glyphs in the current glyph range until the next paragraph separator is reached.
- [func beginParagraph()](nstypesetter/beginparagraph.md)
  Sets up layout parameters at the beginning of a paragraph.
- [func endParagraph()](nstypesetter/endparagraph.md)
  Sets up layout parameters at the end of a paragraph.
- [func beginLine(withGlyphAt: Int)](nstypesetter/beginline(withglyphat:).md)
  Sets up layout parameters at the beginning of a line during typesetting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/endline(withglyphrange:))*