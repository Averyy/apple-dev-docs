# animatedResizableImageNamed(_:capInsets:resizingMode:duration:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates and returns an animated image with end caps and a specific resizing mode.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func animatedResizableImageNamed(_ name: String, capInsets: UIEdgeInsets, resizingMode: UIImage.ResizingMode, duration: TimeInterval) -> UIImage?
```

```objc
+ (UIImage *) animatedResizableImageNamed:(NSString *) name capInsets:(UIEdgeInsets) capInsets resizingMode:(UIImageResizingMode) resizingMode duration:(NSTimeInterval) duration;
```

#### Return Value

A new animated image object with the specified cap insets and resizing mode.

#### Discussion

This method is exactly the same as its counterpart [`animatedResizableImageNamed(_:capInsets:duration:)`](./animatedresizableimagenamed%28_,capinsets,duration%29.md) except that the resizing mode of the new image object can be explicitly declared. Since the resizing mode of an image is [`UIImage.ResizingMode.tile`](./resizingmode-swift.enum/tile.md) by default, this method should only be used in place of its counterpart to create an animated image that needs to be resized with the [`UIImage.ResizingMode.stretch`](./resizingmode-swift.enum/stretch.md) resizing mode.

## Parameters

- `name`: The full or partial path to the file (sans suffix).
- `capInsets`: The values to use for the cap insets.
- `resizingMode`: The mode with which the interior of the image is resized.
- `duration`: The duration of the animation.

## See Also

### Related Documentation
- [func resizableImage(withCapInsets: UIEdgeInsets) -> UIImage](./resizableimage%28withcapinsets%29.md)
  Returns a new version of the image with the specified cap insets.
- [func resizableImage(withCapInsets: UIEdgeInsets, resizingMode: UIImage.ResizingMode) -> UIImage](./resizableimage%28withcapinsets,resizingmode%29.md)
  Returns a new version of the image with the specified cap insets and options.
### Creating animated images
- [class func animatedImageNamed(String, duration: TimeInterval) -> UIImage?](./animatedimagenamed%28_,duration%29.md)
  Creates and returns an animated image.
- [class func animatedImage(with: [UIImage], duration: TimeInterval) -> UIImage?](./animatedimage%28with,duration%29.md)
  Creates and returns an animated image from an existing set of images.
- [class func animatedResizableImageNamed(String, capInsets: UIEdgeInsets, duration: TimeInterval) -> UIImage?](./animatedresizableimagenamed%28_,capinsets,duration%29.md)
  Creates and returns an animated image with end caps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/animatedresizableimagenamed(_:capinsets:resizingmode:duration:))*