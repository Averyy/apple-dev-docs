# NetworkListener.State

**Framework**: Network  
**Kind**: enum

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
- [NetworkListener.State.cancelled](networklistener/state/cancelled.md)
  Cancelled listeners have been invalidated by the client and will send no more events
- [NetworkListener.State.failed(_:)](networklistener/state/failed(_:).md)
  Failed listeners are no longer able to receive incoming connections
- [NetworkListener.State.ready](networklistener/state/ready.md)
  Ready listeners are able to receive incoming connections Bonjour service may not yet be registered
- [NetworkListener.State.setup](networklistener/state/setup.md)
  Prior to start, the listener will be in the setup state
- [NetworkListener.State.waiting(_:)](networklistener/state/waiting(_:).md)
  Waiting listeners do not have a viable network

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networklistener/state)*