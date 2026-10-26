# NSAttributedStringMarkdownInterpretedSyntax

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

A type that represents the syntax for intepreting a Markdown string.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```c
enum NSAttributedStringMarkdownInterpretedSyntax : NSInteger;
```

## Topics

### Syntax Values
- [NSAttributedStringMarkdownInterpretedSyntaxFull](./nsattributedstringmarkdowninterpretedsyntax/nsattributedstringmarkdowninterpretedsyntaxfull.md)
  A syntax value that interprets the full Markdown syntax and produces all relevant attributes.
- [NSAttributedStringMarkdownInterpretedSyntaxInlineOnly](./nsattributedstringmarkdowninterpretedsyntax/nsattributedstringmarkdowninterpretedsyntaxinlineonly.md)
  A syntax value that parses all Markdown text, but interprets only attributes that apply to inline spans.
- [NSAttributedStringMarkdownInterpretedSyntaxInlineOnlyPreservingWhitespace](./nsattributedstringmarkdowninterpretedsyntax/nsattributedstringmarkdowninterpretedsyntaxinlineonlypreservingwhitespace.md)
  A syntax value that parses all Markdown text, but interprets only attributes that apply to inline spans, perserving white space.

## See Also

### Determining Markdown Parsing Options
- [allowsExtendedAttributes](./nsattributedstringmarkdownparsingoptions/allowsextendedattributes.md)
  A Boolean value that indicates whether parsing allows extensions to Markdown that specify extended attributes.
- [appliesSourcePositionAttributes](./nsattributedstringmarkdownparsingoptions/appliessourcepositionattributes.md)
  A Boolean value that indicates whether parsing applies attributes that indicate the position of attributed text in the original Markdown string.
- [failurePolicy](./nsattributedstringmarkdownparsingoptions/failurepolicy.md)
  The policy for handling a parsing failure.
- [NSAttributedStringMarkdownParsingFailurePolicy](./nsattributedstringmarkdownparsingfailurepolicy.md)
  A type that represents policies for handling parsing failures.
- [interpretedSyntax](./nsattributedstringmarkdownparsingoptions/interpretedsyntax.md)
  The syntax for intepreting a Markdown string.
- [languageCode](./nsattributedstringmarkdownparsingoptions/languagecode.md)
  The BCP-47 language code for this document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstringmarkdowninterpretedsyntax)*