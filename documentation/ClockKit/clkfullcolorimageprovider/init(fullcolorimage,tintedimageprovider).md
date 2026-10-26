# init(fullColorImage:tintedImageProvider:)

**Framework**: ClockKit  
**Kind**: init  
**Role**: Initializer

Creates an image provider that produces full-color and tinted images.

**Availability**:
- watchOS 6.0+ - Deprecated in 27.2

## Declaration

```swift
convenience init(fullColorImage image: UIImage, tintedImageProvider: CLKImageProvider?)
```

```objc
+ (instancetype) providerWithFullColorImage:(UIImage *) image tintedImageProvider:(CLKImageProvider *) tintedImageProvider;
```

#### Return Value

An image provider that produces full-color and tinted images. For more information about tinted images, see [`tintedImageProvider`](./tintedimageprovider.md).

#### Discussion

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
- [- initWithFullColorImage:tintedImageProvider:](./initwithfullcolorimage_tintedimageprovider_.md)
  Creates an image provider that produces full-color and tinted images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkfullcolorimageprovider/init(fullcolorimage:tintedimageprovider:))*