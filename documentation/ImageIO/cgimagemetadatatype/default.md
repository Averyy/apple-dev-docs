# CGImageMetadataType.default

**Framework**: Image I/O  
**Kind**: case

The default type for new tags.

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
case `default`
```

#### Discussion

When you create new tags, the system assigns this value initially. The system uses the Core Foundation type of the metadata tag’s value to determine an appropriate type. During the serialization process, the system converts the type automatically to a nondefault value.

## See Also

- [CGImageMetadataType.invalid](cgimagemetadatatype/invalid.md)
  An invalid metadata type.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagemetadatatype/default)*