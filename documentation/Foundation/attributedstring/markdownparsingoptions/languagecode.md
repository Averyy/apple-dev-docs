# languageCode

**Framework**: Foundation  
**Kind**: property

The language code for this document.

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
var languageCode: String?
```

#### Discussion

This value is a [`BCP-47`](https://developer.apple.comhttps://tools.ietf.org/search/bcp47) language code. If not `nil`, the string applies the [`languageIdentifier`](nsattributedstring/key/languageidentifier.md) attribute to any range in the returned string that doesn’t otherwise specify a language attribute. The default is `nil`, which applies no attributes.

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
- [AttributedString.MarkdownParsingOptions.InterpretedSyntax](attributedstring/markdownparsingoptions/interpretedsyntax-swift.enum.md)
  A type that represents the syntax for interpreting a Markdown string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/markdownparsingoptions/languagecode)*