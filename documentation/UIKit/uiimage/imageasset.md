# imageAsset

**Framework**: UIKit  
**Kind**: property

The image asset (if any) for the image.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var imageAsset: UIImageAsset? { get }
```

#### Discussion

For images loaded from an image assets, this property contains an image asset object that you can use to fetch the other variants of the image. If you did not create the image object using an image asset, the value of this property is `nil`. This property is always `nil` for images created using a [`ciImage`](uiimage/ciimage.md) object.

## See Also

- [var cgImage: CGImage?](uiimage/cgimage.md)
  The underlying Quartz image data.
- [var ciImage: CIImage?](uiimage/ciimage.md)
  The underlying Core Image data.
- [var images: [UIImage]?](uiimage/images.md)
  The complete array of image objects that compose the animation of an animated object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/imageasset)*