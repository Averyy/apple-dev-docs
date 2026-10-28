# contentOffset

**Framework**: Messages  
**Kind**: property  
**Role**: Instance Property

The distance that the content is offset from the browser’s origin.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var contentOffset: CGPoint { get set }
```

```objc
@property (nonatomic, assign, readwrite) CGPoint contentOffset;
```

## Discussion

Positive `x` values shift the content to the left. Positive `y` values shift the content upward. The default value is [`CGPointZero`](../../CoreGraphics/cgpointzero.md).

## See Also

### Managing the Browser’s Appearance
- [var contentInset: UIEdgeInsets](./contentinset.md)
  The distance that the content is inset from the edge of the browser view.
- [func setContentOffset(CGPoint, animated: Bool)](./setcontentoffset%28_,animated%29.md)
  Sets the offset distance between the content and the browser’s origin.
- [var stickerSize: MSStickerSize](./stickersize.md)
  The size of the stickers in the browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msstickerbrowserview/contentoffset)*