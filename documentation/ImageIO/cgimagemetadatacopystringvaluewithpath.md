# CGImageMetadataCopyStringValueWithPath(_:_:_:)

**Framework**: Image I/O  
**Kind**: func

Searches the metadata for the specified tag, and returns its string value if it exists.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGImageMetadataCopyStringValueWithPath(_ metadata: CGImageMetadata, _ parent: CGImageMetadataTag?, _ path: CFString) -> CFString?
```

#### Return Value

The string value for the specified tag, or `NULL` if the tag wasn’t found or doesn’t contain a string value.

#### Discussion

The XMP type of the property at the specified path must be [`CGImageMetadataType.string`](cgimagemetadatatype/string.md) or [`CGImageMetadataType.alternateText`](cgimagemetadatatype/alternatetext.md). If the property contains alternate text, this function returns the element with the `x-default` language qualifier.

## Parameters

- `metadata`: The metadata object to search.
- `parent`: The parent tag, if any. Specify   to start the search in the top-level tags of the metadata object. If this parameter is  , you must include a valid prefix string in the   parameter.
- `path`: Use the ? character to delimit qualifiers for tags with string values. You may not use this character for arrays and structures.

## See Also

- [func CGImageMetadataCopyTagWithPath(CGImageMetadata, CGImageMetadataTag?, CFString) -> CGImageMetadataTag?](cgimagemetadatacopytagwithpath(_:_:_:).md)
  Searches for a specific metadata tag within a metadata collection.
- [func CGImageMetadataCopyTags(CGImageMetadata) -> CFArray?](cgimagemetadatacopytags(_:).md)
  Returns an array of root-level metadata tags from the specified metadata object.
- [func CGImageMetadataCopyTagMatchingImageProperty(CGImageMetadata, CFString, CFString) -> CGImageMetadataTag?](cgimagemetadatacopytagmatchingimageproperty(_:_:_:).md)
  Searches for the specified image property and, if found, returns the corresponding tag object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagemetadatacopystringvaluewithpath(_:_:_:))*