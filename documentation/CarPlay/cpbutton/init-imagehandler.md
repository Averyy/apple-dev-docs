# init(image:handler:)

**Framework**: CarPlay  
**Kind**: init

Creates a button that displays an image and invokes a handler when the user taps it.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
init(image: UIImage, handler: ((CPButton) -> Void)? = nil)
```

#### Return Value

A new button that displays an image and invokes its handler when the user taps it.

#### Discussion

Provide an image that is display-ready. If necessary, provide light and dark variants using an asset catalog, or use an instance of [`UIImageAsset`](https://developer.apple.com/documentation/UIKit/UIImageAsset) and register an image for each interface style. To properly size your image, use the display scale of the vehicle’s primary screen, which you access from your interface controller’s [`carTraitCollection`](cpinterfacecontroller/cartraitcollection.md) property, and ensure it is no larger than [`CPButtonMaximumImageSize`](cpbuttonmaximumimagesize.md).

CarPlay doesn’t support animated images. If you provide an animated image, CarPlay uses only the first image in the animation sequence.

## Parameters

- `image`: The image that the button displays.
- `handler`: The closure that the button invokes when the user taps it.

## See Also

- [let CPButtonMaximumImageSize: CGSize](cpbuttonmaximumimagesize.md)
  The maximum size of a button’s image that CarPlay supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpbutton/init(image:handler:))*