# CGImageSourceGetTypeID()

**Framework**: Image I/O  
**Kind**: func  
**Role**: Function

Returns the unique type identifier of an image source opaque type.

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
func CGImageSourceGetTypeID() -> CFTypeID
```

```c
extern CFTypeID CGImageSourceGetTypeID();
```

#### Return Value

Returns the Core Foundation type ID for an image source.

#### Discussion

A type identifier is an integer that identifies the opaque type to which a Core Foundation object belongs. You use type IDs in various contexts, such as when you are operating on heterogeneous collections. Note that a Core Foundation type ID is different from a uniform type identifier.

## See Also

### Getting Information From an Image Source
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
- [func CGImageSourceCopyAuxiliaryDataInfoAtIndex(CGImageSource, Int, CFString) -> CFDictionary?](./cgimagesourcecopyauxiliarydatainfoatindex%28_,_,_%29.md)
  Returns auxiliary data, such as mattes and depth information, that accompany the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagesourcegettypeid())*