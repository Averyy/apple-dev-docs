# NWConnectionGroup.State

**Framework**: Network  
**Kind**: enum

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
- [NWConnectionGroup.State.setup](nwconnectiongroup/state-swift.enum/setup.md)
  You have not yet started the connection group.
- [NWConnectionGroup.State.waiting(_:)](nwconnectiongroup/state-swift.enum/waiting(_:).md)
  The connection group is waiting for a network path change.
- [NWConnectionGroup.State.ready](nwconnectiongroup/state-swift.enum/ready.md)
  The connection group is joined, and ready to send and receive data.
- [NWConnectionGroup.State.failed(_:)](nwconnectiongroup/state-swift.enum/failed(_:).md)
  The connection group encountered a fatal error.
- [NWConnectionGroup.State.cancelled](nwconnectiongroup/state-swift.enum/cancelled.md)
  The connection group has been canceled.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var stateUpdateHandler: ((NWConnectionGroup.State) -> Void)?](nwconnectiongroup/stateupdatehandler.md)
  A handler that receives connection group state updates.
- [var state: NWConnectionGroup.State](nwconnectiongroup/state-swift.property.md)
  The current state of the connection group.
- [func cancel()](nwconnectiongroup/cancel.md)
  Cancels the connection group object and leaves the network group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnectiongroup/state-swift.enum)*