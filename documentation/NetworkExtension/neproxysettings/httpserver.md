# httpServer

**Framework**: Network Extension  
**Kind**: property

An [`NEProxyServer`](neproxyserver.md) object containing the static HTTP proxy server settings.

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
var httpServer: NEProxyServer? { get set }
```

#### Discussion

If [`autoProxyConfigurationEnabled`](neproxysettings/autoproxyconfigurationenabled.md) is [`false`](https://developer.apple.com/documentation/Swift/false) and [`httpEnabled`](neproxysettings/httpenabled.md) is [`true`](https://developer.apple.com/documentation/Swift/true), then the proxy server specified in this property will be used for HTTP connections.

## See Also

- [var autoProxyConfigurationEnabled: Bool](neproxysettings/autoproxyconfigurationenabled.md)
  A Boolean indicating if proxy auto-configuration is enabled.
- [var httpEnabled: Bool](neproxysettings/httpenabled.md)
  A Boolean indicating if a static HTTP proxy will be used.
- [var httpsEnabled: Bool](neproxysettings/httpsenabled.md)
  A Boolean indicating if a static HTTPS proxy will be used.
- [var httpsServer: NEProxyServer?](neproxysettings/httpsserver.md)
  An [`NEProxyServer`](neproxyserver.md) object containing the static HTTPS proxy server settings.
- [class NEProxyServer](neproxyserver.md)
  `NEProxyServer` contains settings for a proxy server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neproxysettings/httpserver)*