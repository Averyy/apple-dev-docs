# AGL_FORMAT_CACHE_SIZE

**Framework**: AGL  
**Kind**: var

**Availability**:
- macOS 10.0+

## Declaration

```swift
var AGL_FORMAT_CACHE_SIZE: Int32 { get }
```

#### Discussion

The associated value is the size of the positive pixel format cache and is initially set to `5`. If your application needs to use `n` different attribute lists to choose `n` different pixel formats repeatedly, then the application should set the cache size to `n` to maximize performance. After your application calls the [`aglChoosePixelFormat`](https://developer.apple.comhttps://developer.apple.com/library/archive/#id(F15007)) function for the last time, you might want to set the cache size to `1` to minimize the memory used by the AGL library.

## See Also

- [var AGL_CLEAR_FORMAT_CACHE: Int32](agl_clear_format_cache.md)
- [var AGL_RETAIN_RENDERERS: Int32](agl_retain_renderers.md)
- [var AGL_CLEAR_FORMAT_CACHE: Int32](agl_clear_format_cache.md)
- [var AGL_RETAIN_RENDERERS: Int32](agl_retain_renderers.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/agl/agl_format_cache_size)*