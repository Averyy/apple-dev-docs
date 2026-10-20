# NetworkChannel.State

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
- [NetworkChannel.State.cancelled](./state-swift.enum/cancelled.md)
  Cancelled connections have been invalidated by the client and will send no more events
- [NetworkChannel.State.failed(_:)](./state-swift.enum/failed%28_%29.md)
- [NetworkChannel.State.preparing](./state-swift.enum/preparing.md)
  Preparing connections are actively establishing the connection
- [NetworkChannel.State.ready](./state-swift.enum/ready.md)
  Ready connections can send and receive data
- [NetworkChannel.State.setup](./state-swift.enum/setup.md)
  The initial state prior to start
- [NetworkChannel.State.waiting(_:)](./state-swift.enum/waiting%28_%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkchannel/state-swift.enum)*