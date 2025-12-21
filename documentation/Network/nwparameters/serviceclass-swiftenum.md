# NWParameters.ServiceClass

**Framework**: Network  
**Kind**: enum

Indicates how the system prioritizes transmitted traffic by your latency and throughput needs.

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
enum ServiceClass
```

#### Overview

Use `ServiceClass` to tell the system and compatible networks how to handle your outgoing packets on Wi-Fi, Ethernet, or cellular. You describe whether your traffic favors low latency or high throughput. It prioritizes data packets transmitted on an underlying transport according to the throughput and latency characteristics of the use case. `ServiceClass` doesn’t necessarily affect the priority of packets received from a data transport, which may be set by the network. The default [`NWParameters.ServiceClass.bestEffort`](nwparameters/serviceclass-swift.enum/besteffort.md) category should be used when their isn’t a specific need or test results that indicates another service class would be helpful.

For more information on using `ServiceClass` with Wi-Fi Aware, refer to [`WAAccessCategory`](https://developer.apple.com/documentation/WiFiAware/WAAccessCategory).

## Topics

### Service Classes
- [NWParameters.ServiceClass.bestEffort](nwparameters/serviceclass-swift.enum/besteffort.md)
  The default service type.
- [NWParameters.ServiceClass.background](nwparameters/serviceclass-swift.enum/background.md)
  A service type for high-delay tolerant, high-loss tolerant, elastic flow, and variable size connections.
- [NWParameters.ServiceClass.interactiveVideo](nwparameters/serviceclass-swift.enum/interactivevideo.md)
  A service type for low-delay tolerant, very low-loss tolerant, inelastic flow, and constant packet rate connections.
- [NWParameters.ServiceClass.interactiveVoice](nwparameters/serviceclass-swift.enum/interactivevoice.md)
  A service type for low-delay tolerant, very low-loss tolerant, inelastic flow, and constant packet rate connections.
- [NWParameters.ServiceClass.responsiveData](nwparameters/serviceclass-swift.enum/responsivedata.md)
  A service type for medium-delay tolerant, inelastic flow, and bursty connections.
- [NWParameters.ServiceClass.signaling](nwparameters/serviceclass-swift.enum/signaling.md)
  A service type for low-loss tolerant, inelastic flow, jitter tolerant, bursty but short rate, and variable size connections.

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
- [NWParameters.MultipathServiceType](nwparameters/multipathservicetype-swift.enum.md)
  Modes in which a connection can support multipath protocols.
- [var serviceClass: NWParameters.ServiceClass](nwparameters/serviceclass-swift.property.md)
  The traffic characteristics network connections send and receive.
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

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparameters/serviceclass-swift.enum)*