# thumbnail

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A thumbnail image of the URL.

**Availability**:
- macOS 10.10+ - Deprecated in 12.0

> **Deprecated**: Use the QuickLookThumbnailing framework and extension point instead

## Declaration

```swift
var thumbnail: NSImage? { get }
```

#### Discussion

The URL populates ths property by retrieving the [`thumbnailKey`](../urlresourcekey/thumbnailkey.md) from the resource values, and is `nil` if there’s no value for the key.

## See Also

### Thumbnail values
- [var thumbnailDictionary: [URLThumbnailDictionaryItem : UIImage]?](./thumbnaildictionary-7jyzz.md)
  A dictionary of UIKit image objects keyed by size.
- [var thumbnailDictionary: [URLThumbnailDictionaryItem : NSImage]?](./thumbnaildictionary-4ztst.md)
  A dictionary of AppKit image objects keyed by size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresourcevalues/thumbnail)*