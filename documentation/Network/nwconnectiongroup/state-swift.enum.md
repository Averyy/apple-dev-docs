# NWConnectionGroup.State

**Framework**: Network  
**Kind**: enum  
**Role**: Enumeration

States that indicate whether you can use a connection group to send and receive messages.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
enum State
```

## Topics

### States
- [NWConnectionGroup.State.setup](./state-swift.enum/setup.md)
  You have not yet started the connection group.
- [NWConnectionGroup.State.waiting(_:)](./state-swift.enum/waiting%28_%29.md)
  The connection group is waiting for a network path change.
- [NWConnectionGroup.State.ready](./state-swift.enum/ready.md)
  The connection group is joined, and ready to send and receive data.
- [NWConnectionGroup.State.failed(_:)](./state-swift.enum/failed%28_%29.md)
  The connection group encountered a fatal error.
- [NWConnectionGroup.State.cancelled](./state-swift.enum/cancelled.md)
  The connection group has been canceled.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing Groups
- [var stateUpdateHandler: ((NWConnectionGroup.State) -> Void)?](./stateupdatehandler.md)
  A handler that receives connection group state updates.
- [var state: NWConnectionGroup.State](./state-swift.property.md)
  The current state of the connection group.
- [func cancel()](./cancel%28%29.md)
  Cancels the connection group object and leaves the network group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnectiongroup/state-swift.enum)*