# nw_proxy_config_set_username_and_password(_:_:_:)

**Framework**: Network  
**Kind**: func  
**Role**: Function

Sets a username and password to use as authentication for a proxy configuration.

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
func nw_proxy_config_set_username_and_password(_ proxy_config: nw_proxy_config_t, _ username: UnsafePointer<CChar>, _ password: UnsafePointer<CChar>?)
```

```c
void nw_proxy_config_set_username_and_password(nw_proxy_config_t proxy_config, const char *username, const char *password);
```

## Parameters

- `proxy_config`: The proxy configuration to modify.
- `username`: A proxy authentication username.
- `password`: A proxy authentication password.

## See Also

### Customizing Proxy Behavior
- [func nw_proxy_config_set_failover_allowed(nw_proxy_config_t, Bool)](./nw_proxy_config_set_failover_allowed%28_,_%29.md)
  Configures whether or not a proxy configuration allows failover to non-proxied connections. Failover isn’t allowed by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_proxy_config_set_username_and_password(_:_:_:))*