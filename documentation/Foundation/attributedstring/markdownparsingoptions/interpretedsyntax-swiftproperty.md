# interpretedSyntax

**Framework**: Foundation  
**Kind**: property

The syntax for interpreting a Markdown string.

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
var interpretedSyntax: AttributedString.MarkdownParsingOptions.InterpretedSyntax
```

#### Discussion

If your Markdown data uses syntax that this setting excludes, the parser still parses it and includes its text in the final result. However, the relevant text won’t have attributes.

## See Also

- [var allowsExtendedAttributes: Bool](attributedstring/markdownparsingoptions/allowsextendedattributes.md)
  A Boolean value that indicates whether parsing allows extensions to Markdown that specify extended attributes.
- [var appliesSourcePositionAttributes: Bool](attributedstring/markdownparsingoptions/appliessourcepositionattributes.md)
  A Boolean value that indicates whether parsing applies attributes that indicate the position of attributed text in the original Markdown string.
- [var failurePolicy: AttributedString.MarkdownParsingOptions.FailurePolicy](attributedstring/markdownparsingoptions/failurepolicy-swift.property.md)
  The policy for handling a parsing failure.
- [AttributedString.MarkdownParsingOptions.FailurePolicy](attributedstring/markdownparsingoptions/failurepolicy-swift.enum.md)
  A type that represents policies for handling parsing failures.
- [AttributedString.MarkdownParsingOptions.InterpretedSyntax](attributedstring/markdownparsingoptions/interpretedsyntax-swift.enum.md)
  A type that represents the syntax for interpreting a Markdown string.
- [var languageCode: String?](attributedstring/markdownparsingoptions/languagecode.md)
  The language code for this document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/markdownparsingoptions/interpretedsyntax-swift.property)*