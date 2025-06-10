# init(text:images:)

**Framework**: CarPlay  
**Kind**: init

Creates a list item that displays a row of images.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
init(text: String, images: [UIImage])
```

#### Discussion

Provide images that are display-ready. If necessary, provide light and dark variants of each image using an asset catalog, or use instances of [`UIImageAsset`](https://developer.apple.com/documentation/UIKit/UIImageAsset) and register an image for each interface style.

To properly size your images, use the display scale of the vehicle’s primary screen, which you access from your interface controller’s [`carTraitCollection`](cpinterfacecontroller/cartraitcollection.md) property. At runtime, use [`maximumImageSize`](cplistimagerowitem/maximumimagesize.md) to determine the maximum size that CarPlay allows for an image, and [`CPMaximumNumberOfGridImages`](cpmaximumnumberofgridimages.md) to establish the total number of images that an image row can display. The list item may display fewer images, depending on the width of the vehicle’s primary screen.

CarPlay doesn’t support animated images. If you provide animated images, CarPlay uses only the first image in each animation sequence.

## Parameters

- `text`: The list item’s primary text.
- `images`: An array of images to display in the list item’s image row.

## See Also

- [init(text: String, images: [UIImage], imageTitles: [String])](cplistimagerowitem/init(text:images:imagetitles:).md)
  Creates a list item that displays a row of images with a title below each image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitem/init(text:images:))*