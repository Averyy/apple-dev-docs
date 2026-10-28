# proxyConfigurations

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

An array of proxy configuration objects containing information about the proxies to use within this session.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
@property (copy) NSArray<NSObject<OS_nw_proxy_config> *> * proxyConfigurations;
```

## Discussion

This property controls which proxy tasks to use within sessions based on this configuration when connecting to remote hosts.

The default value is the empty array, which means that tasks use the default system settings.

## See Also

### Setting HTTP policy and proxy properties
- [var httpMaximumConnectionsPerHost: Int](../urlsessionconfiguration/httpmaximumconnectionsperhost.md)
  The maximum number of simultaneous HTTP/1.1 connections to make to a given host.
- [var httpShouldUsePipelining: Bool](../urlsessionconfiguration/httpshouldusepipelining.md)
  A Boolean value that determines whether the session should use HTTP pipelining.
- [var connectionProxyDictionary: [AnyHashable : Any]?](../urlsessionconfiguration/connectionproxydictionary.md)
  A dictionary containing information about the proxy to use within this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlsessionconfiguration/proxyconfigurations)*