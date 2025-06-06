# init(fullColorImage:tintedImageProvider:)

**Framework**: ClockKit  
**Kind**: init

Creates an image provider that produces full-color and tinted images.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
convenience init(fullColorImage image: UIImage, tintedImageProvider: CLKImageProvider?)
```

#### Return Value

An image provider that produces full-color and tinted images. For more information about tinted images, see [`tintedImageProvider`](clkfullcolorimageprovider/tintedimageprovider.md).

#### Discussion

For information about the image sizes and masks used by the different complication families, see [`Complication Images`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/watchos/icons-and-images/complication-images/).

## Parameters

- `image`: The image to display for full-color complications.
- `tintedImageProvider`: An image provider that produces images for tinted complications.

## See Also

- [convenience init(fullColorImage: UIImage)](clkfullcolorimageprovider/init(fullcolorimage:).md)
  Creates an image provider with the specified full-color image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkfullcolorimageprovider/init(fullcolorimage:tintedimageprovider:))*