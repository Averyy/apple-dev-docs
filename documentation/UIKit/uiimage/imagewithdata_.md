# imageWithData:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates and returns an image object that uses the specified image data.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (UIImage *) imageWithData:(NSData *) data;
```

#### Return Value

A new image object for the specified data, or `nil` if the method could not initialize the image from the specified data.

#### Discussion

This method does not cache the image object.

## Parameters

- `data`: The image data. This can be data from a file or data you create programmatically.

## See Also

### Creating and initializing image objects
- [+ imageWithContentsOfFile:](./imagewithcontentsoffile_.md)
  Creates and returns an image object by loading the image data from the file at the specified path.
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
- [init?(contentsOfFile: String)](./init%28contentsoffile%29.md)
  Initializes and returns the image object with the contents of the specified file.
- [init?(data: Data)](./init%28data%29.md)
  Initializes and returns the image object with the specified data.
- [init?(data: Data, scale: CGFloat)](./init%28data,scale%29.md)
  Initializes and returns the image object with the specified data and scale factor.
- [init(cgImage: CGImage)](./init%28cgimage%29-14qlb.md)
  Initializes and returns the image object with the specified Quartz image reference.
- [init(cgImage: CGImage, scale: CGFloat, orientation: UIImage.Orientation)](./init%28cgimage,scale,orientation%29-2ouhh.md)
  Initializes and returns an image object with the specified scale and orientation factors.
- [init(ciImage: CIImage)](./init%28ciimage%29-93vu1.md)
  Initializes and returns an image object with the specified Core Image object.
- [init(ciImage: CIImage, scale: CGFloat, orientation: UIImage.Orientation)](./init%28ciimage,scale,orientation%29-9gpyn.md)
  Initializes and returns an image object with the specified Core Image object and properties.
- [UIImageReader](../uiimagereader-c.class.md)
- [UIImageReaderConfiguration](../uiimagereaderconfiguration.md)
  The properties that a reader uses to decode images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/imagewithdata:)*