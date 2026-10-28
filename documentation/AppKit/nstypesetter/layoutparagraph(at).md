# layoutParagraph(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Lays out glyphs in the current glyph range until the next paragraph separator is reached.

**Availability**:
- macOS

## Declaration

```swift
func layoutParagraph(at lineFragmentOrigin: NSPointPointer) -> Int
```

```objc
- (NSUInteger) layoutParagraphAtPoint:(NSPointPointer) lineFragmentOrigin;
```

## Return Value

The next glyph index; usually the index right after the paragraph separator, but it can be inside the paragraph range if, for example, the end of the text container is reached before the paragraph separator.

## Discussion

Concrete subclasses must implement this method. A concrete implementation must invoke [`beginParagraph()`](./beginparagraph%28%29.md), [`beginLine(withGlyphAt:)`](./beginline%28withglyphat%29.md), [`endLine(withGlyphRange:)`](./endline%28withglyphrange%29.md), and [`endParagraph()`](./endparagraph%28%29.md).

## Parameters

- `lineFragmentOrigin`: The upper-left corner of line fragment rectangle. On return, `lineFragmentOrigin` contains the next origin.

## See Also

### Laying out a paragraph
- [func beginParagraph()](./beginparagraph%28%29.md)
  Sets up layout parameters at the beginning of a paragraph.
- [func endParagraph()](./endparagraph%28%29.md)
  Sets up layout parameters at the end of a paragraph.
- [func beginLine(withGlyphAt: Int)](./beginline%28withglyphat%29.md)
  Sets up layout parameters at the beginning of a line during typesetting.
- [func endLine(withGlyphRange: NSRange)](./endline%28withglyphrange%29.md)
  Sets up layout parameters at the end of a line during typesetting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/layoutparagraph(at:))*