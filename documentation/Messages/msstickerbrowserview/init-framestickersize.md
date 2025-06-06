# init(frame:stickerSize:)

**Framework**: Messages  
**Kind**: init

Creates a new sticker browser containing stickers of the specified size.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
init(frame: CGRect, stickerSize: MSStickerSize)
```

#### Return Value

A newly initialized sticker browser view.

## Parameters

- `frame`: A rectangular frame for the view, measured in points. The origin of the frame is relative to its superview. This method uses the provided rectangle to set the view’s   and   properties.
- `stickerSize`: The size of the stickers. For a list of possible values, see  .

## See Also

- [init(frame: CGRect)](msstickerbrowserview/init(frame:).md)
  Creates a new sticker browser containing medium-sized stickers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msstickerbrowserview/init(frame:stickersize:))*