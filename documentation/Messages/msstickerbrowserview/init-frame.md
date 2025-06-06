# init(frame:)

**Framework**: Messages  
**Kind**: init

Creates a new sticker browser containing medium-sized stickers.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
init(frame: CGRect)
```

#### Return Value

A newly initialized sticker browser view.

## Parameters

- `frame`: A rectangular frame for the view, measured in points. The origin of the frame is relative to its superview. This method uses the provided rectangle to set the view’s   and   properties.

## See Also

- [init(frame: CGRect, stickerSize: MSStickerSize)](msstickerbrowserview/init(frame:stickersize:).md)
  Creates a new sticker browser containing stickers of the specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msstickerbrowserview/init(frame:))*