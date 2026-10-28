# CGImageSourceGetType(_:)

**Framework**: Image I/O  
**Kind**: func  
**Role**: Function

Returns the uniform type identifier of the source container.

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
func CGImageSourceGetType(_ isrc: CGImageSource) -> CFString?
```

```c
extern CFStringRefCGImageSourceGetType(CGImageSourceRef isrc);
```

## Return Value

The uniform type identifier of the image source container.

## Discussion

The uniform type identifier of the source container can be different from the type of the images in the container. For example, the `.icns` format supports embedded `JPEG2000`. The type of the source container is `"com.apple.icns"`, but type of the images is `JPEG2000`.

For a list of system-declared and third-party identifiers, see [Uniform Type Identifiers](../UniformTypeIdentifiers/UniformTypeIdentifiers.md).

## Parameters

- `isrc`: The image source that contains the image data.

## See Also

### Getting Information From an Image Source
- [func CGImageSourceGetTypeID() -> CFTypeID](./cgimagesourcegettypeid%28%29.md)
  Returns the unique type identifier of an image source opaque type.
- [func CGImageSourceCopyTypeIdentifiers() -> CFArray](./cgimagesourcecopytypeidentifiers%28%29.md)
  Returns an array of uniform type identifiers that are supported for image sources.
- [func CGImageSourceGetCount(CGImageSource) -> Int](./cgimagesourcegetcount%28_%29.md)
  Returns the number of images (not including thumbnails) in the image source.
- [func CGImageSourceCopyProperties(CGImageSource, CFDictionary?) -> CFDictionary?](./cgimagesourcecopyproperties%28_,_%29.md)
  Returns the properties of the image source.
- [func CGImageSourceCopyPropertiesAtIndex(CGImageSource, Int, CFDictionary?) -> CFDictionary?](./cgimagesourcecopypropertiesatindex%28_,_,_%29.md)
  Returns the properties of the image at a specified location in an image source.
- [func CGImageSourceCopyAuxiliaryDataInfoAtIndex(CGImageSource, Int, CFString) -> CFDictionary?](./cgimagesourcecopyauxiliarydatainfoatindex%28_,_,_%29.md)
  Returns auxiliary data, such as mattes and depth information, that accompany the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagesourcegettype(_:))*