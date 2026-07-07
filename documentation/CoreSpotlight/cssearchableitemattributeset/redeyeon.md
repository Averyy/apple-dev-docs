# redEyeOn

**Framework**: Core Spotlight  
**Kind**: property

A value that indicates if the camera used red-eye reduction when capturing the image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var redEyeOn: NSNumber? { get set }
```

#### Discussion

When the value of this property is 0, no red-eye reduction was used; when the value is 1, red-eye reduction was used.

## See Also

- [var isoSpeed: NSNumber?](cssearchableitemattributeset/isospeed.md)
  The ISO speed setting at the time the camera captured the image.
- [var acquisitionMake: String?](cssearchableitemattributeset/acquisitionmake.md)
  The manufacturer of the device that captured the image.
- [var acquisitionModel: String?](cssearchableitemattributeset/acquisitionmodel.md)
  The model of the device that captured the image.
- [var aperture: NSNumber?](cssearchableitemattributeset/aperture.md)
  The size of the lens aperture at the time the camera captured the image, as a log-scale APEX value.
- [var bitsPerSample: NSNumber?](cssearchableitemattributeset/bitspersample.md)
  The number of bits per sample.
- [var cameraOwner: String?](cssearchableitemattributeset/cameraowner.md)
  The owner of the camera that captured the image.
- [var colorSpace: String?](cssearchableitemattributeset/colorspace.md)
  The color space model the image uses, such as RGB, CMYK, YUV, or YCbCr.
- [var flashOn: NSNumber?](cssearchableitemattributeset/flashon.md)
  A value that indicates if the camera used a flash to capture the image.
- [var focalLength: NSNumber?](cssearchableitemattributeset/focallength.md)
  The actual focal length of the lens, in millimeters.
- [var focalLength35mm: NSNumber?](cssearchableitemattributeset/focallength35mm.md)
  A value that indicates if the focal length is 35mm.
- [var layerNames: [String]?](cssearchableitemattributeset/layernames.md)
  An array that contains the names of the various layers in the file.
- [var lensModel: String?](cssearchableitemattributeset/lensmodel.md)
  The model of the lens that captured the image.
- [var orientation: NSNumber?](cssearchableitemattributeset/orientation.md)
  The orientation of the data.
- [var pixelCount: NSNumber?](cssearchableitemattributeset/pixelcount.md)
  The total number of pixels in the image.
- [var pixelHeight: NSNumber?](cssearchableitemattributeset/pixelheight.md)
  The height of the item, such as image or video frame height, in pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/redeyeon)*