# stickerSize

**Framework**: Messages  
**Kind**: property  
**Role**: Instance Property

The size of the stickers in the browser.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var stickerSize: MSStickerSize { get }
```

```objc
@property (nonatomic, assign, readonly) MSStickerSize stickerSize;
```

#### Discussion

For a list of possible size values, see [`MSStickerSize`](../msstickersize.md).

## See Also

### Managing the Browser’s Appearance
- [var contentInset: UIEdgeInsets](./contentinset.md)
  The distance that the content is inset from the edge of the browser view.
- [var contentOffset: CGPoint](./contentoffset.md)
  The distance that the content is offset from the browser’s origin.
- [func setContentOffset(CGPoint, animated: Bool)](./setcontentoffset%28_,animated%29.md)
  Sets the offset distance between the content and the browser’s origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msstickerbrowserview/stickersize)*