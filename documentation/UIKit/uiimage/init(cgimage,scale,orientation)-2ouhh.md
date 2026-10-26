# init(cgImage:scale:orientation:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns an image object with the specified scale and orientation factors.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(cgImage: CGImage, scale: CGFloat, orientation: UIImage.Orientation)
```

```objc
- (instancetype) initWithCGImage:(CGImageRef) cgImage scale:(CGFloat) scale orientation:(UIImageOrientation) orientation;
```

#### Return Value

An initialized `UIImage` object. In Objective-C, this method returns `nil` if the `ciImage` parameter is `nil`.

## Parameters

- `cgImage`: The Quartz image object.
- `scale`: The scale factor to assume when interpreting the image data. Applying a scale factor of 1.0 results in an image whose size matches the pixel-based dimensions of the image. Applying a different scale factor changes the size of the image as reported by the [`size`](./size.md) property.
- `orientation`: The orientation of the image data. You can use this parameter to specify any rotation factors applied to the image.

## See Also

### Creating and initializing image objects
- [init?(contentsOfFile: String)](./init%28contentsoffile%29.md)
  Initializes and returns the image object with the contents of the specified file.
- [init?(data: Data)](./init%28data%29.md)
  Initializes and returns the image object with the specified data.
- [init?(data: Data, scale: CGFloat)](./init%28data,scale%29.md)
  Initializes and returns the image object with the specified data and scale factor.
- [init(cgImage: CGImage)](./init%28cgimage%29-14qlb.md)
  Initializes and returns the image object with the specified Quartz image reference.
- [init(ciImage: CIImage)](./init%28ciimage%29-93vu1.md)
  Initializes and returns an image object with the specified Core Image object.
- [init(ciImage: CIImage, scale: CGFloat, orientation: UIImage.Orientation)](./init%28ciimage,scale,orientation%29-9gpyn.md)
  Initializes and returns an image object with the specified Core Image object and properties.
- [struct UIImageReader](../uiimagereader-swift.struct.md)
- [+ imageWithContentsOfFile:](./imagewithcontentsoffile_.md)
  Creates and returns an image object by loading the image data from the file at the specified path.
- [+ imageWithData:](./imagewithdata_.md)
  Creates and returns an image object that uses the specified image data.
- [+ imageWithData:scale:](./imagewithdata_scale_.md)
  Creates and returns an image object that uses the specified image data and scale factor.
- [+ imageWithCGImage:](./imagewithcgimage_.md)
  Creates and returns an image object representing the specified Quartz image.
- [+ imageWithCGImage:scale:orientation:](./imagewithcgimage_scale_orientation_.md)
  Creates and returns an image object with the specified scale and orientation factors.
- [+ imageWithCIImage:](./imagewithciimage_.md)
  Creates and returns an image object that contains a Core Image object.
- [+ imageWithCIImage:scale:orientation:](./imagewithciimage_scale_orientation_.md)
  Creates and returns an image object based on a Core Image object and the specified attributes.
- [UIImageReader](../uiimagereader-c.class.md)
- [UIImageReaderConfiguration](../uiimagereaderconfiguration.md)
  The properties that a reader uses to decode images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/init(cgimage:scale:orientation:)-2ouhh)*