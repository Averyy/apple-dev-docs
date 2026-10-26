# URLSessionTaskMetrics.DomainResolutionProtocol

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
enum DomainResolutionProtocol
```

```c
enum NSURLSessionTaskMetricsDomainResolutionProtocol : NSInteger;
```

## Topics

### Enumeration Cases
- [URLSessionTaskMetrics.DomainResolutionProtocol.https](./domainresolutionprotocol/https.md)
- [URLSessionTaskMetrics.DomainResolutionProtocol.tcp](./domainresolutionprotocol/tcp.md)
- [URLSessionTaskMetrics.DomainResolutionProtocol.tls](./domainresolutionprotocol/tls.md)
- [URLSessionTaskMetrics.DomainResolutionProtocol.udp](./domainresolutionprotocol/udp.md)
- [URLSessionTaskMetrics.DomainResolutionProtocol.unknown](./domainresolutionprotocol/unknown.md)
### Initializers
- [init?(rawValue: Int)](./domainresolutionprotocol/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing transaction characteristics
- [var networkProtocolName: String?](../urlsessiontasktransactionmetrics/networkprotocolname.md)
  The network protocol used to fetch the resource.
- [var remoteAddress: String?](../urlsessiontasktransactionmetrics/remoteaddress.md)
  The IP address string of the remote interface for the connection.
- [var remotePort: Int?](../urlsessiontasktransactionmetrics/remoteport.md)
  The port number of the remote interface for the connection.
- [var localAddress: String?](../urlsessiontasktransactionmetrics/localaddress.md)
  The IP address string of the local interface for the connection.
- [var localPort: Int?](../urlsessiontasktransactionmetrics/localport.md)
  The port number of the local interface for the connection.
- [var negotiatedTLSCipherSuite: tls_ciphersuite_t?](../urlsessiontasktransactionmetrics/negotiatedtlsciphersuite.md)
  The TLS cipher suite the task negotiated with the endpoint for the connection.
- [var negotiatedTLSProtocolVersion: tls_protocol_version_t?](../urlsessiontasktransactionmetrics/negotiatedtlsprotocolversion.md)
  The TLS protocol version the task negotiated with the endpoint for the connection.
- [var isCellular: Bool](../urlsessiontasktransactionmetrics/iscellular.md)
  A Boolean value that indicates whether the connection operates over a cellular interface.
- [var isExpensive: Bool](../urlsessiontasktransactionmetrics/isexpensive.md)
  A Boolean value that indicates whether the connection operates over an expensive interface.
- [var isConstrained: Bool](../urlsessiontasktransactionmetrics/isconstrained.md)
  A Boolean value that indicates whether the connection operates over an interface marked as constrained.
- [var isProxyConnection: Bool](../urlsessiontasktransactionmetrics/isproxyconnection.md)
  A Boolean value that indicastes whether the task used a proxy connection to fetch the resource.
- [var isReusedConnection: Bool](../urlsessiontasktransactionmetrics/isreusedconnection.md)
  A Boolean value that indicates whether the task used a persistent connection to fetch the resource.
- [var isMultipath: Bool](../urlsessiontasktransactionmetrics/ismultipath.md)
  A Boolean value that indicates whether the connection uses a successfully negotiated multipath protocol.
- [var resourceFetchType: URLSessionTaskMetrics.ResourceFetchType](../urlsessiontasktransactionmetrics/resourcefetchtype.md)
  A value that indicates whether the resource was loaded, pushed, or retrieved from the local cache.
- [URLSessionTaskMetrics.ResourceFetchType](./resourcefetchtype.md)
  The manner in which a resource is fetched.
- [remotePort](../nsurlsessiontasktransactionmetrics/remoteport.md)
  The port number of the remote interface for the connection.
- [localPort](../nsurlsessiontasktransactionmetrics/localport.md)
  The port number of the local interface for the connection.
- [negotiatedTLSCipherSuite](../nsurlsessiontasktransactionmetrics/negotiatedtlsciphersuite.md)
  The TLS cipher suite the task negotiated with the endpoint for the connection.
- [negotiatedTLSProtocolVersion](../nsurlsessiontasktransactionmetrics/negotiatedtlsprotocolversion.md)
  The TLS protocol version the task negotiated with the endpoint for the connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontaskmetrics/domainresolutionprotocol)*