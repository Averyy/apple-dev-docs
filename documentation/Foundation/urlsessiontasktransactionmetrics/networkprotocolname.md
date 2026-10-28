# networkProtocolName

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The network protocol used to fetch the resource.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var networkProtocolName: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * networkProtocolName;
```

## Discussion

When a proxy is configured and a tunnel connection is established, this attribute returns the value for the tunneled protocol, which is identified by the ALPN Protocol ID Identification Sequence, as per [RFC 7310](https://tools.ietf.org/html/rfc7301). For example:

- If no proxy is used, and HTTP/2 is negotiated, then `h2` is returned.
- If HTTP/1.1 is used with the proxy, and the tunneled connection is HTTP/2, then `h2` is returned.
- If HTTP/1.1 is used with the proxy, and there’s no tunnel, then `http/1.1` is returned.

## See Also

### Accessing transaction characteristics
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
- [var isExpensive: Bool](./isexpensive.md)
  A Boolean value that indicates whether the connection operates over an expensive interface.
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
- [remotePort](../nsurlsessiontasktransactionmetrics/remoteport.md)
  The port number of the remote interface for the connection.
- [localPort](../nsurlsessiontasktransactionmetrics/localport.md)
  The port number of the local interface for the connection.
- [negotiatedTLSCipherSuite](../nsurlsessiontasktransactionmetrics/negotiatedtlsciphersuite.md)
  The TLS cipher suite the task negotiated with the endpoint for the connection.
- [negotiatedTLSProtocolVersion](../nsurlsessiontasktransactionmetrics/negotiatedtlsprotocolversion.md)
  The TLS protocol version the task negotiated with the endpoint for the connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontasktransactionmetrics/networkprotocolname)*