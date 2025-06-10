# AttributedString.MarkdownParsingOptions.InterpretedSyntax.inlineOnlyPreservingWhitespace

**Framework**: Foundation  
**Kind**: case

A syntax value that parses all Markdown text, but interprets only attributes that apply to inline spans, preserving white space.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
case inlineOnlyPreservingWhitespace
```

#### Discussion

This value behaves like [`AttributedString.MarkdownParsingOptions.InterpretedSyntax.inlineOnly`](attributedstring/markdownparsingoptions/interpretedsyntax-swift.enum/inlineonly.md), but doesn’t interpret multiple consecutive instances of white space as a single separator space. All whitespace characters appear in the result as the source specifies.

## See Also

- [AttributedString.MarkdownParsingOptions.InterpretedSyntax.full](attributedstring/markdownparsingoptions/interpretedsyntax-swift.enum/full.md)
  A syntax value that interprets the full Markdown syntax and produces all relevant attributes.
- [AttributedString.MarkdownParsingOptions.InterpretedSyntax.inlineOnly](attributedstring/markdownparsingoptions/interpretedsyntax-swift.enum/inlineonly.md)
  A syntax value that parses all Markdown text, but interprets only attributes that apply to inline spans.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/markdownparsingoptions/interpretedsyntax-swift.enum/inlineonlypreservingwhitespace)*