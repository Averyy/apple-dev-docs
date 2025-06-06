# paragraphContentRange

**Framework**: AppKit  
**Kind**: property

Returns the range of the paragraph in the containing text’s attributed string.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var paragraphContentRange: NSTextRange? { get }
```

#### Discussion

The containing text is [`NSTextContentStorage`](nstextcontentstorage.md)’s [`attributedString`](nstextcontentstorage/attributedstring.md).

## See Also

- [var attributedString: NSAttributedString](nstextparagraph/attributedstring.md)
  Returns the source attributed string.
- [var paragraphSeparatorRange: NSTextRange?](nstextparagraph/paragraphseparatorrange.md)
  Returns the range of the paragraph separator in the containing text’s attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextparagraph/paragraphcontentrange)*