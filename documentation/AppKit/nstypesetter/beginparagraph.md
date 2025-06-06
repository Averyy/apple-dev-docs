# beginParagraph()

**Framework**: AppKit  
**Kind**: method

Sets up layout parameters at the beginning of a paragraph.

**Availability**:
- macOS ?+

## Declaration

```swift
func beginParagraph()
```

#### Discussion

Concrete subclasses should invoke this method at the beginning of their [`layoutParagraph(at:)`](nstypesetter/layoutparagraph(at:).md) implementation.

## See Also

- [func layoutParagraph(at: NSPointPointer) -> Int](nstypesetter/layoutparagraph(at:).md)
  Lays out glyphs in the current glyph range until the next paragraph separator is reached.
- [func endParagraph()](nstypesetter/endparagraph.md)
  Sets up layout parameters at the end of a paragraph.
- [func beginLine(withGlyphAt: Int)](nstypesetter/beginline(withglyphat:).md)
  Sets up layout parameters at the beginning of a line during typesetting.
- [func endLine(withGlyphRange: NSRange)](nstypesetter/endline(withglyphrange:).md)
  Sets up layout parameters at the end of a line during typesetting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/beginparagraph())*