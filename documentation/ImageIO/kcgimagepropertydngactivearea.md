# kCGImagePropertyDNGActiveArea

**Framework**: Image I/O  
**Kind**: var

The rectangle that defines the non-masked pixels of the sensor.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
let kCGImagePropertyDNGActiveArea: CFString
```

## See Also

- [let kCGImagePropertyDNGMaskedAreas: CFString](kcgimagepropertydngmaskedareas.md)
  A list of non-overlapping rectangles that contain fully masked pixels in the image.
- [let kCGImagePropertyDNGDefaultCropOrigin: CFString](kcgimagepropertydngdefaultcroporigin.md)
  The origin of the final image area, relative to the top-left corner of the active area rectangle.
- [let kCGImagePropertyDNGDefaultCropSize: CFString](kcgimagepropertydngdefaultcropsize.md)
  The size of the final image area, in raw image coordinates.
- [let kCGImagePropertyDNGDefaultUserCrop: CFString](kcgimagepropertydngdefaultusercrop.md)
  A default user-crop rectangle in relative coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagepropertydngactivearea)*