# httpMaximumConnectionsPerHost

**Framework**: Foundation  
**Kind**: property

The maximum number of simultaneous connections to make to a given host.

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
var httpMaximumConnectionsPerHost: Int { get set }
```

#### Discussion

This property determines the maximum number of simultaneous connections made to each host by tasks within sessions based on this configuration.

This limit is per session, so if you use multiple sessions, your app as a whole may exceed this limit. Additionally, depending on your connection to the Internet, a session may use a lower limit than the one you specify.

The default value is `6`.

## See Also

- [var httpShouldUsePipelining: Bool](urlsessionconfiguration/httpshouldusepipelining.md)
  A Boolean value that determines whether the session should use HTTP pipelining.
- [var proxyConfigurations: [ProxyConfiguration]](urlsessionconfiguration/proxyconfigurations.md)
  An array of proxy configuration objects containing information about the proxies to use within this session.
- [var connectionProxyDictionary: [AnyHashable : Any]?](urlsessionconfiguration/connectionproxydictionary.md)
  A dictionary containing information about the proxy to use within this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/httpmaximumconnectionsperhost)*