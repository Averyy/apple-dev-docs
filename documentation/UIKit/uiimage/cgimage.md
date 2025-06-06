# cgImage

**Framework**: UIKit  
**Kind**: property

The underlying Quartz image data.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var cgImage: CGImage? { get }
```

#### Discussion

If the image data has been purged because of memory constraints, invoking this method forces that data to be loaded back into memory. Reloading the image data may incur a performance penalty.

If the `UIImage` object was initialized using a `CIImage` object, the value of the property is `NULL`.

## See Also

- [var ciImage: CIImage?](uiimage/ciimage.md)
  The underlying Core Image data.
- [var images: [UIImage]?](uiimage/images.md)
  The complete array of image objects that compose the animation of an animated object.
- [var imageAsset: UIImageAsset?](uiimage/imageasset.md)
  The image asset (if any) for the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/cgimage)*