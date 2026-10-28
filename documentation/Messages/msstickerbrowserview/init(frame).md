# init(frame:)

**Framework**: Messages  
**Kind**: init  
**Role**: Initializer

Creates a new sticker browser containing medium-sized stickers.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(frame: CGRect)
```

```objc
- (instancetype) initWithFrame:(CGRect) frame;
```

## Return Value

A newly initialized sticker browser view.

## Parameters

- `frame`: A rectangular frame for the view, measured in points. The origin of the frame is relative to its superview. This method uses the provided rectangle to set the view’s [`center`](../../UIKit/uiview/center.md) and [`bounds`](../../UIKit/uiview/bounds.md) properties.

## See Also

### Creating Sticker Browser Views
- [init(frame: CGRect, stickerSize: MSStickerSize)](./init%28frame,stickersize%29.md)
  Creates a new sticker browser containing stickers of the specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msstickerbrowserview/init(frame:))*