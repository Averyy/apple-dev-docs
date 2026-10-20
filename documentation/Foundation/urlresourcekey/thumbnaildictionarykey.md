# thumbnailDictionaryKey

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A dictionary of NSImage/UIImage objects keyed by size (read-write). See [`URLThumbnailDictionaryItem`](../urlthumbnaildictionaryitem.md) for a list of possible keys.

**Availability**:
- iOS 8.0+ - Deprecated in 15.0
- iPadOS 8.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.10+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 8.0

> **Deprecated**: Use the QuickLookThumbnailing framework and extension point instead

## Declaration

```swift
static let thumbnailDictionaryKey: URLResourceKey
```

```c
extern NSURLResourceKey const NSURLThumbnailDictionaryKey;
```

## See Also

### Thumbnail keys
- [static let thumbnailKey: URLResourceKey](./thumbnailkey.md)
  All thumbnails as a single NSImage (read-write).
- [struct URLThumbnailDictionaryItem](../urlthumbnaildictionaryitem.md)
  Possible keys for the [`thumbnailDictionaryKey`](./thumbnaildictionarykey.md) dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresourcekey/thumbnaildictionarykey)*