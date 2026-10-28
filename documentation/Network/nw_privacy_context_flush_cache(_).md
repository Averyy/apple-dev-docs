# nw_privacy_context_flush_cache(_:)

**Framework**: Network  
**Kind**: func  
**Role**: Function

Flushes all cached data, such as TLS session state, created by connections associated with the privacy context.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func nw_privacy_context_flush_cache(_ privacy_context: nw_privacy_context_t)
```

```c
void nw_privacy_context_flush_cache(nw_privacy_context_t privacy_context);
```

## Discussion

Flushing the cache may be asynchronous, which means that it will take effect shortly after you invoke the function.

## See Also

### Configuring Custom Privacy Settings
- [func nw_privacy_context_create(UnsafePointer<CChar>) -> nw_privacy_context_t](./nw_privacy_context_create%28_%29.md)
  Initializes a privacy context with a description string.
- [func nw_privacy_context_disable_logging(nw_privacy_context_t)](./nw_privacy_context_disable_logging%28_%29.md)
  Disables system logging of connection activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_privacy_context_flush_cache(_:))*