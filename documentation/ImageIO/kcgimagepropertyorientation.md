# kCGImagePropertyOrientation

**Framework**: Image I/O  
**Kind**: var

The intended display orientation of the image.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCGImagePropertyOrientation: CFString
```

#### Discussion

The value of this property is a [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber). The value encodes the intended display orientation for the image according to the TIFF and EXIF specifications. See the [`CGImagePropertyOrientation`](cgimagepropertyorientation.md) type for possible values and their meanings.

## See Also

- [let kCGImagePropertyImageCount: CFString](kcgimagepropertyimagecount.md)
  The number of images in the file.
- [let kCGImagePropertyIsIndexed: CFString](kcgimagepropertyisindexed.md)
  A Boolean value that indicates whether the image contains indexed pixel samples.
- [let kCGImagePropertyImages: CFString](kcgimagepropertyimages.md)
  An array of dictionaries, each of which contains metadata for one of the images in the file.
- [let kCGImagePropertyThumbnailImages: CFString](kcgimagepropertythumbnailimages.md)
- [let kCGImagePropertyPrimaryImage: CFString](kcgimagepropertyprimaryimage.md)
  The index of the primary image in the file.
- [let kCGImagePropertyIsFloat: CFString](kcgimagepropertyisfloat.md)
  A Boolean value that indicates whether the image contains floating-point pixel samples.
- [Individual Image Properties](individual-image-properties.md)
  Properties that apply to an individual image in an image source.
- [enum CGImagePropertyOrientation](cgimagepropertyorientation.md)
  A value describing the intended display orientation for an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagepropertyorientation)*