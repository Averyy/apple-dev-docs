# connectionProxyDictionary

**Framework**: Foundation  
**Kind**: property

A dictionary containing information about the proxy to use within this session.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var connectionProxyDictionary: [AnyHashable : Any]? { get set }
```

#### Discussion

This property controls which proxy tasks within sessions based on this configuration use when connecting to remote hosts.

Prefer using [`proxyConfigurations`](urlsessionconfiguration/proxyconfigurations.md), which supports secure proxy and relay types.

The default value is `NULL`, which means that tasks use the default system settings.

See `Global Proxy Configuration` for more information about these dictionaries.

## See Also

- [var httpMaximumConnectionsPerHost: Int](urlsessionconfiguration/httpmaximumconnectionsperhost.md)
  The maximum number of simultaneous connections to make to a given host.
- [var httpShouldUsePipelining: Bool](urlsessionconfiguration/httpshouldusepipelining.md)
  A Boolean value that determines whether the session should use HTTP pipelining.
- [var proxyConfigurations: [ProxyConfiguration]](urlsessionconfiguration/proxyconfigurations.md)
  An array of proxy configuration objects containing information about the proxies to use within this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/connectionproxydictionary)*