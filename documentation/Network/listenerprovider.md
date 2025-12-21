# ListenerProvider

**Framework**: Network  
**Kind**: protocol

Extensible support for configuring advertise descriptors to define the service a listener should advertise.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
protocol ListenerProvider
```

#### Overview

Listeners use advertise descriptors to advertise services that can subsequently be discovered by browsers.

## Topics

### Instance Properties
- [var service: NWListener.Service](listenerprovider/service.md)
### Type Methods
- [static func bonjour(name: String?, type: String, domain: String?, txtRecord: NWTXTRecord?) -> BonjourListenerProvider](listenerprovider/bonjour(name:type:domain:txtrecord:).md)
  Create a Bonjour service to advertise.
- [static func wifiAware(WAPublisherListener.Action, active: Duration?) -> Self](listenerprovider/wifiaware(_:active:).md)
  Sets a network listener to publish Wi-Fi Aware services to the selected paired devices.

## Relationships

### Conforming Types
- [BonjourListenerProvider](bonjourlistenerprovider.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/listenerprovider)*