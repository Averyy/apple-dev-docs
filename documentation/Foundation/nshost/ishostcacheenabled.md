# isHostCacheEnabled

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Indicates whether caching is turned on or off.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

> **Deprecated**: `NSHost` does not implement caching in macOS 10.6 and later.

## Declaration

```objc
+ (BOOL) isHostCacheEnabled;
```

## Return Value

[`true`](../../Swift/true.md) when caching is turned on; [`false`](../../Swift/false.md) otherwise.

## See Also

### Managing the Host Cache
- [+ setHostCacheEnabled:](./sethostcacheenabled_.md)
  Specifies whether the receiver is to cache instances as it creates them to avoid creating duplicate instances.
- [+ flushHostCache](./flushhostcache.md)
  Releases the cache of existing `NSHost` objects so subsequent requests for `NSHost` objects create new ones.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nshost/ishostcacheenabled)*