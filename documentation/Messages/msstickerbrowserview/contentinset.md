# contentInset

**Framework**: Messages  
**Kind**: property  
**Role**: Instance Property

The distance that the content is inset from the edge of the browser view.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var contentInset: UIEdgeInsets { get set }
```

```objc
@property (nonatomic, assign, readwrite) UIEdgeInsets contentInset;
```

## Discussion

Use this property to add to the scrollable area around the content. The insets are measured in points. The default value is [`zero`](../../UIKit/uiedgeinsets/zero.md).

## See Also

### Managing the Browser’s Appearance
- [var contentOffset: CGPoint](./contentoffset.md)
  The distance that the content is offset from the browser’s origin.
- [func setContentOffset(CGPoint, animated: Bool)](./setcontentoffset%28_,animated%29.md)
  Sets the offset distance between the content and the browser’s origin.
- [var stickerSize: MSStickerSize](./stickersize.md)
  The size of the stickers in the browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msstickerbrowserview/contentinset)*