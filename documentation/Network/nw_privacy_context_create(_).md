# nw_privacy_context_create(_:)

**Framework**: Network  
**Kind**: func  
**Role**: Function

Initializes a privacy context with a description string.

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
func nw_privacy_context_create(_ description: UnsafePointer<CChar>) -> nw_privacy_context_t
```

```c
nw_privacy_context_tnw_privacy_context_create(const char *description);
```

## See Also

### Configuring Custom Privacy Settings
- [func nw_privacy_context_disable_logging(nw_privacy_context_t)](./nw_privacy_context_disable_logging%28_%29.md)
  Disables system logging of connection activity.
- [func nw_privacy_context_flush_cache(nw_privacy_context_t)](./nw_privacy_context_flush_cache%28_%29.md)
  Flushes all cached data, such as TLS session state, created by connections associated with the privacy context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_privacy_context_create(_:))*