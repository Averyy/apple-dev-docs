# sticker

**Framework**: Messages  
**Kind**: property

The displayed sticker object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var sticker: MSSticker? { get set }
```

#### Discussion

Set this property to `nil` to remove the current sticker.

If you are using Auto Layout, setting the [`sticker`](msstickerview/sticker.md) property changes the view’s intrinsic content size. A view with a `nil`-valued [`sticker`](msstickerview/sticker.md) property does not have an intrinsic content size (the intrinsic content size is set to `{UIViewNoIntrinsicMetric, UIViewNoIntrinsicMetric}`). Otherwise, the view’s intrinsic content size is set equal to the size of the sticker’s image file (in points).

If you are not using Auto Layout, setting the sticker property does not change the view’s size. Call [`sizeToFit()`](https://developer.apple.com/documentation/UIKit/UIView/sizeToFit()) to adjust the size of the view to match the sticker.

## See Also

- [init(frame: CGRect, sticker: MSSticker?)](msstickerview/init(frame:sticker:).md)
  Initializes a new sticker view with the provided sticker and frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msstickerview/sticker)*