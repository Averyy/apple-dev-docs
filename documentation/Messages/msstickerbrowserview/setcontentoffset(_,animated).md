# setContentOffset(_:animated:)

**Framework**: Messages  
**Kind**: method  
**Role**: Instance Method

Sets the offset distance between the content and the browser’s origin.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func setContentOffset(_ contentOffset: CGPoint, animated: Bool)
```

```objc
- (void) setContentOffset:(CGPoint) contentOffset animated:(BOOL) animated;
```

#### Discussion

Increasing the offset’s `x` value shifts the content to the left. Increasing the offset’s `y` value shifts the content upward.

## Parameters

- `contentOffset`: The distance that the content is offset from the browser’s origin.
- `animated`: A Boolean value that determines whether the change is animated. If [`true`](../../Swift/true.md), the change is animated at a constant velocity. If [`false`](../../Swift/false.md), the change takes place immediately.

## See Also

### Managing the Browser’s Appearance
- [var contentInset: UIEdgeInsets](./contentinset.md)
  The distance that the content is inset from the edge of the browser view.
- [var contentOffset: CGPoint](./contentoffset.md)
  The distance that the content is offset from the browser’s origin.
- [var stickerSize: MSStickerSize](./stickersize.md)
  The size of the stickers in the browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msstickerbrowserview/setcontentoffset(_:animated:))*