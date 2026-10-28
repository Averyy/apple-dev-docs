# NSAttributedStringMarkdownInterpretedSyntaxInlineOnly

**Framework**: Foundation  
**Kind**: case  
**Role**: Enumeration Case

A syntax value that parses all Markdown text, but interprets only attributes that apply to inline spans.

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
NSAttributedStringMarkdownInterpretedSyntaxInlineOnly
```

## Discussion

With this syntax, the parser doesn’t apply attributes that differentiate blocks, like [`presentationIntentAttributeName`](../nsattributedstring/key/presentationintentattributename.md). However, extended attributes apply to inline spans, so the parser includes them, if the [`allowsExtendedAttributes`](../nsattributedstringmarkdownparsingoptions/allowsextendedattributes.md) property allows them.

## See Also

### Syntax Values
- [NSAttributedStringMarkdownInterpretedSyntaxFull](./nsattributedstringmarkdowninterpretedsyntaxfull.md)
  A syntax value that interprets the full Markdown syntax and produces all relevant attributes.
- [NSAttributedStringMarkdownInterpretedSyntaxInlineOnlyPreservingWhitespace](./nsattributedstringmarkdowninterpretedsyntaxinlineonlypreservingwhitespace.md)
  A syntax value that parses all Markdown text, but interprets only attributes that apply to inline spans, perserving white space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstringmarkdowninterpretedsyntax/nsattributedstringmarkdowninterpretedsyntaxinlineonly)*