# CGImageSourceGetCount(_:)

**Framework**: Image I/O  
**Kind**: func  
**Role**: Function

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

```c
extern size_t CGImageSourceGetCount(CGImageSourceRef isrc);
```

#### Return Value

The number of images. If the image source is a multilayered Photoshop (PSD) file, the function returns `1`.

#### Discussion

This function does not extract the layers of a PSD file.

## Parameters

- `isrc`: The image source that contains the image data.

## See Also

### Getting Information From an Image Source
- [func CGImageSourceGetTypeID() -> CFTypeID](./cgimagesourcegettypeid%28%29.md)
  Returns the unique type identifier of an image source opaque type.
- [func CGImageSourceGetType(CGImageSource) -> CFString?](./cgimagesourcegettype%28_%29.md)
  Returns the uniform type identifier of the source container.
- [func CGImageSourceCopyTypeIdentifiers() -> CFArray](./cgimagesourcecopytypeidentifiers%28%29.md)
  Returns an array of uniform type identifiers that are supported for image sources.
- [func CGImageSourceCopyProperties(CGImageSource, CFDictionary?) -> CFDictionary?](./cgimagesourcecopyproperties%28_,_%29.md)
  Returns the properties of the image source.
- [func CGImageSourceCopyPropertiesAtIndex(CGImageSource, Int, CFDictionary?) -> CFDictionary?](./cgimagesourcecopypropertiesatindex%28_,_,_%29.md)
  Returns the properties of the image at a specified location in an image source.
- [func CGImageSourceCopyAuxiliaryDataInfoAtIndex(CGImageSource, Int, CFString) -> CFDictionary?](./cgimagesourcecopyauxiliarydatainfoatindex%28_,_,_%29.md)
  Returns auxiliary data, such as mattes and depth information, that accompany the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagesourcegetcount(_:))*