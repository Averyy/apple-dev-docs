# initWithFullColorImage:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Instance Method

Creates an image provider with the specified full-color image.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```objc
- (instancetype) initWithFullColorImage:(UIImage *) image;
```

#### Return Value

A full-color image provider.

#### Discussion

For information about the image sizes and masks, see [Apple Watch Human Interface Guidelines](https://developer.apple.com/watch/human-interface-guidelines/).

## Parameters

- `image`: The image to display.

## See Also

### Creating an Image Provider
- [convenience init(fullColorImage: UIImage)](./init%28fullcolorimage%29.md)
  Creates an image provider with the specified full-color image.
- [convenience init(fullColorImage: UIImage, tintedImageProvider: CLKImageProvider?)](./init%28fullcolorimage,tintedimageprovider%29.md)
  Creates an image provider that produces full-color and tinted images.
- [- initWithFullColorImage:tintedImageProvider:](./initwithfullcolorimage_tintedimageprovider_.md)
  Creates an image provider that produces full-color and tinted images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkfullcolorimageprovider/initwithfullcolorimage:)*