# CGImageMetadataTagCopyPrefix(_:)

**Framework**: Image I/O  
**Kind**: func  
**Role**: Function

Returns an immutable copy of the tag’s prefix.

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
func CGImageMetadataTagCopyPrefix(_ tag: CGImageMetadataTag) -> CFString?
```

```c
extern CFStringRefCGImageMetadataTagCopyPrefix(CGImageMetadataTagRef tag);
```

#### Return Value

An immutable string that contains the tag’s prefix. For example, EXIF metadata uses the prefix `exif`. You are responsible for releasing this string.

## Parameters

- `tag`: The metadata tag from which to fetch the namespace information.

## See Also

### Getting the Attributes of the Tag
- [func CGImageMetadataTagCopyNamespace(CGImageMetadataTag) -> CFString?](./cgimagemetadatatagcopynamespace%28_%29.md)
  Returns an immutable copy of the tag’s XMP namespace.
- [func CGImageMetadataTagCopyName(CGImageMetadataTag) -> CFString?](./cgimagemetadatatagcopyname%28_%29.md)
  Returns an immutable copy of the tag’s name.
- [func CGImageMetadataTagCopyValue(CGImageMetadataTag) -> CFTypeRef?](./cgimagemetadatatagcopyvalue%28_%29.md)
  Returns a shallow copy of the tag’s value, which is suitable only for reading.
- [func CGImageMetadataTagCopyQualifiers(CGImageMetadataTag) -> CFArray?](./cgimagemetadatatagcopyqualifiers%28_%29.md)
  Returns a shallow copy of the metadata tags that act as qualifiers for the current tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagemetadatatagcopyprefix(_:))*