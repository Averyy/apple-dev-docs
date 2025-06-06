# CGImageSourceCopyAuxiliaryDataInfoAtIndex(_:_:_:)

**Framework**: Image I/O  
**Kind**: func

Returns auxiliary data, such as mattes and depth information, that accompany the image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func CGImageSourceCopyAuxiliaryDataInfoAtIndex(_ isrc: CGImageSource, _ index: Int, _ auxiliaryImageDataType: CFString) -> CFDictionary?
```

#### Return Value

A dictionary that contains the auxiliary data, or `NULL` if an error occurs.

## Parameters

- `isrc`: The image source that contains the image data.
- `index`: The zero-based index into the images of the image source. If the index is invalid, this method returns  .
- `auxiliaryImageDataType`: The auxiliary data to retrieve. For a list of possible values, see   and  .

## See Also

- [func CGImageSourceGetTypeID() -> CFTypeID](cgimagesourcegettypeid().md)
  Returns the unique type identifier of an image source opaque type.
- [func CGImageSourceGetType(CGImageSource) -> CFString?](cgimagesourcegettype(_:).md)
  Returns the uniform type identifier of the source container.
- [func CGImageSourceCopyTypeIdentifiers() -> CFArray](cgimagesourcecopytypeidentifiers().md)
  Returns an array of uniform type identifiers that are supported for image sources.
- [func CGImageSourceGetCount(CGImageSource) -> Int](cgimagesourcegetcount(_:).md)
  Returns the number of images (not including thumbnails) in the image source.
- [func CGImageSourceCopyProperties(CGImageSource, CFDictionary?) -> CFDictionary?](cgimagesourcecopyproperties(_:_:).md)
  Returns the properties of the image source.
- [func CGImageSourceCopyPropertiesAtIndex(CGImageSource, Int, CFDictionary?) -> CFDictionary?](cgimagesourcecopypropertiesatindex(_:_:_:).md)
  Returns the properties of the image at a specified location in an image source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagesourcecopyauxiliarydatainfoatindex(_:_:_:))*