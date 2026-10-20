# init(text:images:imageTitles:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a list item that displays a row of images with a title below each image.

**Availability**:
- iOS 17.4+ - Deprecated in 26.0
- iPadOS 17.4+ - Deprecated in 26.0
- Mac Catalyst 17.4+ - Deprecated in 26.0

> **Deprecated**: Use initWithText:elements:allowsMultipleLines:

## Declaration

```swift
init(text: String, images: [UIImage], imageTitles: [String])
```

```objc
- (instancetype) initWithText:(NSString *) text images:(NSArray<UIImage *> *) images imageTitles:(NSArray<NSString *> *) imageTitles;
```

#### Discussion

Provide images that are display-ready. If necessary, provide light and dark variants of each image using an asset catalog, or use instances of [`UIImageAsset`](../../UIKit/uiimageasset.md) and register an image for each interface style.

To properly size your images, use the display scale of the vehicle’s primary screen, which you access from your interface controller’s [`carTraitCollection`](../cpinterfacecontroller/cartraitcollection.md) property. At runtime, use [`maximumImageSize`](./maximumimagesize.md) to determine the maximum size that CarPlay allows for an image, and [`CPMaximumNumberOfGridImages`](../cpmaximumnumberofgridimages.md) to establish the total number of images that an image row can display. The list item may display fewer images, depending on the width of the vehicle’s primary screen.

Carplay uses `UIImageAsset` to combine multiple [`UIImage`](../../UIKit/uiimage.md) objects with different trait collections into a single `UIImage` and the framework resizes images, if necessary. CarPlay doesn’t support animated images, if you provide animated images, the framework uses only the first image in each animation sequence.

The number of titles in the `imageTitles` list needs to be equal to the number of images in the `images`.

## Parameters

- `text`: The list item’s primary text.
- `images`: An array of images to display in the list item’s image row.
- `imageTitles`: An array of strings that represent the image titles.

## See Also

### Creating a List Image Row Item
- [init(text: String, images: [UIImage])](./init%28text,images%29.md)
  Creates a list item that displays a row of images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitem/init(text:images:imagetitles:))*