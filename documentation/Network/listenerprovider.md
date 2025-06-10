# ListenerProvider

**Framework**: Network  
**Kind**: protocol

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
protocol ListenerProvider
```

## Topics

### Instance Properties
- [var isApplicationService: Bool](listenerprovider/isapplicationservice.md)
- [var service: NWListener.Service](listenerprovider/service.md)
### Instance Methods
- [func configureParameters(NWParameters)](listenerprovider/configureparameters(_:).md)
### Type Methods
- [static func bonjour(name: String?, type: String, domain: String?, metadata: NWTXTRecord?, port: NWEndpoint.Port?) -> BonjourListenerProvider](listenerprovider/bonjour(name:type:domain:metadata:port:).md)
- [static func bonjour(name: String?, type: String, domain: String?, port: NWEndpoint.Port?) -> BonjourListenerProvider](listenerprovider/bonjour(name:type:domain:port:).md)
- [static func wifiAware(WAPublisherListener.Action, active: Duration?) -> Self](listenerprovider/wifiaware(_:active:).md)
  Sets a `NetworkListener` to publish Wi-Fi Aware services to the selected paired devices.

## Relationships

### Conforming Types
- [BonjourListenerProvider](bonjourlistenerprovider.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/listenerprovider)*