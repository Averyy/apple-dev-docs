# URLThumbnailDictionaryItem

**Framework**: Foundation  
**Kind**: struct

Possible keys for the [`thumbnailDictionaryKey`](urlresourcekey/thumbnaildictionarykey.md) dictionary.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct URLThumbnailDictionaryItem
```

## Topics

### Creating a Thumbnail Dictionary Key
- [init(String)](urlthumbnaildictionaryitem/init(_:).md)
  Creates a thumbnail dictionary item key from the provided constant string.
- [init(rawValue: String)](urlthumbnaildictionaryitem/init(rawvalue:).md)
  Creates a thumbnail dictionary item key from the provided raw value string.
### Constants
- [static let NSThumbnail1024x1024SizeKey: URLThumbnailDictionaryItem](urlthumbnaildictionaryitem/nsthumbnail1024x1024sizekey.md)
  A 1024 x 1024 pixel thumbnail as a `UIImage` on iOS or an `NSImage` in macOS.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [static let thumbnailKey: URLResourceKey](urlresourcekey/thumbnailkey.md)
  All thumbnails as a single NSImage (read-write).
- [static let thumbnailDictionaryKey: URLResourceKey](urlresourcekey/thumbnaildictionarykey.md)
  A dictionary of NSImage/UIImage objects keyed by size (read-write). See [`URLThumbnailDictionaryItem`](urlthumbnaildictionaryitem.md) for a list of possible keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlthumbnaildictionaryitem)*