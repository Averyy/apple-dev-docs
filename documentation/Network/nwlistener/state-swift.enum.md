# NWListener.State

**Framework**: Network  
**Kind**: enum  
**Role**: Enumeration

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
- [NWListener.State.setup](./state-swift.enum/setup.md)
  The listener has been initialized but not started.
- [NWListener.State.waiting(_:)](./state-swift.enum/waiting%28_%29.md)
  The listener is waiting for a network to become available.
- [NWListener.State.ready](./state-swift.enum/ready.md)
  The listener is running and able to receive incoming connections.
- [NWListener.State.failed(_:)](./state-swift.enum/failed%28_%29.md)
  The listener has encountered a fatal error.
- [NWListener.State.cancelled](./state-swift.enum/cancelled.md)
  The listener has been canceled.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating Listeners
- [init(using: NWParameters, on: NWEndpoint.Port) throws](./init%28using,on%29.md)
  Initializes a network listener, with an optional local port.
- [func start(queue: DispatchQueue)](./start%28queue%29.md)
  Registers for listening, and sets the queue on which all listener events are delivered.
- [var stateUpdateHandler: ((NWListener.State) -> Void)?](./stateupdatehandler.md)
  A handler that receives listener state updates.
- [var port: NWEndpoint.Port?](./port.md)
  The port on which the listener can accept connections.
- [func cancel()](./cancel%28%29.md)
  Stops listening for inbound connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwlistener/state-swift.enum)*