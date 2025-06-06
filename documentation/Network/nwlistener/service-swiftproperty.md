# service

**Framework**: Network  
**Kind**: property

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

- [NSBonjourServices](../BundleResources/Information-Property-List/NSBonjourServices.md)
  Bonjour service types browsed by the app.
- [NSLocalNetworkUsageDescription](../BundleResources/Information-Property-List/NSLocalNetworkUsageDescription.md)
  A message that tells the user why the app is requesting access to the local network.
- [NWListener.Service](nwlistener/service-swift.struct.md)
  A description used to advertise the Bonjour service that a listener provides.
- [var serviceRegistrationUpdateHandler: ((NWListener.ServiceRegistrationChange) -> Void)?](nwlistener/serviceregistrationupdatehandler.md)
  A handler that receives updates for the service endpoint being advertised.
- [NWListener.ServiceRegistrationChange](nwlistener/serviceregistrationchange.md)
  Changes to how a network listener’s service is advertised.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwlistener/service-swift.property)*