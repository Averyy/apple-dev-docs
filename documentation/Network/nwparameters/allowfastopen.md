# allowFastOpen

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property

A Boolean that enables sending application data with protocol handshakes.

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
final var allowFastOpen: Bool { get set }
```

## Discussion

When fast open is enabled on a connection, the application is expected to send its early data to be included with the handshake as idempotent data. This data can be sent before or after calling start.

## See Also

### Related Documentation
- [NWConnection.SendCompletion.idempotent](../nwconnection/sendcompletion/idempotent.md)
  Mark the sent data as idempotent—data that can be sent multiple times.
### Customizing Connection Options
- [var multipathServiceType: NWParameters.MultipathServiceType](./multipathservicetype-swift.property.md)
  An option to allow connections to use multipath protocols.
- [NWParameters.MultipathServiceType](./multipathservicetype-swift.enum.md)
  Modes in which a connection can support multipath protocols.
- [var serviceClass: NWParameters.ServiceClass](./serviceclass-swift.property.md)
  The traffic characteristics network connections send and receive.
- [NWParameters.ServiceClass](./serviceclass-swift.enum.md)
  Indicates how the system prioritizes transmitted traffic by your latency and throughput needs.
- [var expiredDNSBehavior: NWParameters.ExpiredDNSBehavior](./expireddnsbehavior-swift.property.md)
  A behavior that defines how expired DNS answers will be used.
- [NWParameters.ExpiredDNSBehavior](./expireddnsbehavior-swift.enum.md)
  Options for configuring how expired DNS answers should be used.
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

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparameters/allowfastopen)*