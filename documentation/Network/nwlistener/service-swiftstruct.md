# NWListener.Service

**Framework**: Network  
**Kind**: struct

A description used to advertise the Bonjour service that a listener provides.

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
struct Service
```

## Topics

### Defining Services
- [init(name: String?, type: String, domain: String?, txtRecord: Data?)](nwlistener/service-swift.struct/init(name:type:domain:txtrecord:)-1lb30.md)
  Initializes a Bonjour service to advertise.
- [init(name: String?, type: String, domain: String?, txtRecord: NWTXTRecord)](nwlistener/service-swift.struct/init(name:type:domain:txtrecord:)-8qh5.md)
  Initializes a Bonjour service to advertise with a TXT record.
- [var noAutoRename: Bool](nwlistener/service-swift.struct/noautorename.md)
  A Boolean that indicates whether the service prohibits automatic renaming in the event of a name conflict.
### Inspecting Services
- [let name: String?](nwlistener/service-swift.struct/name.md)
  The Bonjour name of the service.
- [let type: String](nwlistener/service-swift.struct/type.md)
  The Bonjour type of the service.
- [let domain: String?](nwlistener/service-swift.struct/domain.md)
  The Bonjour domain of the service.
- [var txtRecordObject: NWTXTRecord?](nwlistener/service-swift.struct/txtrecordobject.md)
  The TXT record to advertise with the service.
- [let txtRecord: Data?](nwlistener/service-swift.struct/txtrecord.md)
  The TXT record as a raw buffer to advertise with the service.
### Initializers
- [init(applicationService: String)](nwlistener/service-swift.struct/init(applicationservice:).md)
  Creates a listener for apps that listen for connections from a network device picker.

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [NSBonjourServices](../BundleResources/Information-Property-List/NSBonjourServices.md)
  Bonjour service types browsed by the app.
- [NSLocalNetworkUsageDescription](../BundleResources/Information-Property-List/NSLocalNetworkUsageDescription.md)
  A message that tells people why the app is requesting access to the local network.
- [var service: NWListener.Service?](nwlistener/service-swift.property.md)
  A Bonjour service that advertises the listener on the local network.
- [var serviceRegistrationUpdateHandler: ((NWListener.ServiceRegistrationChange) -> Void)?](nwlistener/serviceregistrationupdatehandler.md)
  A handler that receives updates for the service endpoint being advertised.
- [NWListener.ServiceRegistrationChange](nwlistener/serviceregistrationchange.md)
  Changes to how a network listener’s service is advertised.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwlistener/service-swift.struct)*