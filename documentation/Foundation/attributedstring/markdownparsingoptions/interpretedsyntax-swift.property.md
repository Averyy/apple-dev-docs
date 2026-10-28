# interpretedSyntax

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

## Discussion

If your Markdown data uses syntax that this setting excludes, the parser still parses it and includes its text in the final result. However, the relevant text won’t have attributes.

## See Also

### Accessing Options
- [var allowsExtendedAttributes: Bool](./allowsextendedattributes.md)
  A Boolean value that indicates whether parsing allows extensions to Markdown that specify extended attributes.
- [var appliesSourcePositionAttributes: Bool](./appliessourcepositionattributes.md)
  A Boolean value that indicates whether parsing applies attributes that indicate the position of attributed text in the original Markdown string.
- [var failurePolicy: AttributedString.MarkdownParsingOptions.FailurePolicy](./failurepolicy-swift.property.md)
  The policy for handling a parsing failure.
- [AttributedString.MarkdownParsingOptions.FailurePolicy](./failurepolicy-swift.enum.md)
  A type that represents policies for handling parsing failures.
- [AttributedString.MarkdownParsingOptions.InterpretedSyntax](./interpretedsyntax-swift.enum.md)
  A type that represents the syntax for interpreting a Markdown string.
- [var languageCode: String?](./languagecode.md)
  The language code for this document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/markdownparsingoptions/interpretedsyntax-swift.property)*