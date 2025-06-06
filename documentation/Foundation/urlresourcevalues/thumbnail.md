# thumbnail

**Framework**: Foundation  
**Kind**: property

A thumbnail image of the URL.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var thumbnail: NSImage? { get }
```

#### Discussion

The URL populates ths property by retrieving the [`thumbnailKey`](urlresourcekey/thumbnailkey.md) from the resource values, and is `nil` if there’s no value for the key.

## See Also

- [var thumbnailDictionary: [URLThumbnailDictionaryItem : UIImage]?](urlresourcevalues/thumbnaildictionary-7jyzz.md)
  A dictionary of UIKit image objects keyed by size.
- [var thumbnailDictionary: [URLThumbnailDictionaryItem : NSImage]?](urlresourcevalues/thumbnaildictionary-4ztst.md)
  A dictionary of AppKit image objects keyed by size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresourcevalues/thumbnail)*