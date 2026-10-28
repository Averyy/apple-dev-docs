# initWithFullColorImage:tintedImageProvider:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Instance Method

Creates an image provider that produces full-color and tinted images.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```objc
- (instancetype) initWithFullColorImage:(UIImage *) image tintedImageProvider:(CLKImageProvider *) tintedImageProvider;
```

## Return Value

An image provider that produces full-color and tinted images. For more information about tinted images, see [`tintedImageProvider`](./tintedimageprovider.md).

## Discussion

For information about the image sizes and masks used by the different complication families, see [Complication Images](https://developer.apple.com/design/human-interface-guidelines/watchos/icons-and-images/complication-images/).

## Parameters

- `image`: The image to display for full-color complications.
- `tintedImageProvider`: An image provider that produces images for tinted complications.

## See Also

### Creating an Image Provider
- [convenience init(fullColorImage: UIImage)](./init%28fullcolorimage%29.md)
  Creates an image provider with the specified full-color image.
- [- initWithFullColorImage:](./initwithfullcolorimage_.md)
  Creates an image provider with the specified full-color image.
- [convenience init(fullColorImage: UIImage, tintedImageProvider: CLKImageProvider?)](./init%28fullcolorimage,tintedimageprovider%29.md)
  Creates an image provider that produces full-color and tinted images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkfullcolorimageprovider/initwithfullcolorimage:tintedimageprovider:)*