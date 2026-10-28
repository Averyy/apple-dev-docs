# beginLine(withGlyphAt:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets up layout parameters at the beginning of a line during typesetting.

**Availability**:
- macOS

## Declaration

```swift
func beginLine(withGlyphAt glyphIndex: Int)
```

```objc
- (void) beginLineWithGlyphAtIndex:(NSUInteger) glyphIndex;
```

## Discussion

Concrete subclass implementations of [`layoutParagraph(at:)`](./layoutparagraph%28at%29.md) should invoke this method at the beginning of each line.

## Parameters

- `glyphIndex`: The index of the first glyph to be laid out in the line.

## See Also

### Laying out a paragraph
- [func layoutParagraph(at: NSPointPointer) -> Int](./layoutparagraph%28at%29.md)
  Lays out glyphs in the current glyph range until the next paragraph separator is reached.
- [func beginParagraph()](./beginparagraph%28%29.md)
  Sets up layout parameters at the beginning of a paragraph.
- [func endParagraph()](./endparagraph%28%29.md)
  Sets up layout parameters at the end of a paragraph.
- [func endLine(withGlyphRange: NSRange)](./endline%28withglyphrange%29.md)
  Sets up layout parameters at the end of a line during typesetting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/beginline(withglyphat:))*