# AGL_CLEAR_FORMAT_CACHE

**Framework**: AGL  
**Kind**: var

**Availability**:
- macOS 10.0+

## Declaration

```swift
var AGL_CLEAR_FORMAT_CACHE: Int32 { get }
```

#### Discussion

When the associated value is nonzero, specifies to reset the pixel format cache. Clearing the cache does not affect the size of the cache for future storage of pixel formats. To minimize the memory consumed by the cache, your application should also set the cache size to `1`.

## See Also

- [var AGL_FORMAT_CACHE_SIZE: Int32](agl_format_cache_size.md)
- [var AGL_RETAIN_RENDERERS: Int32](agl_retain_renderers.md)
- [var AGL_FORMAT_CACHE_SIZE: Int32](agl_format_cache_size.md)
- [var AGL_RETAIN_RENDERERS: Int32](agl_retain_renderers.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/agl/agl_clear_format_cache)*