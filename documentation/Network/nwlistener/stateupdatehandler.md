# stateUpdateHandler

**Framework**: Network  
**Kind**: property

A handler that receives listener state updates.

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
@preconcurrency
final var stateUpdateHandler: ((NWListener.State) -> Void)? { get set }
```

## See Also

- [init(using: NWParameters, on: NWEndpoint.Port) throws](nwlistener/init(using:on:).md)
  Initializes a network listener, with an optional local port.
- [func start(queue: DispatchQueue)](nwlistener/start(queue:).md)
  Registers for listening, and sets the queue on which all listener events are delivered.
- [NWListener.State](nwlistener/state-swift.enum.md)
  States indicating whether a listener is able to accept incoming connections.
- [var port: NWEndpoint.Port?](nwlistener/port.md)
  The port on which the listener can accept connections.
- [func cancel()](nwlistener/cancel.md)
  Stops listening for inbound connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwlistener/stateupdatehandler)*