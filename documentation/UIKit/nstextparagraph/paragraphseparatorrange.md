# paragraphSeparatorRange

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Returns the range of the paragraph separator in the containing text’s attributed string.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextparagraph/paragraphseparatorrange)*