# httpShouldUsePipelining

**Framework**: Foundation  
**Kind**: property

A Boolean value that determines whether the session should use HTTP pipelining.

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
var httpShouldUsePipelining: Bool { get set }
```

#### Discussion

This property determines whether tasks within sessions based on this configuration should use HTTP pipelining. You can also enable pipelining on a per-task basis by creating the task with an [`NSURLRequest`](nsurlrequest.md) object.

The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var httpMaximumConnectionsPerHost: Int](urlsessionconfiguration/httpmaximumconnectionsperhost.md)
  The maximum number of simultaneous connections to make to a given host.
- [var proxyConfigurations: [ProxyConfiguration]](urlsessionconfiguration/proxyconfigurations.md)
  An array of proxy configuration objects containing information about the proxies to use within this session.
- [var connectionProxyDictionary: [AnyHashable : Any]?](urlsessionconfiguration/connectionproxydictionary.md)
  A dictionary containing information about the proxy to use within this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/httpshouldusepipelining)*