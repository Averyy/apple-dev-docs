# beginLine(withGlyphAt:)

**Framework**: AppKit  
**Kind**: method

Sets up layout parameters at the beginning of a line during typesetting.

**Availability**:
- macOS ?+

## Declaration

```swift
func beginLine(withGlyphAt glyphIndex: Int)
```

#### Discussion

Concrete subclass implementations of [`layoutParagraph(at:)`](nstypesetter/layoutparagraph(at:).md) should invoke this method at the beginning of each line.

## Parameters

- `glyphIndex`: The index of the first glyph to be laid out in the line.

## See Also

- [func layoutParagraph(at: NSPointPointer) -> Int](nstypesetter/layoutparagraph(at:).md)
  Lays out glyphs in the current glyph range until the next paragraph separator is reached.
- [func beginParagraph()](nstypesetter/beginparagraph.md)
  Sets up layout parameters at the beginning of a paragraph.
- [func endParagraph()](nstypesetter/endparagraph.md)
  Sets up layout parameters at the end of a paragraph.
- [func endLine(withGlyphRange: NSRange)](nstypesetter/endline(withglyphrange:).md)
  Sets up layout parameters at the end of a line during typesetting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/beginline(withglyphat:))*