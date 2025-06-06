# setContentOffset(_:animated:)

**Framework**: Messages  
**Kind**: method

Sets the offset distance between the content and the browser’s origin.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func setContentOffset(_ contentOffset: CGPoint, animated: Bool)
```

#### Discussion

Increasing the offset’s `x` value shifts the content to the left. Increasing the offset’s `y` value shifts the content upward.

## Parameters

- `contentOffset`: The distance that the content is offset from the browser’s origin.
- `animated`: A Boolean value that determines whether the change is animated. If  , the change is animated at a constant velocity. If  , the change takes place immediately.

## See Also

- [var contentInset: UIEdgeInsets](msstickerbrowserview/contentinset.md)
  The distance that the content is inset from the edge of the browser view.
- [var contentOffset: CGPoint](msstickerbrowserview/contentoffset.md)
  The distance that the content is offset from the browser’s origin.
- [var stickerSize: MSStickerSize](msstickerbrowserview/stickersize.md)
  The size of the stickers in the browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msstickerbrowserview/setcontentoffset(_:animated:))*