# isExpensive

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the connection operates over an expensive interface.

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
var isExpensive: Bool { get }
```

```objc
@property (readonly, getter=isExpensive) BOOL expensive;
```

#### Discussion

The system considers an interface expensive if it’s more costly or consumes more power, such as 3G or LTE as compared to ethernet or Wi-Fi. You permit or deny use of expensive interfaces with the [`allowsExpensiveNetworkAccess`](../urlsessionconfiguration/allowsexpensivenetworkaccess.md) property on [`URLSessionConfiguration`](../urlsessionconfiguration.md) or [`allowsExpensiveNetworkAccess`](../urlrequest/allowsexpensivenetworkaccess.md) on [`URLRequest`](../urlrequest.md).

## See Also

### Accessing transaction characteristics
- [var networkProtocolName: String?](./networkprotocolname.md)
  The network protocol used to fetch the resource.
- [var remoteAddress: String?](./remoteaddress.md)
  The IP address string of the remote interface for the connection.
- [var remotePort: Int?](./remoteport.md)
  The port number of the remote interface for the connection.
- [var localAddress: String?](./localaddress.md)
  The IP address string of the local interface for the connection.
- [var localPort: Int?](./localport.md)
  The port number of the local interface for the connection.
- [var negotiatedTLSCipherSuite: tls_ciphersuite_t?](./negotiatedtlsciphersuite.md)
  The TLS cipher suite the task negotiated with the endpoint for the connection.
- [var negotiatedTLSProtocolVersion: tls_protocol_version_t?](./negotiatedtlsprotocolversion.md)
  The TLS protocol version the task negotiated with the endpoint for the connection.
- [var isCellular: Bool](./iscellular.md)
  A Boolean value that indicates whether the connection operates over a cellular interface.
- [var isConstrained: Bool](./isconstrained.md)
  A Boolean value that indicates whether the connection operates over an interface marked as constrained.
- [var isProxyConnection: Bool](./isproxyconnection.md)
  A Boolean value that indicastes whether the task used a proxy connection to fetch the resource.
- [var isReusedConnection: Bool](./isreusedconnection.md)
  A Boolean value that indicates whether the task used a persistent connection to fetch the resource.
- [var isMultipath: Bool](./ismultipath.md)
  A Boolean value that indicates whether the connection uses a successfully negotiated multipath protocol.
- [var resourceFetchType: URLSessionTaskMetrics.ResourceFetchType](./resourcefetchtype.md)
  A value that indicates whether the resource was loaded, pushed, or retrieved from the local cache.
- [URLSessionTaskMetrics.ResourceFetchType](../urlsessiontaskmetrics/resourcefetchtype.md)
  The manner in which a resource is fetched.
- [var domainResolutionProtocol: URLSessionTaskMetrics.DomainResolutionProtocol](./domainresolutionprotocol.md)
  DNS protocol used for domain resolution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontasktransactionmetrics/isexpensive)*