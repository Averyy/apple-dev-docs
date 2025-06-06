# CGImageSourceGetCount(_:)

**Framework**: Image I/O  
**Kind**: func

Returns the number of images (not including thumbnails) in the image source.

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
func CGImageSourceGetCount(_ isrc: CGImageSource) -> Int
```

#### Return Value

The number of images. If the image source is a multilayered Photoshop (PSD) file, the function returns `1`.

#### Discussion

This function does not extract the layers of a PSD file.

## Parameters

- `isrc`: The image source that contains the image data.

## See Also

- [func CGImageSourceGetTypeID() -> CFTypeID](cgimagesourcegettypeid().md)
  Returns the unique type identifier of an image source opaque type.
- [func CGImageSourceGetType(CGImageSource) -> CFString?](cgimagesourcegettype(_:).md)
  Returns the uniform type identifier of the source container.
- [func CGImageSourceCopyTypeIdentifiers() -> CFArray](cgimagesourcecopytypeidentifiers().md)
  Returns an array of uniform type identifiers that are supported for image sources.
- [func CGImageSourceCopyProperties(CGImageSource, CFDictionary?) -> CFDictionary?](cgimagesourcecopyproperties(_:_:).md)
  Returns the properties of the image source.
- [func CGImageSourceCopyPropertiesAtIndex(CGImageSource, Int, CFDictionary?) -> CFDictionary?](cgimagesourcecopypropertiesatindex(_:_:_:).md)
  Returns the properties of the image at a specified location in an image source.
- [func CGImageSourceCopyAuxiliaryDataInfoAtIndex(CGImageSource, Int, CFString) -> CFDictionary?](cgimagesourcecopyauxiliarydatainfoatindex(_:_:_:).md)
  Returns auxiliary data, such as mattes and depth information, that accompany the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagesourcegetcount(_:))*