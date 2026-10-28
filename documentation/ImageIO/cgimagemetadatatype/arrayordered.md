# CGImageMetadataType.arrayOrdered

**Framework**: Image I/O  
**Kind**: case  
**Role**: Case

An array that preserves the order of items.

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
case arrayOrdered
```

```c
kCGImageMetadataTypeArrayOrdered
```

## Discussion

During serialization, this type becomes `<rdf:Seq>` in the XMP format.

## See Also

### Metadata Types
- [CGImageMetadataType.invalid](./invalid.md)
  An invalid metadata type.
- [CGImageMetadataType.default](./default.md)
  The default type for new tags.
- [CGImageMetadataType.string](./string.md)
  A string value.
- [CGImageMetadataType.arrayUnordered](./arrayunordered.md)
  An array that doesn’t preserve the order of items.
- [CGImageMetadataType.alternateArray](./alternatearray.md)
  An ordered array, in which all elements are alternates for the same value.
- [CGImageMetadataType.alternateText](./alternatetext.md)
  An alternate array, in which all elements are localized strings for the same value.
- [CGImageMetadataType.structure](./structure.md)
  A collection of keys and values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagemetadatatype/arrayordered)*