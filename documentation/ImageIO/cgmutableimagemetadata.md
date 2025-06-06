# CGMutableImageMetadata

**Framework**: Image I/O  
**Kind**: class

An opaque type for adding or modifying image metadata.

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
class CGMutableImageMetadata
```

#### Discussion

Create a [`CGMutableImageMetadata`](cgmutableimagemetadata.md) opaque type when you want to modify the metadata in an image. You may pass this type to any functions that take a [`CGImageMetadata`](cgimagemetadata.md) type as a parameter. This object stores the tag information as XMP data, which you can write back to the image.

When you access or modify EXIF or IPTC properties, the metadata functions automatically bridge those properties to appropriate XMP properties. This bridging behavior fills in any fields that are present only in the XMP data. For example, it fills in the namespace, prefix, and XMP type information in the corresponding [`CGImageMetadataTag`](cgimagemetadatatag.md) object.

## Topics

### Creating a Mutable Metadata Type
- [func CGImageMetadataCreateMutable() -> CGMutableImageMetadata](cgimagemetadatacreatemutable().md)
  Creates an empty, mutable image metdata opaque type.
- [func CGImageMetadataCreateMutableCopy(CGImageMetadata) -> CGMutableImageMetadata?](cgimagemetadatacreatemutablecopy(_:).md)
  Creates a deep, mutable copy of the specified metadata information.
### Setting the Values of Tags
- [func CGImageMetadataSetValueWithPath(CGMutableImageMetadata, CGImageMetadataTag?, CFString, CFTypeRef) -> Bool](cgimagemetadatasetvaluewithpath(_:_:_:_:).md)
  Update the value of an existing metadata tag, or create a new tag using the specified information.
- [func CGImageMetadataSetValueMatchingImageProperty(CGMutableImageMetadata, CFString, CFString, CFTypeRef) -> Bool](cgimagemetadatasetvaluematchingimageproperty(_:_:_:_:).md)
  Updates the value of the metadata tag assigned to the specified image property.
- [func CGImageMetadataSetTagWithPath(CGMutableImageMetadata, CGImageMetadataTag?, CFString, CGImageMetadataTag) -> Bool](cgimagemetadatasettagwithpath(_:_:_:_:).md)
  Sets the tag at the specified path in the metadata object.
- [func CGImageMetadataRemoveTagWithPath(CGMutableImageMetadata, CGImageMetadataTag?, CFString) -> Bool](cgimagemetadataremovetagwithpath(_:_:_:).md)
  Removes the tag at the specified path from the metadata object.
### Registering a Custom Namespace
- [func CGImageMetadataRegisterNamespaceForPrefix(CGMutableImageMetadata, CFString, CFString, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](cgimagemetadataregisternamespaceforprefix(_:_:_:_:).md)
  Registers the specified namespace and prefix with the metadata object.

## Relationships

### Inherits From
- [CGImageMetadata](cgimagemetadata.md)
### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [class CGImageMetadata](cgimagemetadata.md)
  An immutable object that contains the XMP metadata associated with an image.
- [class CGImageMetadataTag](cgimagemetadatatag.md)
  An immutable type that contains information about a single piece of image metadata.
- [XMP Namespaces and Prefixes](xmp-namespaces-and-prefixes.md)
  Discover the public namespaces and prefixes that exist in XMP metadata tags.
- [let kCFErrorDomainCGImageMetadata: CFString](kcferrordomaincgimagemetadata.md)
  The domain for metadata-related errors that originate in the Image I/O framework.
- [enum CGImageMetadataErrors](cgimagemetadataerrors.md)
  Constants for errors that occur when getting or setting metadata information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgmutableimagemetadata)*