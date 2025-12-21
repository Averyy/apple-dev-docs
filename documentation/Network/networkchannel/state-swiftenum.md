# NetworkChannel.State

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
- [NetworkChannel.State.cancelled](networkchannel/state-swift.enum/cancelled.md)
  Cancelled connections have been invalidated by the client and will send no more events
- [NetworkChannel.State.failed(_:)](networkchannel/state-swift.enum/failed(_:).md)
  Failed connections are disconnected and can no longer send or receive data
- [NetworkChannel.State.preparing](networkchannel/state-swift.enum/preparing.md)
  Preparing connections are actively establishing the connection
- [NetworkChannel.State.ready](networkchannel/state-swift.enum/ready.md)
  Ready connections can send and receive data
- [NetworkChannel.State.setup](networkchannel/state-swift.enum/setup.md)
  The initial state prior to start
- [NetworkChannel.State.waiting(_:)](networkchannel/state-swift.enum/waiting(_:).md)
  Waiting connections have not yet been started, or do not have a viable network

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkchannel/state-swift.enum)*