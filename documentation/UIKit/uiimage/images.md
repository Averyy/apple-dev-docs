# images

**Framework**: UIKit  
**Kind**: property

The complete array of image objects that compose the animation of an animated object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var images: [UIImage]? { get }
```

#### Discussion

For a non-animated image, the value of this property is `nil`.

## See Also

- [var cgImage: CGImage?](uiimage/cgimage.md)
  The underlying Quartz image data.
- [var ciImage: CIImage?](uiimage/ciimage.md)
  The underlying Core Image data.
- [var imageAsset: UIImageAsset?](uiimage/imageasset.md)
  The image asset (if any) for the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/images)*