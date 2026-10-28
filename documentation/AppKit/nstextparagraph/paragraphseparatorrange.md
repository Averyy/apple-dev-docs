# paragraphSeparatorRange

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns the range of the paragraph separator in the containing text’s attributed string.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var paragraphSeparatorRange: NSTextRange? { get }
```

```objc
@property (strong, readonly, nullable) NSTextRange * paragraphSeparatorRange;
```

## Discussion

The containing text is [`NSTextContentStorage`](../nstextcontentstorage.md)’s [`attributedString`](../nstextcontentstorage/attributedstring.md).

## See Also

### Getting paragraph characteristics
- [var attributedString: NSAttributedString](./attributedstring.md)
  Returns the source attributed string.
- [var paragraphContentRange: NSTextRange?](./paragraphcontentrange.md)
  Returns the range of the paragraph in the containing text’s attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextparagraph/paragraphseparatorrange)*