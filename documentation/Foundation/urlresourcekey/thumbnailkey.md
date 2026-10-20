# thumbnailKey

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

All thumbnails as a single NSImage (read-write).

**Availability**:
- macOS 10.10+ - Deprecated in 12.0

> **Deprecated**: Use the QuickLookThumbnailing framework and extension point instead

## Declaration

```swift
static let thumbnailKey: URLResourceKey
```

```c
extern NSURLResourceKey const NSURLThumbnailKey;
```

## See Also

### Thumbnail keys
- [static let thumbnailDictionaryKey: URLResourceKey](./thumbnaildictionarykey.md)
  A dictionary of NSImage/UIImage objects keyed by size (read-write). See [`URLThumbnailDictionaryItem`](../urlthumbnaildictionaryitem.md) for a list of possible keys.
- [struct URLThumbnailDictionaryItem](../urlthumbnaildictionaryitem.md)
  Possible keys for the [`thumbnailDictionaryKey`](./thumbnaildictionarykey.md) dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresourcekey/thumbnailkey)*