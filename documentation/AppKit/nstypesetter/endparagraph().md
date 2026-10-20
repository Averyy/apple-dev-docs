# endParagraph()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets up layout parameters at the end of a paragraph.

**Availability**:
- macOS

## Declaration

```swift
func endParagraph()
```

```objc
- (void) endParagraph;
```

#### Discussion

Concrete subclasses should invoke this method at the end of their [`layoutParagraph(at:)`](./layoutparagraph%28at%29.md) implementation.

## See Also

### Laying out a paragraph
- [func layoutParagraph(at: NSPointPointer) -> Int](./layoutparagraph%28at%29.md)
  Lays out glyphs in the current glyph range until the next paragraph separator is reached.
- [func beginParagraph()](./beginparagraph%28%29.md)
  Sets up layout parameters at the beginning of a paragraph.
- [func beginLine(withGlyphAt: Int)](./beginline%28withglyphat%29.md)
  Sets up layout parameters at the beginning of a line during typesetting.
- [func endLine(withGlyphRange: NSRange)](./endline%28withglyphrange%29.md)
  Sets up layout parameters at the end of a line during typesetting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/endparagraph())*