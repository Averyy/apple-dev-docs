# CGImageMetadataType

**Framework**: Image I/O  
**Kind**: enum

Constants that indicate the XMP type for a metadata tag.

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
enum CGImageMetadataType
```

#### Overview

Use these constants to identify the type of metadata in a [`CGImageMetadataTag`](cgimagemetadatatag.md) opaque type. The type tells you how to interpret the value of the metadata tag. When creating a new [`CGImageMetadataTag`](cgimagemetadatatag.md), specify a type so the system knows how to serialize the data to the XMP format.

## Topics

### Metadata Types
- [CGImageMetadataType.invalid](cgimagemetadatatype/invalid.md)
  An invalid metadata type.
- [CGImageMetadataType.default](cgimagemetadatatype/default.md)
  The default type for new tags.
- [CGImageMetadataType.string](cgimagemetadatatype/string.md)
  A string value.
- [CGImageMetadataType.arrayUnordered](cgimagemetadatatype/arrayunordered.md)
  An array that doesn’t preserve the order of items.
- [CGImageMetadataType.arrayOrdered](cgimagemetadatatype/arrayordered.md)
  An array that preserves the order of items.
- [CGImageMetadataType.alternateArray](cgimagemetadatatype/alternatearray.md)
  An ordered array, in which all elements are alternates for the same value.
- [CGImageMetadataType.alternateText](cgimagemetadatatype/alternatetext.md)
  An alternate array, in which all elements are localized strings for the same value.
- [CGImageMetadataType.structure](cgimagemetadatatype/structure.md)
  A collection of keys and values.
### Initializers
- [init?(rawValue: Int32)](cgimagemetadatatype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func CGImageMetadataTagGetType(CGImageMetadataTag) -> CGImageMetadataType](cgimagemetadatataggettype(_:).md)
  Returns the type of the metadata tag’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagemetadatatype)*