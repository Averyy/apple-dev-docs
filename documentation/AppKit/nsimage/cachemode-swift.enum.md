# NSImage.CacheMode

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the caching policy on a per-image basis.

**Availability**:
- macOS

## Declaration

```swift
enum CacheMode
```

```c
enum NSImageCacheMode : NSUInteger;
```

## Overview

Set the caching policy using the [`cacheMode`](./cachemode-swift.property.md) property.

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
- [NSImage.CacheMode.default](./cachemode-swift.enum/default.md)
  Caching is unspecified.
- [NSImage.CacheMode.always](./cachemode-swift.enum/always.md)
  Always generate a cache when drawing.
- [NSImage.CacheMode.bySize](./cachemode-swift.enum/bysize.md)
  Cache if the cache size is smaller than the original data.
- [NSImage.CacheMode.never](./cachemode-swift.enum/never.md)
  Never cache; always draw direct.
### Initializers
- [init?(rawValue: UInt)](./cachemode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing Caching Options
- [var cacheMode: NSImage.CacheMode](./cachemode-swift.property.md)
  The image’s caching mode.
- [func recache()](./recache%28%29.md)
  Invalidates and frees offscreen caches of all image representations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/cachemode-swift.enum)*