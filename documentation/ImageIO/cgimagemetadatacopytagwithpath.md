# CGImageMetadataCopyTagWithPath(_:_:_:)

**Framework**: Image I/O  
**Kind**: func

Searches for a specific metadata tag within a metadata collection.

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
func CGImageMetadataCopyTagWithPath(_ metadata: CGImageMetadata, _ parent: CGImageMetadataTag?, _ path: CFString) -> CGImageMetadataTag?
```

#### Return Value

A copy of the [`CGImageMetadataTag`](cgimagemetadatatag.md) object at the specified path, or `NULL` if the tag wasn’t found.

#### Discussion

If you specify a valid tag in the `parent` parameter, you may omit the parent’s path information from the `path` parameter. For example, to access the `RedEyeMode` field, specify the [`CGImageMetadataTag`](cgimagemetadatatag.md) object for the `Flash` parent property, and specify `“RedEyeMode”` for the path string.

If a tag contains a custom prefix that is not already present in the metadata object, call [`CGImageMetadataRegisterNamespaceForPrefix(_:_:_:_:)`](cgimagemetadataregisternamespaceforprefix(_:_:_:_:).md) to register that prefix before you search for it with this function.

## Parameters

- `metadata`: The metadata object that contains the tags.
- `parent`: The parent tag, if any. Specify   to start the search in the top-level tags of the metadata object. If this parameter is  , you must include a valid prefix string in the   parameter.
- `path`: Use the ? character to delimit qualifiers for tags with string values. You may not use this character for arrays and structures.

## See Also

- [func CGImageMetadataCopyTags(CGImageMetadata) -> CFArray?](cgimagemetadatacopytags(_:).md)
  Returns an array of root-level metadata tags from the specified metadata object.
- [func CGImageMetadataCopyTagMatchingImageProperty(CGImageMetadata, CFString, CFString) -> CGImageMetadataTag?](cgimagemetadatacopytagmatchingimageproperty(_:_:_:).md)
  Searches for the specified image property and, if found, returns the corresponding tag object.
- [func CGImageMetadataCopyStringValueWithPath(CGImageMetadata, CGImageMetadataTag?, CFString) -> CFString?](cgimagemetadatacopystringvaluewithpath(_:_:_:).md)
  Searches the metadata for the specified tag, and returns its string value if it exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagemetadatacopytagwithpath(_:_:_:))*