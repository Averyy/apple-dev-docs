# init(frame:sticker:)

**Framework**: Messages  
**Kind**: init

Initializes a new sticker view with the provided sticker and frame.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(frame: CGRect, sticker: MSSticker?)
```

#### Return Value

A newly initialized sticker view.

#### Discussion

If the sticker image is larger than the view’s frame, the view scales down the sticker to fit. If the frame is larger than the sticker image, the view centers the image in the frame.

## Parameters

- `frame`: A rectangular frame for the view, measured in points. The origin of the frame is relative to its superview. This method uses the provided rectangle to set the view’s [`center`](https://developer.apple.com/documentation/UIKit/UIView/center) and [`bounds`](https://developer.apple.com/documentation/UIKit/UIView/bounds) properties.
- `sticker`: The sticker object to be displayed. Pass `nil` to create an empty sticker view.

## See Also

- [var sticker: MSSticker?](msstickerview/sticker.md)
  The displayed sticker object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msstickerview/init(frame:sticker:))*