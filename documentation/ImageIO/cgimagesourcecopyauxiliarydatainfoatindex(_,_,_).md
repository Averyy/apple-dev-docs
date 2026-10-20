# CGImageSourceCopyAuxiliaryDataInfoAtIndex(_:_:_:)

**Framework**: Image I/O  
**Kind**: func  
**Role**: Function

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

```c
extern CFDictionaryRefCGImageSourceCopyAuxiliaryDataInfoAtIndex(CGImageSourceRef isrc, size_t index, CFStringRef auxiliaryImageDataType);
```

#### Return Value

A dictionary that contains the auxiliary data, or `NULL` if an error occurs.

## Parameters

- `isrc`: The image source that contains the image data.
- `index`: The zero-based index into the images of the image source. If the index is invalid, this method returns `NULL`.
- `auxiliaryImageDataType`: The auxiliary data to retrieve. For a list of possible values, see [Auxiliary Image Data](./individual-image-properties.md#Auxiliary-Image-Data) and [Auxiliary Data Types](./individual-image-properties.md#Auxiliary-Data-Types).

## See Also

### Getting Information From an Image Source
- [func CGImageSourceGetTypeID() -> CFTypeID](./cgimagesourcegettypeid%28%29.md)
  Returns the unique type identifier of an image source opaque type.
- [func CGImageSourceGetType(CGImageSource) -> CFString?](./cgimagesourcegettype%28_%29.md)
  Returns the uniform type identifier of the source container.
- [func CGImageSourceCopyTypeIdentifiers() -> CFArray](./cgimagesourcecopytypeidentifiers%28%29.md)
  Returns an array of uniform type identifiers that are supported for image sources.
- [func CGImageSourceGetCount(CGImageSource) -> Int](./cgimagesourcegetcount%28_%29.md)
  Returns the number of images (not including thumbnails) in the image source.
- [func CGImageSourceCopyProperties(CGImageSource, CFDictionary?) -> CFDictionary?](./cgimagesourcecopyproperties%28_,_%29.md)
  Returns the properties of the image source.
- [func CGImageSourceCopyPropertiesAtIndex(CGImageSource, Int, CFDictionary?) -> CFDictionary?](./cgimagesourcecopypropertiesatindex%28_,_,_%29.md)
  Returns the properties of the image at a specified location in an image source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagesourcecopyauxiliarydatainfoatindex(_:_:_:))*