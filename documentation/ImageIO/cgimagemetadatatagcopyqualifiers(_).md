# CGImageMetadataTagCopyQualifiers(_:)

**Framework**: Image I/O  
**Kind**: func  
**Role**: Function

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

```c
extern CFArrayRefCGImageMetadataTagCopyQualifiers(CGImageMetadataTagRef tag);
```

#### Return Value

An array of [`CGImageMetadataTag`](./cgimagemetadatatag.md) types that represent the current tag’s qualifiers, or `NULL` if the tag has no qualifiers.

#### Discussion

XMP allows a metadata tag to contain supplemental tags that act as qualifiers on the content. For example, the `xml:lang` qualifier provides alternate text entries for the current tag. Each qualifier is a [`CGImageMetadataTag`](./cgimagemetadatatag.md) with its own namespace, prefix, name, and value.

## Parameters

- `tag`: The metadata tag from which to fetch the namespace information.

## See Also

### Getting the Attributes of the Tag
- [func CGImageMetadataTagCopyNamespace(CGImageMetadataTag) -> CFString?](./cgimagemetadatatagcopynamespace%28_%29.md)
  Returns an immutable copy of the tag’s XMP namespace.
- [func CGImageMetadataTagCopyPrefix(CGImageMetadataTag) -> CFString?](./cgimagemetadatatagcopyprefix%28_%29.md)
  Returns an immutable copy of the tag’s prefix.
- [func CGImageMetadataTagCopyName(CGImageMetadataTag) -> CFString?](./cgimagemetadatatagcopyname%28_%29.md)
  Returns an immutable copy of the tag’s name.
- [func CGImageMetadataTagCopyValue(CGImageMetadataTag) -> CFTypeRef?](./cgimagemetadatatagcopyvalue%28_%29.md)
  Returns a shallow copy of the tag’s value, which is suitable only for reading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagemetadatatagcopyqualifiers(_:))*