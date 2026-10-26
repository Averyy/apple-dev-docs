# nw_proxy_config_get_failover_allowed(_:)

**Framework**: Network  
**Kind**: func  
**Role**: Function

Checks if a proxy configuration allows failover to non-proxied connections.

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
func nw_proxy_config_get_failover_allowed(_ proxy_config: nw_proxy_config_t) -> Bool
```

```c
bool nw_proxy_config_get_failover_allowed(nw_proxy_config_t proxy_config);
```

#### Return Value

A Boolean that indicates whether or not a proxy configuration allows failover to non-proxied connections.

## Parameters

- `proxy_config`: The proxy configuration to check.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_proxy_config_get_failover_allowed(_:))*