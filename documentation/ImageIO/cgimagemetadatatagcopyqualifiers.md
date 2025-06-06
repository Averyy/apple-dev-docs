# CGImageMetadataTagCopyQualifiers(_:)

**Framework**: Image I/O  
**Kind**: func

Returns a shallow copy of the metadata tags that act as qualifiers for the current tag.

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
func CGImageMetadataTagCopyQualifiers(_ tag: CGImageMetadataTag) -> CFArray?
```

#### Return Value

An array of [`CGImageMetadataTag`](cgimagemetadatatag.md) types that represent the current tag’s qualifiers, or `NULL` if the tag has no qualifiers.

#### Discussion

XMP allows a metadata tag to contain supplemental tags that act as qualifiers on the content. For example, the `xml:lang` qualifier provides alternate text entries for the current tag. Each qualifier is a [`CGImageMetadataTag`](cgimagemetadatatag.md) with its own namespace, prefix, name, and value.

## Parameters

- `tag`: The metadata tag from which to fetch the namespace information.

## See Also

- [func CGImageMetadataTagCopyNamespace(CGImageMetadataTag) -> CFString?](cgimagemetadatatagcopynamespace(_:).md)
  Returns an immutable copy of the tag’s XMP namespace.
- [func CGImageMetadataTagCopyPrefix(CGImageMetadataTag) -> CFString?](cgimagemetadatatagcopyprefix(_:).md)
  Returns an immutable copy of the tag’s prefix.
- [func CGImageMetadataTagCopyName(CGImageMetadataTag) -> CFString?](cgimagemetadatatagcopyname(_:).md)
  Returns an immutable copy of the tag’s name.
- [func CGImageMetadataTagCopyValue(CGImageMetadataTag) -> CFTypeRef?](cgimagemetadatatagcopyvalue(_:).md)
  Returns a shallow copy of the tag’s value, which is suitable only for reading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagemetadatatagcopyqualifiers(_:))*