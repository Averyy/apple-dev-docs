# init(text:detailText:image:accessoryImage:accessoryType:)

**Framework**: CarPlay  
**Kind**: init

Creates a list item that displays an accessory beside its content.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
init(text: String?, detailText: String?, image: UIImage?, accessoryImage: UIImage?, accessoryType: CPListItemAccessoryType)
```

#### Discussion

If you specify an image, CarPlay sets `accessoryType` to [`CPListItemAccessoryType.none`](cplistitemaccessorytype/none.md).

Provide an image that is display-ready. If necessary, provide light and dark variants using an asset catalog, or use an instance of [`UIImageAsset`](https://developer.apple.com/documentation/UIKit/UIImageAsset) and register an image for each interface style. To properly size your image, use the display scale of the vehicle’s primary screen, which you access from your interface controller’s [`carTraitCollection`](cpinterfacecontroller/cartraitcollection.md) property. At runtime, use [`maximumImageSize`](cplistitem/maximumimagesize.md) to determine the maximum size for a list item’s image and accessory image.

CarPlay doesn’t support animated images. If you provide an animated image, CarPlay uses only the first image in the animation sequence.

## Parameters

- `text`: The list item’s primary text.
- `detailText`: The list item’s secondary text.
- `image`: The image that the list item displays in its leading region.
- `accessoryImage`: The image that the list item displays in its trailing region.
- `accessoryType`: The accessory that the list item displays in its trailing region.

## See Also

- [init(text: String?, detailText: String?)](cplistitem/init(text:detailtext:).md)
  Creates a list item with primary and secondary text.
- [init(text: String?, detailText: String?, image: UIImage?)](cplistitem/init(text:detailtext:image:).md)
  Creates a list item with primary text, secondary text, and an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/init(text:detailtext:image:accessoryimage:accessorytype:))*