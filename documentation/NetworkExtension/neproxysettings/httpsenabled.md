# httpsEnabled

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A Boolean indicating if a static HTTPS proxy will be used.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var httpsEnabled: Bool { get set }
```

```objc
@property BOOL HTTPSEnabled;
```

## See Also

### Accessing Manual Proxy Properties
- [var httpEnabled: Bool](./httpenabled.md)
  A Boolean indicating if a static HTTP proxy will be used.
- [var httpServer: NEProxyServer?](./httpserver.md)
  An [`NEProxyServer`](../neproxyserver.md) object containing the static HTTP proxy server settings.
- [var httpsServer: NEProxyServer?](./httpsserver.md)
  An [`NEProxyServer`](../neproxyserver.md) object containing the static HTTPS proxy server settings.
- [class NEProxyServer](../neproxyserver.md)
  `NEProxyServer` contains settings for a proxy server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neproxysettings/httpsenabled)*