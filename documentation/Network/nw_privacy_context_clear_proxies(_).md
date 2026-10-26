# nw_privacy_context_clear_proxies(_:)

**Framework**: Network  
**Kind**: func  
**Role**: Function

Clears out any proxies added using [`nw_privacy_context_add_proxy(_:_:)`](./nw_privacy_context_add_proxy%28_,_%29.md)

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func nw_privacy_context_clear_proxies(_ privacy_context: nw_privacy_context_t)
```

```c
void nw_privacy_context_clear_proxies(nw_privacy_context_t privacy_context);
```

## Parameters

- `privacy_context`: A privacy context to modify. This can include the default privacy context.

## See Also

### Configuring Proxies
- [func nw_privacy_context_add_proxy(nw_privacy_context_t, nw_proxy_config_t)](./nw_privacy_context_add_proxy%28_,_%29.md)
  Applies a proxy configuration to all connections associated with this context.
- [typealias nw_proxy_config_t](./nw_proxy_config_t.md)
  A proxy configuration for Relays, Oblivious HTTP, HTTP CONNECT, or SOCKSv5.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_privacy_context_clear_proxies(_:))*