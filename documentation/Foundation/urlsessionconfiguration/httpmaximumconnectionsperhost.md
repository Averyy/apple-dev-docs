# httpMaximumConnectionsPerHost

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The maximum number of simultaneous HTTP/1.1 connections to make to a given host.

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

```objc
@property NSInteger HTTPMaximumConnectionsPerHost;
```

## Discussion

This property determines the maximum number of simultaneous HTTP/1.1 connections made to each host by tasks within sessions based on this configuration.

This limit is per session, so if you use multiple sessions, your app as a whole may exceed this limit. Additionally, depending on your connection to the Internet, a session may use a lower limit than the one you specify.

The default value is `6`.

HTTP/2 and later run multiple requests over a single connection and thus ignore this property.

## See Also

### Setting HTTP policy and proxy properties
- [var httpShouldUsePipelining: Bool](./httpshouldusepipelining.md)
  A Boolean value that determines whether the session should use HTTP pipelining.
- [var proxyConfigurations: [ProxyConfiguration]](./proxyconfigurations.md)
  An array of proxy configuration objects containing information about the proxies to use within this session.
- [var connectionProxyDictionary: [AnyHashable : Any]?](./connectionproxydictionary.md)
  A dictionary containing information about the proxy to use within this session.
- [proxyConfigurations](../nsurlsessionconfiguration/proxyconfigurations.md)
  An array of proxy configuration objects containing information about the proxies to use within this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/httpmaximumconnectionsperhost)*