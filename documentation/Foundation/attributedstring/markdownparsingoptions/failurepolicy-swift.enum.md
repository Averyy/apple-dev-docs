# AttributedString.MarkdownParsingOptions.FailurePolicy

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

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
- [AttributedString.MarkdownParsingOptions.FailurePolicy.returnPartiallyParsedIfPossible](./failurepolicy-swift.enum/returnpartiallyparsedifpossible.md)
  A policy to return a partially-parsed string, if possible.
- [AttributedString.MarkdownParsingOptions.FailurePolicy.throwError](./failurepolicy-swift.enum/throwerror.md)
  A policy to throw an error from the initializer if parsing fails.

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [Equatable](../../../Swift/equatable.md)
- [Escapable](../../../Swift/escapable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Accessing Options
- [var allowsExtendedAttributes: Bool](./allowsextendedattributes.md)
  A Boolean value that indicates whether parsing allows extensions to Markdown that specify extended attributes.
- [var appliesSourcePositionAttributes: Bool](./appliessourcepositionattributes.md)
  A Boolean value that indicates whether parsing applies attributes that indicate the position of attributed text in the original Markdown string.
- [var failurePolicy: AttributedString.MarkdownParsingOptions.FailurePolicy](./failurepolicy-swift.property.md)
  The policy for handling a parsing failure.
- [var interpretedSyntax: AttributedString.MarkdownParsingOptions.InterpretedSyntax](./interpretedsyntax-swift.property.md)
  The syntax for interpreting a Markdown string.
- [AttributedString.MarkdownParsingOptions.InterpretedSyntax](./interpretedsyntax-swift.enum.md)
  A type that represents the syntax for interpreting a Markdown string.
- [var languageCode: String?](./languagecode.md)
  The language code for this document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/markdownparsingoptions/failurepolicy-swift.enum)*