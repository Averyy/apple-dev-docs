# init(allowsExtendedAttributes:interpretedSyntax:failurePolicy:languageCode:)

**Framework**: Foundation  
**Kind**: init

Creates a Markdown parsing options instance with the specified values.

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
init(allowsExtendedAttributes: Bool = false, interpretedSyntax: AttributedString.MarkdownParsingOptions.InterpretedSyntax = .full, failurePolicy: AttributedString.MarkdownParsingOptions.FailurePolicy = .throwError, languageCode: String? = nil)
```

## Parameters

- `allowsExtendedAttributes`: A Boolean value that indicates whether parsing allows extensions to Markdown that specify extended attributes.
- `interpretedSyntax`: The syntax for intepreting a Markdown string.
- `failurePolicy`: The policy for handling a parsing failure.
- `languageCode`: The   language code for this document.

## See Also

- [init(allowsExtendedAttributes: Bool, interpretedSyntax: AttributedString.MarkdownParsingOptions.InterpretedSyntax, failurePolicy: AttributedString.MarkdownParsingOptions.FailurePolicy, languageCode: String?, appliesSourcePositionAttributes: Bool)](attributedstring/markdownparsingoptions/init(allowsextendedattributes:interpretedsyntax:failurepolicy:languagecode:appliessourcepositionattributes:).md)
  Creates a Markdown parsing options instance with the specified values, optionally marking the source position of attributed text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/markdownparsingoptions/init(allowsextendedattributes:interpretedsyntax:failurepolicy:languagecode:))*