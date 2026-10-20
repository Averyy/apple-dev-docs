# animatedImageNamed(_:duration:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates and returns an animated image.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func animatedImageNamed(_ name: String, duration: TimeInterval) -> UIImage?
```

```objc
+ (UIImage *) animatedImageNamed:(NSString *) name duration:(NSTimeInterval) duration;
```

#### Return Value

A new image object.

#### Discussion

This method loads a series of files by appending a series of numbers to the base file name provided in the `name` parameter. For example, if the `name` parameter had ‘image’ as its contents, this method would attempt to load images from files with the names ‘image0’, ‘image1’ and so on all the way up to ‘image1024’. All images included in the animated image should share the same size and scale.

## Parameters

- `name`: The full or partial path to the file (sans suffix).
- `duration`: The duration of the animation.

## See Also

### Creating animated images
- [class func animatedImage(with: [UIImage], duration: TimeInterval) -> UIImage?](./animatedimage%28with,duration%29.md)
  Creates and returns an animated image from an existing set of images.
- [class func animatedResizableImageNamed(String, capInsets: UIEdgeInsets, duration: TimeInterval) -> UIImage?](./animatedresizableimagenamed%28_,capinsets,duration%29.md)
  Creates and returns an animated image with end caps.
- [class func animatedResizableImageNamed(String, capInsets: UIEdgeInsets, resizingMode: UIImage.ResizingMode, duration: TimeInterval) -> UIImage?](./animatedresizableimagenamed%28_,capinsets,resizingmode,duration%29.md)
  Creates and returns an animated image with end caps and a specific resizing mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/animatedimagenamed(_:duration:))*