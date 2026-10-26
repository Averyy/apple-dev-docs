# setHostCacheEnabled:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Specifies whether the receiver is to cache instances as it creates them to avoid creating duplicate instances.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

> **Deprecated**: `NSHost` does not implement caching in macOS 10.6 and later.

## Declaration

```objc
+ (void) setHostCacheEnabled:(BOOL) flag;
```

#### Discussion

This method doesn’t flush the cache. If you turn caching off and then back on, new requests for hosts use what was in the cache at the time caching was turned off. However, `NSHost` objects created while caching is turned off aren’t entered into the cache.

## Parameters

- `flag`: [`true`](../../Swift/true.md) to turn on caching. [`false`](../../Swift/false.md) to turn of caching.

## See Also

### Managing the Host Cache
- [+ isHostCacheEnabled](./ishostcacheenabled.md)
  Indicates whether caching is turned on or off.
- [+ flushHostCache](./flushhostcache.md)
  Releases the cache of existing `NSHost` objects so subsequent requests for `NSHost` objects create new ones.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nshost/sethostcacheenabled:)*