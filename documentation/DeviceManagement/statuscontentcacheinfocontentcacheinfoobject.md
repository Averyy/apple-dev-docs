# StatusContentCacheInfoContentCacheInfoObject

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that contains info about the usage of the Content Cache on the device

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
object StatusContentCacheInfoContentCacheInfoObject
```

## Properties

- `cache-details` ([string]): The amount of disk space that various categories of cached content use. Apple defines these categories and they’re subject to change.
- `cache-free` (integer): The amount of disk space in bytes, available to the Content Cache.
- `cache-limit` (integer): The maximum amount of disk space in bytes, available to the Content Cache. A value of `0` indicates an unlimited amount. This value corresponds to `CacheLimit` in the installed [`ContentCaching`](contentcaching.md) configuration.
- `cache-status` (string): The level of cache pressure. `LOWSPACE` means cache pressure is high.
- `cache-used` (integer): The amount of disk space in bytes, cached content uses. The Content Cache allocates space in its cache for entire files even when it stores only part of those files in its cache.
- `max-cache-pressure-last-hour` (number): A floating-point number between `0.0` and `1.0` that represents how often the cache needed more disk space over the last hour of operation. A lower value is better.
- `personal-cache-free` (integer): The amount of disk space in bytes, available to the Content Cache for personal iCloud content.
- `personal-cache-limit` (integer): The maximum amount of disk space in bytes, available to the Content Cache for personal iCloud content. A value of `0` indicates an unlimited amount.
- `personal-cache-used` (integer): The amount of disk space, in bytes, available to the Content Cache for personal iCloud content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statuscontentcacheinfocontentcacheinfoobject)*