# cacheMode

**Framework**: AppKit  
**Kind**: property

The image’s caching mode.

**Availability**:
- macOS ?+

## Declaration

```swift
var cacheMode: NSImage.CacheMode { get set }
```

#### Discussion

The caching mode determines when the image representations use offscreen caches. Offscreen caches speed up rendering time but do so by using extra memory. In the default caching mode (`NSImageCacheDefault`), each image representation chooses the caching technique that produces the fastest drawing times. For example, in the default mode, the `NSPDFImageRep` and `NSEPSImageRep` classes use the `NSImageCacheAlways` mode but the `NSBitmapImageRep` class uses the `NSImageCacheBySize` mode.  For a list of possible values, see [`NSImage.CacheMode`](nsimage/cachemode-swift.enum.md). This value is set to `NSImageCacheDefault` by default.

## See Also

- [func recache()](nsimage/recache.md)
  Invalidates and frees offscreen caches of all image representations.
- [NSImage.CacheMode](nsimage/cachemode-swift.enum.md)
  Constants that specify the caching policy on a per-image basis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/cachemode-swift.property)*