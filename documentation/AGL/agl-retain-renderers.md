# AGL_RETAIN_RENDERERS

**Framework**: AGL  
**Kind**: var

**Availability**:
- macOS 10.0+

## Declaration

```swift
var AGL_RETAIN_RENDERERS: Int32 { get }
```

#### Discussion

Specifies whether or not to retain loaded plug-in renderers in memory. When the associated value is nonzero, the AGL library will not unload any plug-in renderers even if they are no longer in use. This option is useful to improve the performance of applications that repeatedly destroy and recreate their only (or last) rendering context. Normally, when the last rendering context created by a particular plug-in renderer is destroyed, that renderer is unloaded from memory. When the associated value is zero, AGL returns to its normal mode of operation and all renderers that are not in use are unloaded.

## See Also

- [var AGL_FORMAT_CACHE_SIZE: Int32](agl_format_cache_size.md)
- [var AGL_CLEAR_FORMAT_CACHE: Int32](agl_clear_format_cache.md)
- [var AGL_FORMAT_CACHE_SIZE: Int32](agl_format_cache_size.md)
- [var AGL_CLEAR_FORMAT_CACHE: Int32](agl_clear_format_cache.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/agl/agl_retain_renderers)*