# init(using:on:)

**Framework**: Network  
**Kind**: init

Initializes a network listener, with an optional local port.

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
init(using: NWParameters, on: NWEndpoint.Port = .any) throws
```

## See Also

- [func start(queue: DispatchQueue)](nwlistener/start(queue:).md)
  Registers for listening, and sets the queue on which all listener events are delivered.
- [var stateUpdateHandler: ((NWListener.State) -> Void)?](nwlistener/stateupdatehandler.md)
  A handler that receives listener state updates.
- [NWListener.State](nwlistener/state-swift.enum.md)
  States indicating whether a listener is able to accept incoming connections.
- [var port: NWEndpoint.Port?](nwlistener/port.md)
  The port on which the listener can accept connections.
- [func cancel()](nwlistener/cancel.md)
  Stops listening for inbound connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwlistener/init(using:on:))*