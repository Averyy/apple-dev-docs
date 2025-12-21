# NWParameters.MultipathServiceType

**Framework**: Network  
**Kind**: enum

Modes in which a connection can support multipath protocols.

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
enum MultipathServiceType
```

## Topics

### Multipath Service Types
- [NWParameters.MultipathServiceType.disabled](nwparameters/multipathservicetype-swift.enum/disabled.md)
  Disable multipath.
- [NWParameters.MultipathServiceType.handover](nwparameters/multipathservicetype-swift.enum/handover.md)
  Enable multipath, but only use other interfaces when the primary interface is lost.
- [NWParameters.MultipathServiceType.interactive](nwparameters/multipathservicetype-swift.enum/interactive.md)
  Enable multipath to use other interfaces when the primary interface encounters loss or delay.
- [NWParameters.MultipathServiceType.aggregate](nwparameters/multipathservicetype-swift.enum/aggregate.md)
  Enable multipath to maximize bandwidth across multiple interfaces.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var multipathServiceType: NWParameters.MultipathServiceType](nwparameters/multipathservicetype-swift.property.md)
  An option to allow connections to use multipath protocols.
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
- [var preferNoProxies: Bool](nwparameters/prefernoproxies.md)
  A Boolean that indicates that connections should ignore proxies when they are enabled on the system.
- [var includePeerToPeer: Bool](nwparameters/includepeertopeer.md)
  A Boolean that enables peer-to-peer link technologies for connections and listeners.
- [var allowLocalEndpointReuse: Bool](nwparameters/allowlocalendpointreuse.md)
  A Boolean that allows reusing local addresses and ports across connections.
- [var acceptLocalOnly: Bool](nwparameters/acceptlocalonly.md)
  A Boolean that restricts listeners to only accepting connections from the local link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparameters/multipathservicetype-swift.enum)*