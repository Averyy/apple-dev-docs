# animatedImage(with:duration:)

**Framework**: UIKit  
**Kind**: method

Creates and returns an animated image from an existing set of images.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func animatedImage(with images: [UIImage], duration: TimeInterval) -> UIImage?
```

#### Return Value

A new image object.

#### Discussion

All images included in the animated image should share the same size and scale.

## Parameters

- `images`: An array of   objects.
- `duration`: The duration of the animation.

## See Also

- [class func animatedImageNamed(String, duration: TimeInterval) -> UIImage?](uiimage/animatedimagenamed(_:duration:).md)
  Creates and returns an animated image.
- [class func animatedResizableImageNamed(String, capInsets: UIEdgeInsets, duration: TimeInterval) -> UIImage?](uiimage/animatedresizableimagenamed(_:capinsets:duration:).md)
  Creates and returns an animated image with end caps.
- [class func animatedResizableImageNamed(String, capInsets: UIEdgeInsets, resizingMode: UIImage.ResizingMode, duration: TimeInterval) -> UIImage?](uiimage/animatedresizableimagenamed(_:capinsets:resizingmode:duration:).md)
  Creates and returns an animated image with end caps and a specific resizing mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/animatedimage(with:duration:))*