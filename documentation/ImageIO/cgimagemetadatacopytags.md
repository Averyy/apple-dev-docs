# CGImageMetadataCopyTags(_:)

**Framework**: Image I/O  
**Kind**: func

Returns an array of root-level metadata tags from the specified metadata object.

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
func CGImageMetadataCopyTags(_ metadata: CGImageMetadata) -> CFArray?
```

#### Return Value

An array that contains a shallow copy of all root-level [`CGImageMetadataTag`](cgimagemetadatatag.md) objects. This array contains only the root-level tags. It doesn’t contain any nested tags.

## Parameters

- `metadata`: The metadata object that contains the tags.

## See Also

- [func CGImageMetadataCopyTagWithPath(CGImageMetadata, CGImageMetadataTag?, CFString) -> CGImageMetadataTag?](cgimagemetadatacopytagwithpath(_:_:_:).md)
  Searches for a specific metadata tag within a metadata collection.
- [func CGImageMetadataCopyTagMatchingImageProperty(CGImageMetadata, CFString, CFString) -> CGImageMetadataTag?](cgimagemetadatacopytagmatchingimageproperty(_:_:_:).md)
  Searches for the specified image property and, if found, returns the corresponding tag object.
- [func CGImageMetadataCopyStringValueWithPath(CGImageMetadata, CGImageMetadataTag?, CFString) -> CFString?](cgimagemetadatacopystringvaluewithpath(_:_:_:).md)
  Searches the metadata for the specified tag, and returns its string value if it exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagemetadatacopytags(_:))*