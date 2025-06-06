# contentOffset

**Framework**: Messages  
**Kind**: property

The distance that the content is offset from the browser’s origin.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var contentOffset: CGPoint { get set }
```

#### Discussion

Positive `x` values shift the content to the left. Positive `y` values shift the content upward. The default value is [`CGPointZero`](https://developer.apple.com/documentation/CoreGraphics/CGPointZero).

## See Also

- [var contentInset: UIEdgeInsets](msstickerbrowserview/contentinset.md)
  The distance that the content is inset from the edge of the browser view.
- [func setContentOffset(CGPoint, animated: Bool)](msstickerbrowserview/setcontentoffset(_:animated:).md)
  Sets the offset distance between the content and the browser’s origin.
- [var stickerSize: MSStickerSize](msstickerbrowserview/stickersize.md)
  The size of the stickers in the browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msstickerbrowserview/contentoffset)*