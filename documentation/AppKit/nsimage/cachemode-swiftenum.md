# NSImage.CacheMode

**Framework**: AppKit  
**Kind**: enum

Constants that specify the caching policy on a per-image basis.

**Availability**:
- macOS ?+

## Declaration

```swift
enum CacheMode
```

#### Overview

Set the caching policy using the [`cacheMode`](nsimage/cachemode-swift.property.md) property.

The following table specifies the default caching policy for the various types of image representation.

| Image Rep Class | Default caching policy |
| --- | --- |
| `NSBitmapImageRep` | `NSImageCacheBySize`. Cache if bitmap is 32-bits in 16-bit world or greater than 72 dpi. |
| `NSPICTImageRep` | `NSImageCacheBySize`. Same reasoning as `NSBitmapImageRep` in the event the PICT contains a bitmap. |
| `NSPDFImageRep` | `NSImageCacheAlways` |
| `NSCIImageRep` | `NSImageCacheBySize`. Cache if the bitmap depth does not match the screen depth or the resolution is greater than 72 dpi. |
| `NSEPSImageRep` | `NSImageCacheAlways` |
| `NSCustomImageRep` | `NSImageCacheAlways` |

## Topics

### Cache Options
- [NSImage.CacheMode.default](nsimage/cachemode-swift.enum/default.md)
  Caching is unspecified.
- [NSImage.CacheMode.always](nsimage/cachemode-swift.enum/always.md)
  Always generate a cache when drawing.
- [NSImage.CacheMode.bySize](nsimage/cachemode-swift.enum/bysize.md)
  Cache if the cache size is smaller than the original data.
- [NSImage.CacheMode.never](nsimage/cachemode-swift.enum/never.md)
  Never cache; always draw direct.
### Initializers
- [init?(rawValue: UInt)](nsimage/cachemode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var cacheMode: NSImage.CacheMode](nsimage/cachemode-swift.property.md)
  The image’s caching mode.
- [func recache()](nsimage/recache.md)
  Invalidates and frees offscreen caches of all image representations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/cachemode-swift.enum)*