# CGImageMetadataErrors

**Framework**: Image I/O  
**Kind**: enum

Constants for errors that occur when getting or setting metadata information.

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
enum CGImageMetadataErrors
```

## Topics

### Error Codes
- [CGImageMetadataErrors.unknown](cgimagemetadataerrors/unknown.md)
  An error that indicates an unknown condition occurred.
- [CGImageMetadataErrors.unsupportedFormat](cgimagemetadataerrors/unsupportedformat.md)
  An error that indicates the metadata was in an unsupported format.
- [CGImageMetadataErrors.badArgument](cgimagemetadataerrors/badargument.md)
  An error that indicates a parameter was malformed or contained invalid data.
- [CGImageMetadataErrors.conflictingArguments](cgimagemetadataerrors/conflictingarguments.md)
  An error that indicates an attempt to save conflicting metadata values.
- [CGImageMetadataErrors.prefixConflict](cgimagemetadataerrors/prefixconflict.md)
  An error that indicates an attempt to register a namespace with a prefix that is different than the namespace’s existing prefix.
### Initializers
- [init?(rawValue: Int32)](cgimagemetadataerrors/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class CGImageMetadata](cgimagemetadata.md)
  An immutable object that contains the XMP metadata associated with an image.
- [class CGMutableImageMetadata](cgmutableimagemetadata.md)
  An opaque type for adding or modifying image metadata.
- [class CGImageMetadataTag](cgimagemetadatatag.md)
  An immutable type that contains information about a single piece of image metadata.
- [XMP Namespaces and Prefixes](xmp-namespaces-and-prefixes.md)
  Discover the public namespaces and prefixes that exist in XMP metadata tags.
- [let kCFErrorDomainCGImageMetadata: CFString](kcferrordomaincgimagemetadata.md)
  The domain for metadata-related errors that originate in the Image I/O framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagemetadataerrors)*