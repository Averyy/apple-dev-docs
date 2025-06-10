# isCellular

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the connection operates over a cellular interface.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var isCellular: Bool { get }
```

#### Discussion

You permit or deny use of cellular interfaces with the [`allowsCellularAccess`](urlsessionconfiguration/allowscellularaccess.md) property on [`URLSessionConfiguration`](urlsessionconfiguration.md) or [`allowsCellularAccess`](urlrequest/allowscellularaccess.md) on [`URLRequest`](urlrequest.md).

## See Also

- [var networkProtocolName: String?](urlsessiontasktransactionmetrics/networkprotocolname.md)
  The network protocol used to fetch the resource.
- [var remoteAddress: String?](urlsessiontasktransactionmetrics/remoteaddress.md)
  The IP address string of the remote interface for the connection.
- [var remotePort: Int?](urlsessiontasktransactionmetrics/remoteport.md)
  The port number of the remote interface for the connection.
- [var localAddress: String?](urlsessiontasktransactionmetrics/localaddress.md)
  The IP address string of the local interface for the connection.
- [var localPort: Int?](urlsessiontasktransactionmetrics/localport.md)
  The port number of the local interface for the connection.
- [var negotiatedTLSCipherSuite: tls_ciphersuite_t?](urlsessiontasktransactionmetrics/negotiatedtlsciphersuite.md)
  The TLS cipher suite the task negotiated with the endpoint for the connection.
- [var negotiatedTLSProtocolVersion: tls_protocol_version_t?](urlsessiontasktransactionmetrics/negotiatedtlsprotocolversion.md)
  The TLS protocol version the task negotiated with the endpoint for the connection.
- [var isExpensive: Bool](urlsessiontasktransactionmetrics/isexpensive.md)
  A Boolean value that indicates whether the connection operates over an expensive interface.
- [var isConstrained: Bool](urlsessiontasktransactionmetrics/isconstrained.md)
  A Boolean value that indicates whether the connection operates over an interface marked as constrained.
- [var isProxyConnection: Bool](urlsessiontasktransactionmetrics/isproxyconnection.md)
  A Boolean value that indicastes whether the task used a proxy connection to fetch the resource.
- [var isReusedConnection: Bool](urlsessiontasktransactionmetrics/isreusedconnection.md)
  A Boolean value that indicates whether the task used a persistent connection to fetch the resource.
- [var isMultipath: Bool](urlsessiontasktransactionmetrics/ismultipath.md)
  A Boolean value that indicates whether the connection uses a successfully negotiated multipath protocol.
- [var resourceFetchType: URLSessionTaskMetrics.ResourceFetchType](urlsessiontasktransactionmetrics/resourcefetchtype.md)
  A value that indicates whether the resource was loaded, pushed, or retrieved from the local cache.
- [URLSessionTaskMetrics.ResourceFetchType](urlsessiontaskmetrics/resourcefetchtype.md)
  The manner in which a resource is fetched.
- [var domainResolutionProtocol: URLSessionTaskMetrics.DomainResolutionProtocol](urlsessiontasktransactionmetrics/domainresolutionprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontasktransactionmetrics/iscellular)*