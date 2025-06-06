# init(trailingItem:trailingImage:)

**Framework**: CarPlay  
**Kind**: init

Creates a trailing configuration that contains an item and an image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
init(trailingItem: CPMessageTrailingItem, trailingImage: UIImage?)
```

#### Discussion

Provide an image that is display-ready. If necessary, provide light and dark variants using an asset catalog, or use an instance of [`UIImageAsset`](https://developer.apple.com/documentation/UIKit/UIImageAsset) and register an image for each interface style. To properly size your image, use the display scale of the vehicle’s primary screen, which you access from your interface controller’s [`carTraitCollection`](cpinterfacecontroller/cartraitcollection.md) property. Make sure that the image isn’t larger than [`CPMaximumMessageItemImageSize`](cpmaximummessageitemimagesize.md).

CarPlay doesn’t support animated images. If you provide an animated image, CarPlay uses only the first image in the animation sequence.

## Parameters

- `trailingItem`: The item to show in the trailing region of the message list item. See   for the available options.
- `trailingImage`: The image to show in the trailing region of the message list item.

## See Also

- [let CPMaximumMessageItemImageSize: CGSize](cpmaximummessageitemimagesize.md)
  The maximum size of a message list item’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagelistitemtrailingconfiguration/init(trailingitem:trailingimage:))*