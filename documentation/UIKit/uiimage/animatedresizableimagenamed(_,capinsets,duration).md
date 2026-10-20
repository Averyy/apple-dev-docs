# animatedResizableImageNamed(_:capInsets:duration:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates and returns an animated image with end caps.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func animatedResizableImageNamed(_ name: String, capInsets: UIEdgeInsets, duration: TimeInterval) -> UIImage?
```

```objc
+ (UIImage *) animatedResizableImageNamed:(NSString *) name capInsets:(UIEdgeInsets) capInsets duration:(NSTimeInterval) duration;
```

#### Return Value

A new image object.

#### Discussion

This method loads a series of files by appending a series of numbers to the base file name provided in the `name` parameter. For example, if the `name` parameter had ‘image’ as its contents, this method would attempt to load images from files with the names ‘image0’, ‘image1’ and so on all the way up to ‘image1024’. All images included in the animated image should share the same size and scale.

Each frame in the animation follows the rules for resizable images created by the [`resizableImage(withCapInsets:)`](./resizableimage%28withcapinsets%29.md) method.

## Parameters

- `name`: The full or partial path to the file (sans suffix).
- `capInsets`: The values to use for the cap insets.
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
- [class func animatedResizableImageNamed(String, capInsets: UIEdgeInsets, resizingMode: UIImage.ResizingMode, duration: TimeInterval) -> UIImage?](./animatedresizableimagenamed%28_,capinsets,resizingmode,duration%29.md)
  Creates and returns an animated image with end caps and a specific resizing mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/animatedresizableimagenamed(_:capinsets:duration:))*