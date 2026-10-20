# service

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property

A Bonjour service that advertises the listener on the local network.

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
final var service: NWListener.Service? { get set }
```

## See Also

### Advertising Bonjour Services
- [NSBonjourServices](../../BundleResources/information-property-list/nsbonjourservices.md)
  Bonjour service types browsed by the app.
- [NSLocalNetworkUsageDescription](../../BundleResources/information-property-list/nslocalnetworkusagedescription.md)
  A message that tells people why the app is requesting access to the local network.
- [NWListener.Service](./service-swift.struct.md)
  A description used to advertise the Bonjour service that a listener provides.
- [var serviceRegistrationUpdateHandler: ((NWListener.ServiceRegistrationChange) -> Void)?](./serviceregistrationupdatehandler.md)
  A handler that receives updates for the service endpoint being advertised.
- [NWListener.ServiceRegistrationChange](./serviceregistrationchange.md)
  Changes to how a network listener’s service is advertised.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwlistener/service-swift.property)*