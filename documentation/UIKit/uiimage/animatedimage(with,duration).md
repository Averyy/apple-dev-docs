# animatedImage(with:duration:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates and returns an animated image from an existing set of images.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func animatedImage(with images: [UIImage], duration: TimeInterval) -> UIImage?
```

```objc
+ (UIImage *) animatedImageWithImages:(NSArray<UIImage *> *) images duration:(NSTimeInterval) duration;
```

## Return Value

A new image object.

## Discussion

All images included in the animated image should share the same size and scale.

## Parameters

- `images`: An array of [`UIImage`](../uiimage.md) objects.
- `duration`: The duration of the animation.

## See Also

### Creating animated images
- [class func animatedImageNamed(String, duration: TimeInterval) -> UIImage?](./animatedimagenamed%28_,duration%29.md)
  Creates and returns an animated image.
- [class func animatedResizableImageNamed(String, capInsets: UIEdgeInsets, duration: TimeInterval) -> UIImage?](./animatedresizableimagenamed%28_,capinsets,duration%29.md)
  Creates and returns an animated image with end caps.
- [class func animatedResizableImageNamed(String, capInsets: UIEdgeInsets, resizingMode: UIImage.ResizingMode, duration: TimeInterval) -> UIImage?](./animatedresizableimagenamed%28_,capinsets,resizingmode,duration%29.md)
  Creates and returns an animated image with end caps and a specific resizing mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/animatedimage(with:duration:))*