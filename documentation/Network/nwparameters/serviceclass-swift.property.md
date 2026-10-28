# serviceClass

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property

The traffic characteristics network connections send and receive.

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
final var serviceClass: NWParameters.ServiceClass { get set }
```

## Discussion

The `serviceClass` you use tells the system and compatible networks how to prioritize transmitted packets on Wi-Fi, Ethernet, or cellular for a given connection. Describe whether your traffic favors low latency (for immediacy), or high throughput (for bulk transfers), and the transport may schedule your outgoing packets to reflect that tradeoff.

Use [`NWParameters.ServiceClass.bestEffort`](./serviceclass-swift.enum/besteffort.md) by default. Choose a different class only when you have a specific requirement or measurement showing that another choice improves your results on the networks your app uses.

Certain cellular networks also offer Network Slicing, which can use `serviceClass` to isolate traffic based on its expected characteristics.

## Enabling Network Slicing

There are two steps to enable Cellular Network Slicing:

- Set the entitlements in your property list for [`5G Network Slicing App Category`](../../BundleResources/entitlements/com.apple.developer.networking.slicing.appcategory.md) and [`5G Network Slicing Traffic Category`](../../BundleResources/entitlements/com.apple.developer.networking.slicing.trafficcategory.md). If you don’t entitle your app by specifying both these entitlements, your apps network connections won’t be using Cellular Network Slicing, even if supported by the carrier.
- Set this to the appropriate [`NWParameters.ServiceClass`](./serviceclass-swift.enum.md).

## See Also

### Customizing Connection Options
- [var multipathServiceType: NWParameters.MultipathServiceType](./multipathservicetype-swift.property.md)
  An option to allow connections to use multipath protocols.
- [NWParameters.MultipathServiceType](./multipathservicetype-swift.enum.md)
  Modes in which a connection can support multipath protocols.
- [NWParameters.ServiceClass](./serviceclass-swift.enum.md)
  Indicates how the system prioritizes transmitted traffic by your latency and throughput needs.
- [var allowFastOpen: Bool](./allowfastopen.md)
  A Boolean that enables sending application data with protocol handshakes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparameters/serviceclass-swift.property)*