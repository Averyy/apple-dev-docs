# lensModel

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

The model of the lens that captured the image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var lensModel: String? { get set }
```

```objc
@property (copy, nullable) NSString * lensModel;
```

## See Also

### Describing images
- [var isoSpeed: NSNumber?](./isospeed.md)
  The ISO speed setting at the time the camera captured the image.
- [var acquisitionMake: String?](./acquisitionmake.md)
  The manufacturer of the device that captured the image.
- [var acquisitionModel: String?](./acquisitionmodel.md)
  The model of the device that captured the image.
- [var aperture: NSNumber?](./aperture.md)
  The size of the lens aperture at the time the camera captured the image, as a log-scale APEX value.
- [var bitsPerSample: NSNumber?](./bitspersample.md)
  The number of bits per sample.
- [var cameraOwner: String?](./cameraowner.md)
  The owner of the camera that captured the image.
- [var colorSpace: String?](./colorspace.md)
  The color space model the image uses, such as RGB, CMYK, YUV, or YCbCr.
- [var flashOn: NSNumber?](./flashon.md)
  A value that indicates if the camera used a flash to capture the image.
- [var focalLength: NSNumber?](./focallength.md)
  The actual focal length of the lens, in millimeters.
- [var focalLength35mm: NSNumber?](./focallength35mm.md)
  A value that indicates if the focal length is 35mm.
- [var layerNames: [String]?](./layernames.md)
  An array that contains the names of the various layers in the file.
- [var orientation: NSNumber?](./orientation.md)
  The orientation of the data.
- [var pixelCount: NSNumber?](./pixelcount.md)
  The total number of pixels in the image.
- [var pixelHeight: NSNumber?](./pixelheight.md)
  The height of the item, such as image or video frame height, in pixels.
- [var pixelWidth: NSNumber?](./pixelwidth.md)
  The width of the item, such as image or video frame width, in pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/lensmodel)*