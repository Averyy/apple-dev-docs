# interpretedSyntax

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The syntax for intepreting a Markdown string.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```objc
@property NSAttributedStringMarkdownInterpretedSyntax interpretedSyntax;
```

#### Discussion

If your Markdown data uses syntax that this setting excludes, the parser still parses it and includes its text in the final result. However, the relevant text won’t have attributes.

## See Also

### Determining Markdown Parsing Options
- [allowsExtendedAttributes](./allowsextendedattributes.md)
  A Boolean value that indicates whether parsing allows extensions to Markdown that specify extended attributes.
- [appliesSourcePositionAttributes](./appliessourcepositionattributes.md)
  A Boolean value that indicates whether parsing applies attributes that indicate the position of attributed text in the original Markdown string.
- [failurePolicy](./failurepolicy.md)
  The policy for handling a parsing failure.
- [NSAttributedStringMarkdownParsingFailurePolicy](../nsattributedstringmarkdownparsingfailurepolicy.md)
  A type that represents policies for handling parsing failures.
- [NSAttributedStringMarkdownInterpretedSyntax](../nsattributedstringmarkdowninterpretedsyntax.md)
  A type that represents the syntax for intepreting a Markdown string.
- [languageCode](./languagecode.md)
  The BCP-47 language code for this document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstringmarkdownparsingoptions/interpretedsyntax)*