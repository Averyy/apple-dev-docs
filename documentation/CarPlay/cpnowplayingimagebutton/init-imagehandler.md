# init(image:handler:)

**Framework**: CarPlay  
**Kind**: init

Creates a Now Playing button that displays a custom image and invokes a handler.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
init(image: UIImage, handler: ((CPNowPlayingButton) -> Void)? = nil)
```

#### Discussion

Provide an image that is display-ready. If necessary, provide light and dark variants using an asset catalog, or use an instance of [`UIImageAsset`](https://developer.apple.com/documentation/UIKit/UIImageAsset) and register an image for each interface style. To properly size your image, use the display scale of the vehicle’s primary screen—see your interface controller’s [`carTraitCollection`](cpinterfacecontroller/cartraitcollection.md) property—and make sure it is no larger than [`CPNowPlayingButtonMaximumImageSize`](cpnowplayingbuttonmaximumimagesize.md).

CarPlay doesn’t support animated images. If you provide an animated image, CarPlay uses only the first image in the animation sequence.

## Parameters

- `image`: An image to display on the button.
- `handler`: A closure that the button invokes when the user taps it.

## See Also

- [let CPNowPlayingButtonMaximumImageSize: CGSize](cpnowplayingbuttonmaximumimagesize.md)
  The maximum size CarPlay supports for a button’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingimagebutton/init(image:handler:))*