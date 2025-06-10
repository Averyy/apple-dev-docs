# URLSessionTaskMetrics.ResourceFetchType

**Framework**: Foundation  
**Kind**: enum

The manner in which a resource is fetched.

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
enum ResourceFetchType
```

## Topics

### Fetch types
- [URLSessionTaskMetrics.ResourceFetchType.unknown](urlsessiontaskmetrics/resourcefetchtype/unknown.md)
  The manner in which the resource was fetched could not be determined.
- [URLSessionTaskMetrics.ResourceFetchType.networkLoad](urlsessiontaskmetrics/resourcefetchtype/networkload.md)
  The resource was loaded over the network.
- [URLSessionTaskMetrics.ResourceFetchType.serverPush](urlsessiontaskmetrics/resourcefetchtype/serverpush.md)
  The resource was pushed by the server to the client.
- [URLSessionTaskMetrics.ResourceFetchType.localCache](urlsessiontaskmetrics/resourcefetchtype/localcache.md)
  The resource was retrieved from the local storage.
- [URLSessionTaskMetrics.ResourceFetchType.unknown](urlsessiontaskmetrics/resourcefetchtype/unknown.md)
  The manner in which the resource was fetched could not be determined.
- [URLSessionTaskMetrics.ResourceFetchType.networkLoad](urlsessiontaskmetrics/resourcefetchtype/networkload.md)
  The resource was loaded over the network.
- [URLSessionTaskMetrics.ResourceFetchType.serverPush](urlsessiontaskmetrics/resourcefetchtype/serverpush.md)
  The resource was pushed by the server to the client.
- [URLSessionTaskMetrics.ResourceFetchType.localCache](urlsessiontaskmetrics/resourcefetchtype/localcache.md)
  The resource was retrieved from the local storage.
### Initializers
- [init?(rawValue: Int)](urlsessiontaskmetrics/resourcefetchtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [var isCellular: Bool](urlsessiontasktransactionmetrics/iscellular.md)
  A Boolean value that indicates whether the connection operates over a cellular interface.
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
- [var domainResolutionProtocol: URLSessionTaskMetrics.DomainResolutionProtocol](urlsessiontasktransactionmetrics/domainresolutionprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontaskmetrics/resourcefetchtype)*