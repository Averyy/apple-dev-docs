# NetworkListener.State

**Framework**: Network  
**Kind**: enum  
**Role**: Enumeration

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
enum State
```

## Topics

### Enumeration Cases
- [NetworkListener.State.cancelled](./state/cancelled.md)
  Cancelled listeners have been invalidated by the client and will send no more events
- [NetworkListener.State.failed(_:)](./state/failed%28_%29.md)
  Failed listeners are no longer able to receive incoming connections
- [NetworkListener.State.ready](./state/ready.md)
  Ready listeners are able to receive incoming connections Bonjour service may not yet be registered
- [NetworkListener.State.setup](./state/setup.md)
  Prior to start, the listener will be in the setup state
- [NetworkListener.State.waiting(_:)](./state/waiting%28_%29.md)
  Waiting listeners do not have a viable network

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networklistener/state)*