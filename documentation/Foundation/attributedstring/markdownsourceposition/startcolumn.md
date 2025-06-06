# startColumn

**Framework**: Foundation  
**Kind**: property

The column where the text begins in the Markdown source.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
let startColumn: Int
```

#### Discussion

This property uses `1`-based counting. Columns represent UTF-8 indices; for multi-byte characters, the column indicates the first byte.

## See Also

- [let startLine: Int](attributedstring/markdownsourceposition/startline.md)
  The line where the text begins in the Markdown source.
- [let endLine: Int](attributedstring/markdownsourceposition/endline.md)
  The line where the text ends in the Markdown source.
- [let endColumn: Int](attributedstring/markdownsourceposition/endcolumn.md)
  The column where the text ends in the Markdown source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/markdownsourceposition/startcolumn)*