# NSAttributedStringMarkdownInterpretedSyntaxInlineOnlyPreservingWhitespace

**Framework**: Foundation  
**Kind**: case  
**Role**: Enumeration Case

A syntax value that parses all Markdown text, but interprets only attributes that apply to inline spans, perserving white space.

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
NSAttributedStringMarkdownInterpretedSyntaxInlineOnlyPreservingWhitespace
```

## Discussion

This value behaves like [`NSAttributedStringMarkdownInterpretedSyntaxInlineOnly`](./nsattributedstringmarkdowninterpretedsyntaxinlineonly.md), but doesn’t interpret multiple consecutive instances of white space as a single separator space. All whitespace characters appear in the result as the source specifies.

## See Also

### Syntax Values
- [NSAttributedStringMarkdownInterpretedSyntaxFull](./nsattributedstringmarkdowninterpretedsyntaxfull.md)
  A syntax value that interprets the full Markdown syntax and produces all relevant attributes.
- [NSAttributedStringMarkdownInterpretedSyntaxInlineOnly](./nsattributedstringmarkdowninterpretedsyntaxinlineonly.md)
  A syntax value that parses all Markdown text, but interprets only attributes that apply to inline spans.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstringmarkdowninterpretedsyntax/nsattributedstringmarkdowninterpretedsyntaxinlineonlypreservingwhitespace)*