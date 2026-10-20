# NWEthernetChannel.State

**Framework**: Network  
**Kind**: enum  
**Role**: Enumeration

States indicating whether an Ethernet channel is able to send and receive frames.

**Availability**:
- macOS 10.15+

## Declaration

```swift
enum State
```

## Topics

### States
- [NWEthernetChannel.State.setup](./state-swift.enum/setup.md)
  The channel has been initialized but not started.
- [NWEthernetChannel.State.waiting(_:)](./state-swift.enum/waiting%28_%29.md)
  The channel is waiting for its interface to become available.
- [NWEthernetChannel.State.preparing](./state-swift.enum/preparing.md)
  The channel is registering with the interface.
- [NWEthernetChannel.State.ready](./state-swift.enum/ready.md)
  The channel is able to send and receive Ethernet frames.
- [NWEthernetChannel.State.failed(_:)](./state-swift.enum/failed%28_%29.md)
  The channel has encountered a fatal error.
- [NWEthernetChannel.State.cancelled](./state-swift.enum/cancelled.md)
  The channel has been canceled.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Handling State Updates
- [var state: NWEthernetChannel.State](./state-swift.property.md)
  The current state of the channel.
- [var stateUpdateHandler: ((NWEthernetChannel.State) -> Void)?](./stateupdatehandler.md)
  A handler that delivers channel state updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwethernetchannel/state-swift.enum)*