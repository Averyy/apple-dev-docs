# setAccessoryImage(_:)

**Framework**: CarPlay  
**Kind**: method

Updates the list item’s accessory image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
func setAccessoryImage(_ accessoryImage: UIImage?)
```

#### Discussion

Provide an image that is display-ready. If necessary, provide light and dark variants using an asset catalog, or use an instance of [`UIImageAsset`](https://developer.apple.com/documentation/UIKit/UIImageAsset) and register an image for each interface style. To properly size your image, use the display scale of the vehicle’s primary screen, which you access from your interface controller’s [`carTraitCollection`](cpinterfacecontroller/cartraitcollection.md) property. At runtime, use [`maximumImageSize`](cplistitem/maximumimagesize.md) to determine the maximum size for a list item’s accessory image.

CarPlay doesn’t support animated images. If you provide an animated image, CarPlay uses only the first image in the animation sequence.

CarPlay sets the `accessoryType` property’s value to [`CPListItemAccessoryType.none`](cplistitemaccessorytype/none.md) when you call this method.

## Parameters

- `accessoryImage`: The image to display in the item’s trailing region.

## See Also

- [var accessoryType: CPListItemAccessoryType](cplistitem/accessorytype.md)
  The accessory that the list item displays in its trailing region.
- [enum CPListItemAccessoryType](cplistitemaccessorytype.md)
  The accessory types that a list item can display.
- [var accessoryImage: UIImage?](cplistitem/accessoryimage.md)
  The image that the list item displays in its trailing region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/setaccessoryimage(_:))*