# AttributedString.MarkdownSourcePosition

**Framework**: Foundation  
**Kind**: struct

The position of attributed string text in its original Markdown source string.

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
struct MarkdownSourcePosition
```

## Topics

### Creating a Markdown Source Position
- [init(startLine: Int, startColumn: Int, endLine: Int, endColumn: Int)](attributedstring/markdownsourceposition/init(startline:startcolumn:endline:endcolumn:).md)
  Creates a Markdown source position instance from its start and end line and column.
### Inspecting Markdown Source Position Properties
- [let startLine: Int](attributedstring/markdownsourceposition/startline.md)
  The line where the text begins in the Markdown source.
- [let startColumn: Int](attributedstring/markdownsourceposition/startcolumn.md)
  The column where the text begins in the Markdown source.
- [let endLine: Int](attributedstring/markdownsourceposition/endline.md)
  The line where the text ends in the Markdown source.
- [let endColumn: Int](attributedstring/markdownsourceposition/endcolumn.md)
  The column where the text ends in the Markdown source.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/markdownsourceposition)*