# connectionProxyDictionary

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, nullable) NSDictionary * connectionProxyDictionary;
```

#### Discussion

This property controls which proxy tasks within sessions based on this configuration use when connecting to remote hosts.

Prefer using [`proxyConfigurations`](./proxyconfigurations.md), which supports secure proxy and relay types.

The default value is `NULL`, which means that tasks use the default system settings.

See `Global Proxy Configuration` for more information about these dictionaries.

## See Also

### Setting HTTP policy and proxy properties
- [var httpMaximumConnectionsPerHost: Int](./httpmaximumconnectionsperhost.md)
  The maximum number of simultaneous HTTP/1.1 connections to make to a given host.
- [var httpShouldUsePipelining: Bool](./httpshouldusepipelining.md)
  A Boolean value that determines whether the session should use HTTP pipelining.
- [var proxyConfigurations: [ProxyConfiguration]](./proxyconfigurations.md)
  An array of proxy configuration objects containing information about the proxies to use within this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/connectionproxydictionary)*