# httpsServer

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

An [`NEProxyServer`](../neproxyserver.md) object containing the static HTTPS proxy server settings.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var httpsServer: NEProxyServer? { get set }
```

```objc
@property (copy, nullable) NEProxyServer * HTTPSServer;
```

## Discussion

If [`autoProxyConfigurationEnabled`](./autoproxyconfigurationenabled.md) is [`false`](../../Swift/false.md) and [`httpsEnabled`](./httpsenabled.md) is [`true`](../../Swift/true.md), then the proxy server specified in this property will be used for HTTPS connections.

## See Also

### Related Documentation
- [var autoProxyConfigurationEnabled: Bool](./autoproxyconfigurationenabled.md)
  A Boolean indicating if proxy auto-configuration is enabled.
### Accessing Manual Proxy Properties
- [var httpEnabled: Bool](./httpenabled.md)
  A Boolean indicating if a static HTTP proxy will be used.
- [var httpServer: NEProxyServer?](./httpserver.md)
  An [`NEProxyServer`](../neproxyserver.md) object containing the static HTTP proxy server settings.
- [var httpsEnabled: Bool](./httpsenabled.md)
  A Boolean indicating if a static HTTPS proxy will be used.
- [class NEProxyServer](../neproxyserver.md)
  `NEProxyServer` contains settings for a proxy server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neproxysettings/httpsserver)*