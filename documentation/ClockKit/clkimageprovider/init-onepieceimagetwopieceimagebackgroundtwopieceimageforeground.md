# init(onePieceImage:twoPieceImageBackground:twoPieceImageForeground:)

**Framework**: ClockKit  
**Kind**: init

Creates and returns an image provider with both one-piece and two-piece images.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
convenience init(onePieceImage: UIImage, twoPieceImageBackground: UIImage?, twoPieceImageForeground: UIImage?)
```

#### Return Value

An image provider with both the one-piece and two-piece images.

#### Discussion

Use this method when you want to display a two-piece image in multicolor environments. In monochrome environments, the image provider still displays the one-piece image. After creating the image provider, you can customize the tint color applied to your images by modifying the [`tintColor`](clkimageprovider/tintcolor.md) property.

## Parameters

- `onePieceImage`: The one-piece image to use. The image must be a template image, where only the alpha channel is used to define the image contents. This parameter must not be  .
- `twoPieceImageBackground`: The background to use for a two-piece image. The image must be a template image, where only the alpha channel is used to define the image contents. This parameter must not be  .
- `twoPieceImageForeground`: The foreground to use for a two-piece image. The image must be a template image, where only the alpha channel is used to define the image contents. This parameter must not be  .

## See Also

- [convenience init(onePieceImage: UIImage)](clkimageprovider/init(onepieceimage:).md)
  Creates and returns an image provider with the specified one-piece image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkimageprovider/init(onepieceimage:twopieceimagebackground:twopieceimageforeground:))*