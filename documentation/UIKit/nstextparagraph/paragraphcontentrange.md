# paragraphContentRange

**Framework**: UIKit  
**Kind**: property

Returns the range of the paragraph in the containing text’s attributed string.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextparagraph/paragraphcontentrange)*