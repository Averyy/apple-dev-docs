# CPNowPlayingButtonMaximumImageSize

**Framework**: CarPlay  
**Kind**: var  
**Role**: Global Variable

The dimensions for images in custom buttons.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+

## Declaration

```swift
let CPNowPlayingButtonMaximumImageSize: CGSize
```

```c
extern const CGSize CPNowPlayingButtonMaximumImageSize;
```

## Discussion

This constant specifies the expected dimensions for images you use with a [`CPNowPlayingImageButton`](./cpnowplayingimagebutton.md) object. The image dimensions are in points. To get the image dimensions in pixels, multiple the width and height values by the current display scale from the vehicle’s trait collection. You can get the current traits from the [`carTraitCollection`](./cpinterfacecontroller/cartraitcollection.md) property of your interface controller.

## See Also

### Creating the button
- [init(image: UIImage, handler: ((CPNowPlayingButton) -> Void)?)](./cpnowplayingimagebutton/init%28image,handler%29.md)
  Creates a button with the specified image and handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingbuttonmaximumimagesize)*