# ciImage

**Framework**: UIKit  
**Kind**: property

The underlying Core Image data.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var ciImage: CIImage? { get }
```

#### Discussion

If the `UIImage` object was initialized using a [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage), the value of the property is `nil`.

## See Also

- [var cgImage: CGImage?](uiimage/cgimage.md)
  The underlying Quartz image data.
- [var images: [UIImage]?](uiimage/images.md)
  The complete array of image objects that compose the animation of an animated object.
- [var imageAsset: UIImageAsset?](uiimage/imageasset.md)
  The image asset (if any) for the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/ciimage)*