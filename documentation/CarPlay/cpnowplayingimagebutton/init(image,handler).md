# init(image:handler:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a button with the specified image and handler.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
init(image: UIImage, handler: ((CPNowPlayingButton) -> Void)? = nil)
```

```objc
- (instancetype) initWithImage:(UIImage *) image handler:(void (^)(CPNowPlayingButton *)) handler;
```

## Return Value

An initialized image button.

## Discussion

When calculating the size of your image, multiply the dimensions in [`CPNowPlayingButtonMaximumImageSize`](../cpnowplayingbuttonmaximumimagesize.md) by the current display scale to get the image size in pixels. You can retrieve the current display scale from the vehicle’s trait collection, which you get from the [`carTraitCollection`](../cpinterfacecontroller/cartraitcollection.md) property of your interface controller.

## Parameters

- `image`: The image to display for the button. Specify an SF Symbol or an image with the dimensions in [`CPNowPlayingButtonMaximumImageSize`](../cpnowplayingbuttonmaximumimagesize.md). This method scales images to the expected dimensions as needed. If you specify an animated image, the system uses only the first image in the animation sequence.
- `handler`: The handler to run when someone interacts with the button. This closure takes the button as a parameter and returns no value.

## See Also

### Creating the button
- [let CPNowPlayingButtonMaximumImageSize: CGSize](../cpnowplayingbuttonmaximumimagesize.md)
  The dimensions for images in custom buttons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingimagebutton/init(image:handler:))*