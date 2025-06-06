# contentInset

**Framework**: Messages  
**Kind**: property

The distance that the content is inset from the edge of the browser view.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var contentInset: UIEdgeInsets { get set }
```

#### Discussion

Use this property to add to the scrollable area around the content. The insets are measured in points. The default value is [`zero`](https://developer.apple.com/documentation/UIKit/UIEdgeInsets/zero).

## See Also

- [var contentOffset: CGPoint](msstickerbrowserview/contentoffset.md)
  The distance that the content is offset from the browser’s origin.
- [func setContentOffset(CGPoint, animated: Bool)](msstickerbrowserview/setcontentoffset(_:animated:).md)
  Sets the offset distance between the content and the browser’s origin.
- [var stickerSize: MSStickerSize](msstickerbrowserview/stickersize.md)
  The size of the stickers in the browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msstickerbrowserview/contentinset)*