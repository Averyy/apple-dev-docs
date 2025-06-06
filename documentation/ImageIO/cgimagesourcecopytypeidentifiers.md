# CGImageSourceCopyTypeIdentifiers()

**Framework**: Image I/O  
**Kind**: func

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

#### Return Value

Returns an array of the uniform type identifiers that are supported for image sources.

#### Discussion

For a list of system-declared and third-party identifiers, see [`Uniform Type Identifiers`](https://developer.apple.com/documentation/UniformTypeIdentifiers).

## See Also

- [func CGImageSourceGetTypeID() -> CFTypeID](cgimagesourcegettypeid().md)
  Returns the unique type identifier of an image source opaque type.
- [func CGImageSourceGetType(CGImageSource) -> CFString?](cgimagesourcegettype(_:).md)
  Returns the uniform type identifier of the source container.
- [func CGImageSourceGetCount(CGImageSource) -> Int](cgimagesourcegetcount(_:).md)
  Returns the number of images (not including thumbnails) in the image source.
- [func CGImageSourceCopyProperties(CGImageSource, CFDictionary?) -> CFDictionary?](cgimagesourcecopyproperties(_:_:).md)
  Returns the properties of the image source.
- [func CGImageSourceCopyPropertiesAtIndex(CGImageSource, Int, CFDictionary?) -> CFDictionary?](cgimagesourcecopypropertiesatindex(_:_:_:).md)
  Returns the properties of the image at a specified location in an image source.
- [func CGImageSourceCopyAuxiliaryDataInfoAtIndex(CGImageSource, Int, CFString) -> CFDictionary?](cgimagesourcecopyauxiliarydatainfoatindex(_:_:_:).md)
  Returns auxiliary data, such as mattes and depth information, that accompany the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagesourcecopytypeidentifiers())*