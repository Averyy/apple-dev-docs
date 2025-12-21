# preferNoProxies

**Framework**: Network  
**Kind**: property

A Boolean that indicates that connections should ignore proxies when they are enabled on the system.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
final var preferNoProxies: Bool { get set }
```

## See Also

- [var multipathServiceType: NWParameters.MultipathServiceType](nwparameters/multipathservicetype-swift.property.md)
  An option to allow connections to use multipath protocols.
- [NWParameters.MultipathServiceType](nwparameters/multipathservicetype-swift.enum.md)
  Modes in which a connection can support multipath protocols.
- [var serviceClass: NWParameters.ServiceClass](nwparameters/serviceclass-swift.property.md)
  The traffic characteristics network connections send and receive.
- [NWParameters.ServiceClass](nwparameters/serviceclass-swift.enum.md)
  Indicates how the system prioritizes transmitted traffic by your latency and throughput needs.
- [var allowFastOpen: Bool](nwparameters/allowfastopen.md)
  A Boolean that enables sending application data with protocol handshakes.
- [var expiredDNSBehavior: NWParameters.ExpiredDNSBehavior](nwparameters/expireddnsbehavior-swift.property.md)
  A behavior that defines how expired DNS answers will be used.
- [NWParameters.ExpiredDNSBehavior](nwparameters/expireddnsbehavior-swift.enum.md)
  Options for configuring how expired DNS answers should be used.
- [var requiresDNSSECValidation: Bool](nwparameters/requiresdnssecvalidation.md)
  A Boolean value that determines whether a connection requires DNSSEC validation when resolving endpoints.
- [var includePeerToPeer: Bool](nwparameters/includepeertopeer.md)
  A Boolean that enables peer-to-peer link technologies for connections and listeners.
- [var allowLocalEndpointReuse: Bool](nwparameters/allowlocalendpointreuse.md)
  A Boolean that allows reusing local addresses and ports across connections.
- [var acceptLocalOnly: Bool](nwparameters/acceptlocalonly.md)
  A Boolean that restricts listeners to only accepting connections from the local link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparameters/prefernoproxies)*