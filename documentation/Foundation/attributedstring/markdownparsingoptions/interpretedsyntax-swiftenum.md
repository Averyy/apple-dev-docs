# AttributedString.MarkdownParsingOptions.InterpretedSyntax

**Framework**: Foundation  
**Kind**: enum

A type that represents the syntax for interpreting a Markdown string.

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
enum InterpretedSyntax
```

## Topics

### Syntax Values
- [AttributedString.MarkdownParsingOptions.InterpretedSyntax.full](attributedstring/markdownparsingoptions/interpretedsyntax-swift.enum/full.md)
  A syntax value that interprets the full Markdown syntax and produces all relevant attributes.
- [AttributedString.MarkdownParsingOptions.InterpretedSyntax.inlineOnly](attributedstring/markdownparsingoptions/interpretedsyntax-swift.enum/inlineonly.md)
  A syntax value that parses all Markdown text, but interprets only attributes that apply to inline spans.
- [AttributedString.MarkdownParsingOptions.InterpretedSyntax.inlineOnlyPreservingWhitespace](attributedstring/markdownparsingoptions/interpretedsyntax-swift.enum/inlineonlypreservingwhitespace.md)
  A syntax value that parses all Markdown text, but interprets only attributes that apply to inline spans, preserving white space.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var allowsExtendedAttributes: Bool](attributedstring/markdownparsingoptions/allowsextendedattributes.md)
  A Boolean value that indicates whether parsing allows extensions to Markdown that specify extended attributes.
- [var appliesSourcePositionAttributes: Bool](attributedstring/markdownparsingoptions/appliessourcepositionattributes.md)
  A Boolean value that indicates whether parsing applies attributes that indicate the position of attributed text in the original Markdown string.
- [var failurePolicy: AttributedString.MarkdownParsingOptions.FailurePolicy](attributedstring/markdownparsingoptions/failurepolicy-swift.property.md)
  The policy for handling a parsing failure.
- [AttributedString.MarkdownParsingOptions.FailurePolicy](attributedstring/markdownparsingoptions/failurepolicy-swift.enum.md)
  A type that represents policies for handling parsing failures.
- [var interpretedSyntax: AttributedString.MarkdownParsingOptions.InterpretedSyntax](attributedstring/markdownparsingoptions/interpretedsyntax-swift.property.md)
  The syntax for interpreting a Markdown string.
- [var languageCode: String?](attributedstring/markdownparsingoptions/languagecode.md)
  The language code for this document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/markdownparsingoptions/interpretedsyntax-swift.enum)*