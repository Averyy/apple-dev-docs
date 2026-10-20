# sticker

**Framework**: Messages  
**Kind**: property  
**Role**: Instance Property

The displayed sticker object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var sticker: MSSticker? { get set }
```

```objc
@property (nonatomic, strong, readwrite, nullable) MSSticker * sticker;
```

#### Discussion

Set this property to `nil` to remove the current sticker.

If you are using Auto Layout, setting the [`sticker`](./sticker.md) property changes the view’s intrinsic content size. A view with a `nil`-valued [`sticker`](./sticker.md) property does not have an intrinsic content size (the intrinsic content size is set to `{UIViewNoIntrinsicMetric, UIViewNoIntrinsicMetric}`). Otherwise, the view’s intrinsic content size is set equal to the size of the sticker’s image file (in points).

If you are not using Auto Layout, setting the sticker property does not change the view’s size. Call [`sizeToFit()`](../../UIKit/uiview/sizetofit%28%29.md) to adjust the size of the view to match the sticker.

## See Also

### Working with Sticker Views
- [init(frame: CGRect, sticker: MSSticker?)](./init%28frame,sticker%29.md)
  Initializes a new sticker view with the provided sticker and frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msstickerview/sticker)*