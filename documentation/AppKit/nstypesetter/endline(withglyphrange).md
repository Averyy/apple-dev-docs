# endLine(withGlyphRange:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets up layout parameters at the end of a line during typesetting.

**Availability**:
- macOS

## Declaration

```swift
func endLine(withGlyphRange lineGlyphRange: NSRange)
```

```objc
- (void) endLineWithGlyphRange:(NSRange) lineGlyphRange;
```

## Discussion

Concrete subclass implementations of [`layoutParagraph(at:)`](./layoutparagraph%28at%29.md) should invoke this method at the end of each line.

## Parameters

- `lineGlyphRange`: The range of glyphs laid out in the line.

## See Also

### Laying out a paragraph
- [func layoutParagraph(at: NSPointPointer) -> Int](./layoutparagraph%28at%29.md)
  Lays out glyphs in the current glyph range until the next paragraph separator is reached.
- [func beginParagraph()](./beginparagraph%28%29.md)
  Sets up layout parameters at the beginning of a paragraph.
- [func endParagraph()](./endparagraph%28%29.md)
  Sets up layout parameters at the end of a paragraph.
- [func beginLine(withGlyphAt: Int)](./beginline%28withglyphat%29.md)
  Sets up layout parameters at the beginning of a line during typesetting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/endline(withglyphrange:))*