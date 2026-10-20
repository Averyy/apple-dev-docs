# ciImage

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The underlying Core Image data.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var ciImage: CIImage? { get }
```

```objc
@property (nonatomic, readonly, nullable) CIImage * CIImage;
```

#### Discussion

If the `UIImage` object was initialized using a [`CGImage`](../../CoreGraphics/cgimage.md), the value of the property is `nil`.

## See Also

### Getting the image data
- [var cgImage: CGImage?](./cgimage.md)
  The underlying Quartz image data.
- [var images: [UIImage]?](./images.md)
  The complete array of image objects that compose the animation of an animated object.
- [var imageAsset: UIImageAsset?](./imageasset.md)
  The image asset (if any) for the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/ciimage)*