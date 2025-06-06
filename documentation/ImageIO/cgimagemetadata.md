# CGImageMetadata

**Framework**: Image I/O  
**Kind**: class

An immutable object that contains the XMP metadata associated with an image.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CGImageMetadata
```

#### Overview

A [`CGImageMetadata`](cgimagemetadata.md) object stores the metadata associated with an image. Create this object from your image’s associated XMP data, and use it to fetch individual metadata tags. You can search for specific tags, or enumerate all of the tags present for the image.

## Topics

### Creating an Image Metadata Type
- [func CGImageMetadataCreateFromXMPData(CFData) -> CGImageMetadata?](cgimagemetadatacreatefromxmpdata(_:).md)
  Creates a collection of metadata tags from the specified XMP data.
### Getting the Metadata Tags
- [func CGImageMetadataCopyTagWithPath(CGImageMetadata, CGImageMetadataTag?, CFString) -> CGImageMetadataTag?](cgimagemetadatacopytagwithpath(_:_:_:).md)
  Searches for a specific metadata tag within a metadata collection.
- [func CGImageMetadataCopyTags(CGImageMetadata) -> CFArray?](cgimagemetadatacopytags(_:).md)
  Returns an array of root-level metadata tags from the specified metadata object.
- [func CGImageMetadataCopyTagMatchingImageProperty(CGImageMetadata, CFString, CFString) -> CGImageMetadataTag?](cgimagemetadatacopytagmatchingimageproperty(_:_:_:).md)
  Searches for the specified image property and, if found, returns the corresponding tag object.
- [func CGImageMetadataCopyStringValueWithPath(CGImageMetadata, CGImageMetadataTag?, CFString) -> CFString?](cgimagemetadatacopystringvaluewithpath(_:_:_:).md)
  Searches the metadata for the specified tag, and returns its string value if it exists.
### Enumerating the Metadata Tags
- [func CGImageMetadataEnumerateTagsUsingBlock(CGImageMetadata, CFString?, CFDictionary?, CGImageMetadataTagBlock)](cgimagemetadataenumeratetagsusingblock(_:_:_:_:).md)
  Enumerates the tags of a metadata object and executes the specified block on each tag.
- [typealias CGImageMetadataTagBlock](cgimagemetadatatagblock.md)
  The block to execute when enumerating the tags of a metadata object.
- [let kCGImageMetadataEnumerateRecursively: CFString](kcgimagemetadataenumeraterecursively.md)
  An option to enumerate recursively through a set of metadata tags.
### Generating XMP Data
- [func CGImageMetadataCreateXMPData(CGImageMetadata, CFDictionary?) -> CFData?](cgimagemetadatacreatexmpdata(_:_:).md)
  Returns a data object that contains the metadata object’s contents serialized into the XMP format.
### Getting the Core Foundation Type
- [func CGImageMetadataGetTypeID() -> CFTypeID](cgimagemetadatagettypeid().md)
  Returns the type identifier for metadata objects.

## Relationships

### Inherited By
- [CGMutableImageMetadata](cgmutableimagemetadata.md)
### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [class CGMutableImageMetadata](cgmutableimagemetadata.md)
  An opaque type for adding or modifying image metadata.
- [class CGImageMetadataTag](cgimagemetadatatag.md)
  An immutable type that contains information about a single piece of image metadata.
- [XMP Namespaces and Prefixes](xmp-namespaces-and-prefixes.md)
  Discover the public namespaces and prefixes that exist in XMP metadata tags.
- [let kCFErrorDomainCGImageMetadata: CFString](kcferrordomaincgimagemetadata.md)
  The domain for metadata-related errors that originate in the Image I/O framework.
- [enum CGImageMetadataErrors](cgimagemetadataerrors.md)
  Constants for errors that occur when getting or setting metadata information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagemetadata)*