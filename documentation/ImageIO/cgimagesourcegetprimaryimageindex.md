# CGImageSourceGetPrimaryImageIndex(_:)

**Framework**: Image I/O  
**Kind**: func

Returns the index of the primary image for an High Efficiency Image File Format (HEIF) image.

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
func CGImageSourceGetPrimaryImageIndex(_ isrc: CGImageSource) -> Int
```

#### Return Value

The index of the primary image, or `0` for image formats other than the HEIF format.

## Parameters

- `isrc`: The image source that contains the image data.

## See Also

- [func CGImageSourceCreateImageAtIndex(CGImageSource, Int, CFDictionary?) -> CGImage?](cgimagesourcecreateimageatindex(_:_:_:).md)
  Creates an image object from the data at the specified index in an image source.
- [func CGImageSourceCreateThumbnailAtIndex(CGImageSource, Int, CFDictionary?) -> CGImage?](cgimagesourcecreatethumbnailatindex(_:_:_:).md)
  Creates a thumbnail version of the image at the specified index in an image source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagesourcegetprimaryimageindex(_:))*