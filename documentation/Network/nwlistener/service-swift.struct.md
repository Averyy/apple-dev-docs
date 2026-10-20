# NWListener.Service

**Framework**: Network  
**Kind**: struct  
**Role**: Structure

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
- [init(name: String?, type: String, domain: String?, txtRecord: Data?)](./service-swift.struct/init%28name,type,domain,txtrecord%29-1lb30.md)
  Initializes a Bonjour service to advertise.
- [init(name: String?, type: String, domain: String?, txtRecord: NWTXTRecord)](./service-swift.struct/init%28name,type,domain,txtrecord%29-8qh5.md)
  Initializes a Bonjour service to advertise with a TXT record.
- [var noAutoRename: Bool](./service-swift.struct/noautorename.md)
  A Boolean that indicates whether the service prohibits automatic renaming in the event of a name conflict.
### Inspecting Services
- [let name: String?](./service-swift.struct/name.md)
  The Bonjour name of the service.
- [let type: String](./service-swift.struct/type.md)
  The Bonjour type of the service.
- [let domain: String?](./service-swift.struct/domain.md)
  The Bonjour domain of the service.
- [var txtRecordObject: NWTXTRecord?](./service-swift.struct/txtrecordobject.md)
  The TXT record to advertise with the service.
- [let txtRecord: Data?](./service-swift.struct/txtrecord.md)
  The TXT record as a raw buffer to advertise with the service.
### Initializers
- [init(applicationService: String)](./service-swift.struct/init%28applicationservice%29.md)
  Creates a listener for apps that listen for connections from a network device picker.

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Advertising Bonjour Services
- [NSBonjourServices](../../BundleResources/information-property-list/nsbonjourservices.md)
  Bonjour service types browsed by the app.
- [NSLocalNetworkUsageDescription](../../BundleResources/information-property-list/nslocalnetworkusagedescription.md)
  A message that tells people why the app is requesting access to the local network.
- [var service: NWListener.Service?](./service-swift.property.md)
  A Bonjour service that advertises the listener on the local network.
- [var serviceRegistrationUpdateHandler: ((NWListener.ServiceRegistrationChange) -> Void)?](./serviceregistrationupdatehandler.md)
  A handler that receives updates for the service endpoint being advertised.
- [NWListener.ServiceRegistrationChange](./serviceregistrationchange.md)
  Changes to how a network listener’s service is advertised.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwlistener/service-swift.struct)*