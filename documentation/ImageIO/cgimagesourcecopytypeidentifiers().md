# CGImageSourceCopyTypeIdentifiers()

**Framework**: Image I/O  
**Kind**: func  
**Role**: Function

Returns an array of uniform type identifiers that are supported for image sources.

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
func CGImageSourceCopyTypeIdentifiers() -> CFArray
```

```c
extern CFArrayRefCGImageSourceCopyTypeIdentifiers();
```

## Return Value

Returns an array of the uniform type identifiers that are supported for image sources.

## Discussion

For a list of system-declared and third-party identifiers, see [Uniform Type Identifiers](../UniformTypeIdentifiers/UniformTypeIdentifiers.md).

## See Also

### Getting Information From an Image Source
- [func CGImageSourceGetTypeID() -> CFTypeID](./cgimagesourcegettypeid%28%29.md)
  Returns the unique type identifier of an image source opaque type.
- [func CGImageSourceGetType(CGImageSource) -> CFString?](./cgimagesourcegettype%28_%29.md)
  Returns the uniform type identifier of the source container.
- [func CGImageSourceGetCount(CGImageSource) -> Int](./cgimagesourcegetcount%28_%29.md)
  Returns the number of images (not including thumbnails) in the image source.
- [func CGImageSourceCopyProperties(CGImageSource, CFDictionary?) -> CFDictionary?](./cgimagesourcecopyproperties%28_,_%29.md)
  Returns the properties of the image source.
- [func CGImageSourceCopyPropertiesAtIndex(CGImageSource, Int, CFDictionary?) -> CFDictionary?](./cgimagesourcecopypropertiesatindex%28_,_,_%29.md)
  Returns the properties of the image at a specified location in an image source.
- [func CGImageSourceCopyAuxiliaryDataInfoAtIndex(CGImageSource, Int, CFString) -> CFDictionary?](./cgimagesourcecopyauxiliarydatainfoatindex%28_,_,_%29.md)
  Returns auxiliary data, such as mattes and depth information, that accompany the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagesourcecopytypeidentifiers())*