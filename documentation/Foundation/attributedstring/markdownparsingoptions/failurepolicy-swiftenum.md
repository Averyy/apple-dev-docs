# AttributedString.MarkdownParsingOptions.FailurePolicy

**Framework**: Foundation  
**Kind**: enum

A type that represents policies for handling parsing failures.

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
enum FailurePolicy
```

## Topics

### Declaring Failure Policies
- [AttributedString.MarkdownParsingOptions.FailurePolicy.returnPartiallyParsedIfPossible](attributedstring/markdownparsingoptions/failurepolicy-swift.enum/returnpartiallyparsedifpossible.md)
  A policy to return a partially-parsed string, if possible.
- [AttributedString.MarkdownParsingOptions.FailurePolicy.throwError](attributedstring/markdownparsingoptions/failurepolicy-swift.enum/throwerror.md)
  A policy to throw an error from the initializer if parsing fails.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var allowsExtendedAttributes: Bool](attributedstring/markdownparsingoptions/allowsextendedattributes.md)
  A Boolean value that indicates whether parsing allows extensions to Markdown that specify extended attributes.
- [var appliesSourcePositionAttributes: Bool](attributedstring/markdownparsingoptions/appliessourcepositionattributes.md)
  A Boolean value that indicates whether parsing applies attributes that indicate the position of attributed text in the original Markdown string.
- [var failurePolicy: AttributedString.MarkdownParsingOptions.FailurePolicy](attributedstring/markdownparsingoptions/failurepolicy-swift.property.md)
  The policy for handling a parsing failure.
- [var interpretedSyntax: AttributedString.MarkdownParsingOptions.InterpretedSyntax](attributedstring/markdownparsingoptions/interpretedsyntax-swift.property.md)
  The syntax for interpreting a Markdown string.
- [AttributedString.MarkdownParsingOptions.InterpretedSyntax](attributedstring/markdownparsingoptions/interpretedsyntax-swift.enum.md)
  A type that represents the syntax for interpreting a Markdown string.
- [var languageCode: String?](attributedstring/markdownparsingoptions/languagecode.md)
  The language code for this document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/markdownparsingoptions/failurepolicy-swift.enum)*