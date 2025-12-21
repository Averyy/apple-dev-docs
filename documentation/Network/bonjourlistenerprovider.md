# BonjourListenerProvider

**Framework**: Network  
**Kind**: struct

Advertise a Bonjour service.

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
struct BonjourListenerProvider
```

## Topics

### Initializers
- [init(name: String?, type: String, domain: String?, txtRecord: NWTXTRecord?)](bonjourlistenerprovider/init(name:type:domain:txtrecord:).md)
  Create a Bonjour service to advertise.
### Instance Properties
- [var service: NWListener.Service](bonjourlistenerprovider/service.md)
  The service advertised by the listener.

## Relationships

### Conforms To
- [ListenerProvider](listenerprovider.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/bonjourlistenerprovider)*