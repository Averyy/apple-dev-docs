# NWListener.State

**Framework**: Network  
**Kind**: enum

States indicating whether a listener is able to accept incoming connections.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
enum State
```

## Topics

### States
- [NWListener.State.setup](nwlistener/state-swift.enum/setup.md)
  The listener has been initialized but not started.
- [NWListener.State.waiting(_:)](nwlistener/state-swift.enum/waiting(_:).md)
  The listener is waiting for a network to become available.
- [NWListener.State.ready](nwlistener/state-swift.enum/ready.md)
  The listener is running and able to receive incoming connections.
- [NWListener.State.failed(_:)](nwlistener/state-swift.enum/failed(_:).md)
  The listener has encountered a fatal error.
- [NWListener.State.cancelled](nwlistener/state-swift.enum/cancelled.md)
  The listener has been canceled.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [init(using: NWParameters, on: NWEndpoint.Port) throws](nwlistener/init(using:on:).md)
  Initializes a network listener, with an optional local port.
- [func start(queue: DispatchQueue)](nwlistener/start(queue:).md)
  Registers for listening, and sets the queue on which all listener events are delivered.
- [var stateUpdateHandler: ((NWListener.State) -> Void)?](nwlistener/stateupdatehandler.md)
  A handler that receives listener state updates.
- [var port: NWEndpoint.Port?](nwlistener/port.md)
  The port on which the listener can accept connections.
- [func cancel()](nwlistener/cancel.md)
  Stops listening for inbound connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwlistener/state-swift.enum)*