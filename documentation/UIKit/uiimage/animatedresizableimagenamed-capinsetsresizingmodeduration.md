# animatedResizableImageNamed(_:capInsets:resizingMode:duration:)

**Framework**: UIKit  
**Kind**: method

Creates and returns an animated image with end caps and a specific resizing mode.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func animatedResizableImageNamed(_ name: String, capInsets: UIEdgeInsets, resizingMode: UIImage.ResizingMode, duration: TimeInterval) -> UIImage?
```

#### Return Value

A new animated image object with the specified cap insets and resizing mode.

#### Discussion

This method is exactly the same as its counterpart [`animatedResizableImageNamed(_:capInsets:duration:)`](uiimage/animatedresizableimagenamed(_:capinsets:duration:).md) except that the resizing mode of the new image object can be explicitly declared. Since the resizing mode of an image is [`UIImage.ResizingMode.tile`](uiimage/resizingmode-swift.enum/tile.md) by default, this method should only be used in place of its counterpart to create an animated image that needs to be resized with the [`UIImage.ResizingMode.stretch`](uiimage/resizingmode-swift.enum/stretch.md) resizing mode.

## Parameters

- `name`: The full or partial path to the file (sans suffix).
- `capInsets`: The values to use for the cap insets.
- `resizingMode`: The mode with which the interior of the image is resized.
- `duration`: The duration of the animation.

## See Also

- [func resizableImage(withCapInsets: UIEdgeInsets) -> UIImage](uiimage/resizableimage(withcapinsets:).md)
  Returns a new version of the image with the specified cap insets.
- [func resizableImage(withCapInsets: UIEdgeInsets, resizingMode: UIImage.ResizingMode) -> UIImage](uiimage/resizableimage(withcapinsets:resizingmode:).md)
  Returns a new version of the image with the specified cap insets and options.
- [class func animatedImageNamed(String, duration: TimeInterval) -> UIImage?](uiimage/animatedimagenamed(_:duration:).md)
  Creates and returns an animated image.
- [class func animatedImage(with: [UIImage], duration: TimeInterval) -> UIImage?](uiimage/animatedimage(with:duration:).md)
  Creates and returns an animated image from an existing set of images.
- [class func animatedResizableImageNamed(String, capInsets: UIEdgeInsets, duration: TimeInterval) -> UIImage?](uiimage/animatedresizableimagenamed(_:capinsets:duration:).md)
  Creates and returns an animated image with end caps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/animatedresizableimagenamed(_:capinsets:resizingmode:duration:))*