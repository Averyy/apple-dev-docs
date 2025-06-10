# AttributedString.MarkdownParsingOptions.InterpretedSyntax.inlineOnly

**Framework**: Foundation  
**Kind**: case

A syntax value that parses all Markdown text, but interprets only attributes that apply to inline spans.

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
case inlineOnly
```

#### Discussion

With this syntax, the parser doesn’t apply attributes that differentiate blocks. However, extended attributes apply to inline spans, so the parser includes them, if the [`allowsExtendedAttributes`](attributedstring/markdownparsingoptions/allowsextendedattributes.md) property allows them.

## See Also

- [AttributedString.MarkdownParsingOptions.InterpretedSyntax.full](attributedstring/markdownparsingoptions/interpretedsyntax-swift.enum/full.md)
  A syntax value that interprets the full Markdown syntax and produces all relevant attributes.
- [AttributedString.MarkdownParsingOptions.InterpretedSyntax.inlineOnlyPreservingWhitespace](attributedstring/markdownparsingoptions/interpretedsyntax-swift.enum/inlineonlypreservingwhitespace.md)
  A syntax value that parses all Markdown text, but interprets only attributes that apply to inline spans, preserving white space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/markdownparsingoptions/interpretedsyntax-swift.enum/inlineonly)*