# allowsExtendedAttributes

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether parsing allows extensions to Markdown that specify extended attributes.

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
@property BOOL allowsExtendedAttributes;
```

## Discussion

If this value is `NO`, the Markdown parser supports only the CommonMark syntax. The default is `NO`.

## See Also

### Determining Markdown Parsing Options
- [appliesSourcePositionAttributes](./appliessourcepositionattributes.md)
  A Boolean value that indicates whether parsing applies attributes that indicate the position of attributed text in the original Markdown string.
- [failurePolicy](./failurepolicy.md)
  The policy for handling a parsing failure.
- [NSAttributedStringMarkdownParsingFailurePolicy](../nsattributedstringmarkdownparsingfailurepolicy.md)
  A type that represents policies for handling parsing failures.
- [interpretedSyntax](./interpretedsyntax.md)
  The syntax for intepreting a Markdown string.
- [NSAttributedStringMarkdownInterpretedSyntax](../nsattributedstringmarkdowninterpretedsyntax.md)
  A type that represents the syntax for intepreting a Markdown string.
- [languageCode](./languagecode.md)
  The BCP-47 language code for this document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstringmarkdownparsingoptions/allowsextendedattributes)*