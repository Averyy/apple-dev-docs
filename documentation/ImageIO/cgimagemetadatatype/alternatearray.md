# CGImageMetadataType.alternateArray

**Framework**: Image I/O  
**Kind**: case

An ordered array, in which all elements are alternates for the same value.

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
case alternateArray
```

#### Discussion

During serialization, this type becomes `<rdf:Alt>` in the XMP format.

## See Also

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
- [CGImageMetadataType.alternateText](cgimagemetadatatype/alternatetext.md)
  An alternate array, in which all elements are localized strings for the same value.
- [CGImageMetadataType.structure](cgimagemetadatatype/structure.md)
  A collection of keys and values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagemetadatatype/alternatearray)*