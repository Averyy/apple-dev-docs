# images

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The complete array of image objects that compose the animation of an animated object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var images: [UIImage]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSArray<UIImage *> * images;
```

## Discussion

For a non-animated image, the value of this property is `nil`.

## See Also

### Getting the image data
- [var cgImage: CGImage?](./cgimage.md)
  The underlying Quartz image data.
- [var ciImage: CIImage?](./ciimage.md)
  The underlying Core Image data.
- [var imageAsset: UIImageAsset?](./imageasset.md)
  The image asset (if any) for the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/images)*