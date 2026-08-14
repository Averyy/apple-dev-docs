# NWListener.ServiceRegistrationChange

**Framework**: Network  
**Kind**: enum

Changes to how a network listener’s service is advertised.

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
enum ServiceRegistrationChange
```

## Topics

### Changes
- [NWListener.ServiceRegistrationChange.add(_:)](nwlistener/serviceregistrationchange/add(_:).md)
  The service is now advertising a new endpoint.
- [NWListener.ServiceRegistrationChange.remove(_:)](nwlistener/serviceregistrationchange/remove(_:).md)
  The service is no longer advertising a specific endpoint.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [NSBonjourServices](../bundleresources/information-property-list/nsbonjourservices.md)
  Bonjour service types browsed by the app.
- [NSLocalNetworkUsageDescription](../bundleresources/information-property-list/nslocalnetworkusagedescription.md)
  A message that tells people why the app is requesting access to the local network.
- [var service: NWListener.Service?](nwlistener/service-swift.property.md)
  A Bonjour service that advertises the listener on the local network.
- [NWListener.Service](nwlistener/service-swift.struct.md)
  A description used to advertise the Bonjour service that a listener provides.
- [var serviceRegistrationUpdateHandler: ((NWListener.ServiceRegistrationChange) -> Void)?](nwlistener/serviceregistrationupdatehandler.md)
  A handler that receives updates for the service endpoint being advertised.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwlistener/serviceregistrationchange)*