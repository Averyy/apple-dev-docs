# flushHostCache

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Releases the cache of existing `NSHost` objects so subsequent requests for `NSHost` objects create new ones.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

> **Deprecated**: `NSHost` does not implement caching in macOS 10.6 and later.

## Declaration

```objc
+ (void) flushHostCache;
```

#### Discussion

`NSHost` objects that were retained before this method was invoked remain valid.

## See Also

### Managing the Host Cache
- [+ isHostCacheEnabled](./ishostcacheenabled.md)
  Indicates whether caching is turned on or off.
- [+ setHostCacheEnabled:](./sethostcacheenabled_.md)
  Specifies whether the receiver is to cache instances as it creates them to avoid creating duplicate instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nshost/flushhostcache)*