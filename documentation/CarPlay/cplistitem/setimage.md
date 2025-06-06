# setImage(_:)

**Framework**: CarPlay  
**Kind**: method

Updates the list item’s image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func setImage(_ image: UIImage?)
```

#### Discussion

Provide an image that is display-ready. If necessary, provide light and dark variants using an asset catalog, or use an instance of [`UIImageAsset`](https://developer.apple.com/documentation/UIKit/UIImageAsset) and register an image for each interface style. To properly size your image, use the display scale of the vehicle’s primary screen, which you access from your interface controller’s [`carTraitCollection`](cpinterfacecontroller/cartraitcollection.md) property. At runtime, use [`maximumImageSize`](cplistitem/maximumimagesize.md) to determine the maximum size for a list item’s image.

CarPlay doesn’t support animated images. If you provide an animated image, CarPlay uses only the first image in the animation sequence.

## Parameters

- `image`: The image to display in the item’s leading region.

## See Also

- [var text: String?](cplistitem/text.md)
  The list item’s primary text.
- [func setText(String)](cplistitem/settext(_:).md)
  Updates the list item’s primary text.
- [var detailText: String?](cplistitem/detailtext.md)
  The list item’s secondary text.
- [func setDetailText(String?)](cplistitem/setdetailtext(_:).md)
  Updates the list item’s secondary text.
- [var image: UIImage?](cplistitem/image.md)
  The image that the list item displays in its leading region.
- [class var maximumImageSize: CGSize](cplistitem/maximumimagesize.md)
  The maximum size of a list item’s image and accessory image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/setimage(_:))*