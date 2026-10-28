# port

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property

The port on which the listener can accept connections.

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
final var port: NWEndpoint.Port? { get }
```

## Discussion

The listener’s port is available once the listener is in the ready state.

## See Also

### Creating Listeners
- [init(using: NWParameters, on: NWEndpoint.Port) throws](./init%28using,on%29.md)
  Initializes a network listener, with an optional local port.
- [func start(queue: DispatchQueue)](./start%28queue%29.md)
  Registers for listening, and sets the queue on which all listener events are delivered.
- [var stateUpdateHandler: ((NWListener.State) -> Void)?](./stateupdatehandler.md)
  A handler that receives listener state updates.
- [NWListener.State](./state-swift.enum.md)
  States indicating whether a listener is able to accept incoming connections.
- [func cancel()](./cancel%28%29.md)
  Stops listening for inbound connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwlistener/port)*