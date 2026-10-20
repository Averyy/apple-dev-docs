# AttributedString.MarkdownSourcePosition

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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
- [init(startLine: Int, startColumn: Int, endLine: Int, endColumn: Int)](./markdownsourceposition/init%28startline,startcolumn,endline,endcolumn%29.md)
  Creates a Markdown source position instance from its start and end line and column.
### Inspecting Markdown Source Position Properties
- [let startLine: Int](./markdownsourceposition/startline.md)
  The line where the text begins in the Markdown source.
- [let startColumn: Int](./markdownsourceposition/startcolumn.md)
  The column where the text begins in the Markdown source.
- [let endLine: Int](./markdownsourceposition/endline.md)
  The line where the text ends in the Markdown source.
- [let endColumn: Int](./markdownsourceposition/endcolumn.md)
  The column where the text ends in the Markdown source.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/markdownsourceposition)*