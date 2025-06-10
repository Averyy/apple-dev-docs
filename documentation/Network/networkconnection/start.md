# start()

**Framework**: Network  
**Kind**: method

Initiate some action to open the connection on the network like making a handshake, initiating a multiplexing session, etc. Starts the connection, which will cause the connection to evaluate its path, do resolution, and try to become ready (connected). `NetworkConnection` establishment is asynchronous. `onStateUpdate` will be called when the state changes. If the connection cannot be established, the state will transition to `waiting` with an associated error describing the reason. If an unrecoverable error is encountered, the state will transition to `failed` with an associated error value. If the connection is established, the state will transition to `ready`.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
final func start() -> Self
```

#### Discussion

Start should only be called once on a connection, and multiple calls to start will be ignored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkconnection/start())*