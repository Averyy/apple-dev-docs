# recache()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invalidates and frees offscreen caches of all image representations.

**Availability**:
- macOS

## Declaration

```swift
func recache()
```

```objc
- (void) recache;
```

#### Discussion

If you modify an image representation, you must send a  [`recache()`](./recache%28%29.md) message to the corresponding image object to force the changes to be recached. The next time any image representation is drawn, it is asked to recreate its cached image. If you do not send this message, the image representation may use the old cache data. This method simply clears the cached image data; it does not delete the `NSCachedImageRep` objects associated with any image representations.

If you do not plan to use an image again right away, you can free its caches to reduce the amount of memory consumed by your program.

## See Also

### Managing Caching Options
- [var cacheMode: NSImage.CacheMode](./cachemode-swift.property.md)
  The image’s caching mode.
- [NSImage.CacheMode](./cachemode-swift.enum.md)
  Constants that specify the caching policy on a per-image basis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/recache())*