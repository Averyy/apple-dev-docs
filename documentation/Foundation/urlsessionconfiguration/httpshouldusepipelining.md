# httpShouldUsePipelining

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the session should use HTTP pipelining.

**Availability**:
- iOS 7.0+ - Deprecated in 18.4
- iPadOS 7.0+ - Deprecated in 18.4
- Mac Catalyst 13.1+ - Deprecated in 18.4
- macOS 10.9+ - Deprecated in 15.4
- tvOS 9.0+ - Deprecated in 18.4
- visionOS 1.0+ - Deprecated in 2.4
- watchOS 2.0+ - Deprecated in 11.4

> **Deprecated**: Pipelining is an HTTP/1.1 concept. Adopt HTTP/2 or later instead.

## Declaration

```swift
var httpShouldUsePipelining: Bool { get set }
```

```objc
@property BOOL HTTPShouldUsePipelining;
```

## Discussion

This property determines whether tasks within sessions based on this configuration should use HTTP pipelining. You can also enable pipelining on a per-task basis by creating the task with an [`NSURLRequest`](../nsurlrequest.md) object.

The default value is [`false`](../../Swift/false.md).

HTTP/2 and later ignore this property. HTTP/1.1 only considers this property in the classic loading mode ([`usesClassicLoadingMode`](./usesclassicloadingmode.md)).

## See Also

### Setting HTTP policy and proxy properties
- [var httpMaximumConnectionsPerHost: Int](./httpmaximumconnectionsperhost.md)
  The maximum number of simultaneous HTTP/1.1 connections to make to a given host.
- [var proxyConfigurations: [ProxyConfiguration]](./proxyconfigurations.md)
  An array of proxy configuration objects containing information about the proxies to use within this session.
- [var connectionProxyDictionary: [AnyHashable : Any]?](./connectionproxydictionary.md)
  A dictionary containing information about the proxy to use within this session.
- [proxyConfigurations](../nsurlsessionconfiguration/proxyconfigurations.md)
  An array of proxy configuration objects containing information about the proxies to use within this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/httpshouldusepipelining)*