# CGImageMetadataTagCopyNamespace(_:)

**Framework**: Image I/O  
**Kind**: func

Returns an immutable copy of the tag’s XMP namespace.

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
func CGImageMetadataTagCopyNamespace(_ tag: CGImageMetadataTag) -> CFString?
```

#### Return Value

An immutable string that contains the tag’s namespace. For a list of public namespaces, see [`XMP Namespaces and Prefixes`](xmp-namespaces-and-prefixes.md). You are responsible for releasing this string.

#### Discussion

By convention, namespaces end with either a `/` or `#` character. For example, EXIF metadata uses the namespace `http://ns.adobe.com/exif/1.0/`. Custom namespaces must be a valid XML namespace.

## Parameters

- `tag`: The metadata tag from which to fetch the namespace information.

## See Also

- [func CGImageMetadataTagCopyPrefix(CGImageMetadataTag) -> CFString?](cgimagemetadatatagcopyprefix(_:).md)
  Returns an immutable copy of the tag’s prefix.
- [func CGImageMetadataTagCopyName(CGImageMetadataTag) -> CFString?](cgimagemetadatatagcopyname(_:).md)
  Returns an immutable copy of the tag’s name.
- [func CGImageMetadataTagCopyValue(CGImageMetadataTag) -> CFTypeRef?](cgimagemetadatatagcopyvalue(_:).md)
  Returns a shallow copy of the tag’s value, which is suitable only for reading.
- [func CGImageMetadataTagCopyQualifiers(CGImageMetadataTag) -> CFArray?](cgimagemetadatatagcopyqualifiers(_:).md)
  Returns a shallow copy of the metadata tags that act as qualifiers for the current tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagemetadatatagcopynamespace(_:))*