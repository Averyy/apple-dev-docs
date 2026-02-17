# update(_:)

**Framework**: CarPlay  
**Kind**: method

Adds, removes, reorders, or updates the images in the list item’s image row.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func update(_ gridImages: [UIImage])
```

#### Discussion

This method is multipurpose. Use it to add new images to the image row, and to remove or reorder existing images.

Provide images that are display-ready. If necessary, provide light and dark variants of each image using an asset catalog, or use instances of [`UIImageAsset`](https://developer.apple.com/documentation/UIKit/UIImageAsset) and register an image for each interface style.

To properly size your images, use the display scale of the vehicle’s primary screen, which you access from your interface controller’s [`carTraitCollection`](cpinterfacecontroller/cartraitcollection.md) property. At runtime, use [`maximumImageSize`](cplistimagerowitem/maximumimagesize.md) to determine the maximum size that CarPlay allows for an image, and [`CPMaximumNumberOfGridImages`](cpmaximumnumberofgridimages.md) to establish the total number of images that an image row can display. The list item may display fewer images, depending on the width of the vehicle’s primary screen.

CarPlay doesn’t support animated images. If you provide animated images, CarPlay uses only the first image in each animation sequence.

## Parameters

- `gridImages`: An array of images to display in the list item’s image row.

## See Also

- [var text: String?](cplistimagerowitem/text.md)
  The list item’s primary text.
- [var gridImages: [UIImage]](cplistimagerowitem/gridimages.md)
  The images that appear in the list item’s image row.
- [class var maximumImageSize: CGSize](cplistimagerowitem/maximumimagesize.md)
  The maximum size of an image that an image row can display.
- [let CPMaximumNumberOfGridImages: Int](cpmaximumnumberofgridimages.md)
  The maximum number of images that an image row can contain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitem/update(_:))*