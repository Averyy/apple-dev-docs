# maximumImageSize(forAspectRatio:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Type Method

Calculates the maximum image size for a thumbnail image with the specified aspect ratio.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
class func maximumImageSize(forAspectRatio aspectRatio: CGFloat) -> CGSize
```

```objc
+ (CGSize) maximumImageSizeForAspectRatio:(CGFloat) aspectRatio;
```

## Return Value

The maximum size of the thumbnail image in points. To calculate the image dimensions in pixels, multiply the returned value by the scale factor from the current CarPlay traits, which you can get from your scene’s [`CPInterfaceController`](../cpinterfacecontroller.md) object.

## Discussion

Call this method to calculate the maximum size of the image you use for the main image of a [`CPThumbnailImage`](../cpthumbnailimage.md) object.

## Parameters

- `aspectRatio`: The width-to-height ratio of the image. Divide the width of the image by its height to get this value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpthumbnailimage/maximumimagesize(foraspectratio:))*