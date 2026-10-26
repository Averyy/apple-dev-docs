# UIImageReaderConfiguration

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

The properties that a reader uses to decode images.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
@interface UIImageReaderConfiguration : NSObject
```

## Topics

### Configuration properties
- [prefersHighDynamicRange](./uiimagereaderconfiguration/prefershighdynamicrange.md)
  A Boolean value that indicates whether the image reader should decode the image as HDR when the type is capable of decoding in either SDR or HDR.
- [preferredThumbnailSize](./uiimagereaderconfiguration/preferredthumbnailsize.md)
  The thumbnail size in pixels that the image reader makes the image.
- [preparesImagesForDisplay](./uiimagereaderconfiguration/preparesimagesfordisplay.md)
  A Boolean value that indicates whether the image reader prepares the image for display.
- [pixelsPerInch](./uiimagereaderconfiguration/pixelsperinch.md)
  The integral scale that the image reader applies to the image.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)

## See Also

### Creating and initializing image objects
- [+ imageWithContentsOfFile:](./uiimage/imagewithcontentsoffile_.md)
  Creates and returns an image object by loading the image data from the file at the specified path.
- [+ imageWithData:](./uiimage/imagewithdata_.md)
  Creates and returns an image object that uses the specified image data.
- [+ imageWithData:scale:](./uiimage/imagewithdata_scale_.md)
  Creates and returns an image object that uses the specified image data and scale factor.
- [+ imageWithCGImage:](./uiimage/imagewithcgimage_.md)
  Creates and returns an image object representing the specified Quartz image.
- [+ imageWithCGImage:scale:orientation:](./uiimage/imagewithcgimage_scale_orientation_.md)
  Creates and returns an image object with the specified scale and orientation factors.
- [+ imageWithCIImage:](./uiimage/imagewithciimage_.md)
  Creates and returns an image object that contains a Core Image object.
- [+ imageWithCIImage:scale:orientation:](./uiimage/imagewithciimage_scale_orientation_.md)
  Creates and returns an image object based on a Core Image object and the specified attributes.
- [init?(contentsOfFile: String)](./uiimage/init%28contentsoffile%29.md)
  Initializes and returns the image object with the contents of the specified file.
- [init?(data: Data)](./uiimage/init%28data%29.md)
  Initializes and returns the image object with the specified data.
- [init?(data: Data, scale: CGFloat)](./uiimage/init%28data,scale%29.md)
  Initializes and returns the image object with the specified data and scale factor.
- [init(cgImage: CGImage)](./uiimage/init%28cgimage%29-14qlb.md)
  Initializes and returns the image object with the specified Quartz image reference.
- [init(cgImage: CGImage, scale: CGFloat, orientation: UIImage.Orientation)](./uiimage/init%28cgimage,scale,orientation%29-2ouhh.md)
  Initializes and returns an image object with the specified scale and orientation factors.
- [init(ciImage: CIImage)](./uiimage/init%28ciimage%29-93vu1.md)
  Initializes and returns an image object with the specified Core Image object.
- [init(ciImage: CIImage, scale: CGFloat, orientation: UIImage.Orientation)](./uiimage/init%28ciimage,scale,orientation%29-9gpyn.md)
  Initializes and returns an image object with the specified Core Image object and properties.
- [UIImageReader](./uiimagereader-c.class.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagereaderconfiguration)*