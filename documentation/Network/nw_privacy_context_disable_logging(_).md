# nw_privacy_context_disable_logging(_:)

**Framework**: Network  
**Kind**: func  
**Role**: Function

Disables system logging of connection activity.

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
func nw_privacy_context_disable_logging(_ privacy_context: nw_privacy_context_t)
```

```c
void nw_privacy_context_disable_logging(nw_privacy_context_t privacy_context);
```

## See Also

### Configuring Custom Privacy Settings
- [func nw_privacy_context_create(UnsafePointer<CChar>) -> nw_privacy_context_t](./nw_privacy_context_create%28_%29.md)
  Initializes a privacy context with a description string.
- [func nw_privacy_context_flush_cache(nw_privacy_context_t)](./nw_privacy_context_flush_cache%28_%29.md)
  Flushes all cached data, such as TLS session state, created by connections associated with the privacy context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_privacy_context_disable_logging(_:))*