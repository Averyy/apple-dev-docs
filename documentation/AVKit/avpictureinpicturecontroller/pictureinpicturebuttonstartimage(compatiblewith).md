# pictureInPictureButtonStartImage(compatibleWith:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Type Method

Returns a system-default template image that’s compatible with a trait collection for the button that starts Picture in Picture in your app.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func pictureInPictureButtonStartImage(compatibleWith traitCollection: UITraitCollection?) -> UIImage
```

```objc
+ (UIImage *) pictureInPictureButtonStartImageCompatibleWithTraitCollection:(UITraitCollection *) traitCollection;
```

#### Return Value

A system-default template image.

## Parameters

- `traitCollection`: A trait collection that describes the image to retrieve. Pass `nil` to use traits that describe the main screen.

## See Also

### Retrieving Picture in Picture template images
- [class var pictureInPictureButtonStartImage: UIImage](./pictureinpicturebuttonstartimage.md)
  A system-default template image for the button that starts Picture in Picture in your app.
- [class var pictureInPictureButtonStopImage: UIImage](./pictureinpicturebuttonstopimage.md)
  A system-default template image for the button that stops Picture in Picture in your app.
- [class func pictureInPictureButtonStopImage(compatibleWith: UITraitCollection?) -> UIImage](./pictureinpicturebuttonstopimage%28compatiblewith%29.md)
  Returns a system-default template image that’s compatible with a trait collection for the button that stops Picture in Picture in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/pictureinpicturebuttonstartimage(compatiblewith:))*