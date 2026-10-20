# NWParameters.ExpiredDNSBehavior

**Framework**: Network  
**Kind**: enum  
**Role**: Enumeration

Options for configuring how expired DNS answers should be used.

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
enum ExpiredDNSBehavior
```

## Topics

### Behaviors
- [NWParameters.ExpiredDNSBehavior.systemDefault](./expireddnsbehavior-swift.enum/systemdefault.md)
  Let the system determine whether or not to allow expired DNS answers.
- [NWParameters.ExpiredDNSBehavior.allow](./expireddnsbehavior-swift.enum/allow.md)
  Explicitly allow the use of expired DNS answers.
- [NWParameters.ExpiredDNSBehavior.prohibit](./expireddnsbehavior-swift.enum/prohibit.md)
  Explicitly prohibit the use of expired DNS answers.
### Enumeration Cases
- [NWParameters.ExpiredDNSBehavior.persistent](./expireddnsbehavior-swift.enum/persistent.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Customizing Connection Options
- [var multipathServiceType: NWParameters.MultipathServiceType](./multipathservicetype-swift.property.md)
  An option to allow connections to use multipath protocols.
- [NWParameters.MultipathServiceType](./multipathservicetype-swift.enum.md)
  Modes in which a connection can support multipath protocols.
- [var serviceClass: NWParameters.ServiceClass](./serviceclass-swift.property.md)
  The traffic characteristics network connections send and receive.
- [NWParameters.ServiceClass](./serviceclass-swift.enum.md)
  Indicates how the system prioritizes transmitted traffic by your latency and throughput needs.
- [var allowFastOpen: Bool](./allowfastopen.md)
  A Boolean that enables sending application data with protocol handshakes.
- [var expiredDNSBehavior: NWParameters.ExpiredDNSBehavior](./expireddnsbehavior-swift.property.md)
  A behavior that defines how expired DNS answers will be used.
- [var requiresDNSSECValidation: Bool](./requiresdnssecvalidation.md)
  A Boolean value that determines whether a connection requires DNSSEC validation when resolving endpoints.
- [var preferNoProxies: Bool](./prefernoproxies.md)
  A Boolean that indicates that connections should ignore proxies when they are enabled on the system.
- [var includePeerToPeer: Bool](./includepeertopeer.md)
  A Boolean that enables peer-to-peer link technologies for connections and listeners.
- [var allowLocalEndpointReuse: Bool](./allowlocalendpointreuse.md)
  A Boolean that allows reusing local addresses and ports across connections.
- [var acceptLocalOnly: Bool](./acceptlocalonly.md)
  A Boolean that restricts listeners to only accepting connections from the local link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparameters/expireddnsbehavior-swift.enum)*