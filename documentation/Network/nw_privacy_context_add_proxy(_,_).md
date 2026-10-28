# nw_privacy_context_add_proxy(_:_:)

**Framework**: Network  
**Kind**: func  
**Role**: Function

Applies a proxy configuration to all connections associated with this context.

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
func nw_privacy_context_add_proxy(_ privacy_context: nw_privacy_context_t, _ proxy_config: nw_proxy_config_t)
```

```c
void nw_privacy_context_add_proxy(nw_privacy_context_t privacy_context, nw_proxy_config_t proxy_config);
```

## Discussion

If set on `NW_DEFAULT_PRIVACY_CONTEXT`, this proxy will additionally apply to other networking APIs used by the calling process.

## Parameters

- `privacy_context`: A privacy context to modify. This can include the default privacy context.
- `proxy_config`: A proxy configuration object to apply to all connections that use this context.

## See Also

### Configuring Proxies
- [func nw_privacy_context_clear_proxies(nw_privacy_context_t)](./nw_privacy_context_clear_proxies%28_%29.md)
  Clears out any proxies added using [`nw_privacy_context_add_proxy(_:_:)`](./nw_privacy_context_add_proxy%28_,_%29.md)
- [typealias nw_proxy_config_t](./nw_proxy_config_t.md)
  A proxy configuration for Relays, Oblivious HTTP, HTTP CONNECT, or SOCKSv5.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_privacy_context_add_proxy(_:_:))*