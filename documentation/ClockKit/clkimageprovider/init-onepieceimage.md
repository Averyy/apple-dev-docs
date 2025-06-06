# init(onePieceImage:)

**Framework**: ClockKit  
**Kind**: init

Creates and returns an image provider with the specified one-piece image.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
convenience init(onePieceImage: UIImage)
```

#### Return Value

An image provider with only the one-piece image.

#### Discussion

Use this method to create an image provider with only a one-piece image. The resulting image provider displays the one-piece image in all contexts. After creating the image provider, you can customize the tint color applied to your image by modifying the [`tintColor`](clkimageprovider/tintcolor.md) property.

## Parameters

- `onePieceImage`: The image to display. The image must be a template image, where only the alpha channel is used to define the image contents. This parameter must not be  .

## See Also

- [convenience init(onePieceImage: UIImage, twoPieceImageBackground: UIImage?, twoPieceImageForeground: UIImage?)](clkimageprovider/init(onepieceimage:twopieceimagebackground:twopieceimageforeground:).md)
  Creates and returns an image provider with both one-piece and two-piece images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkimageprovider/init(onepieceimage:))*