# imageAsset

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The image asset (if any) for the image.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var imageAsset: UIImageAsset? { get }
```

```objc
@property (nonatomic, readonly, nullable) UIImageAsset * imageAsset;
```

#### Discussion

For images loaded from an image assets, this property contains an image asset object that you can use to fetch the other variants of the image. If you did not create the image object using an image asset, the value of this property is `nil`. This property is always `nil` for images created using a [`ciImage`](./ciimage.md) object.

## See Also

### Getting the image data
- [var cgImage: CGImage?](./cgimage.md)
  The underlying Quartz image data.
- [var ciImage: CIImage?](./ciimage.md)
  The underlying Core Image data.
- [var images: [UIImage]?](./images.md)
  The complete array of image objects that compose the animation of an animated object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/imageasset)*