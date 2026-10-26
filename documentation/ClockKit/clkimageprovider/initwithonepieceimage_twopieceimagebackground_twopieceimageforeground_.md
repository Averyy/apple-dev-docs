# initWithOnePieceImage:twoPieceImageBackground:twoPieceImageForeground:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Instance Method

Creates and returns an image provider with both one-piece and two-piece images.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```objc
- (instancetype) initWithOnePieceImage:(UIImage *) onePieceImage twoPieceImageBackground:(UIImage *) twoPieceImageBackground twoPieceImageForeground:(UIImage *) twoPieceImageForeground;
```

#### Return Value

An image provider with both the one-piece and two-piece images.

#### Discussion

Use this method when you want to display a two-piece image in multicolor environments. In monochrome environments, the image provider still displays the one-piece image. After creating the image provider, you can customize the tint color applied to your images by modifying the [`tintColor`](./tintcolor.md) property.

## Parameters

- `onePieceImage`: The one-piece image to use. The image must be a template image, where only the alpha channel is used to define the image contents. This parameter must not be `nil`.
- `twoPieceImageBackground`: The background to use for a two-piece image. The image must be a template image, where only the alpha channel is used to define the image contents. This parameter must not be `nil`.
- `twoPieceImageForeground`: The foreground to use for a two-piece image. The image must be a template image, where only the alpha channel is used to define the image contents. This parameter must not be `nil`.

## See Also

### Creating an Image Provider
- [convenience init(onePieceImage: UIImage)](./init%28onepieceimage%29.md)
  Creates and returns an image provider with the specified one-piece image.
- [- initWithOnePieceImage:](./initwithonepieceimage_.md)
  Creates and returns an image provider with the specified one-piece image.
- [convenience init(onePieceImage: UIImage, twoPieceImageBackground: UIImage?, twoPieceImageForeground: UIImage?)](./init%28onepieceimage,twopieceimagebackground,twopieceimageforeground%29.md)
  Creates and returns an image provider with both one-piece and two-piece images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkimageprovider/initwithonepieceimage:twopieceimagebackground:twopieceimageforeground:)*