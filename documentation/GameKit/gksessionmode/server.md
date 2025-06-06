# GKSessionMode.server

**Framework**: GameKit  
**Kind**: case

A server advertises itself to local devices using its [`sessionID`](gksession/sessionid.md) property.

**Availability**:
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case server
```

## See Also

- [GKSessionMode.client](gksessionmode/client.md)
  A client searches for servers advertising the same [`sessionID`](gksession/sessionid.md) property.
- [GKSessionMode.peer](gksessionmode/peer.md)
  A peer advertises like a server and searches like a client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksessionmode/server)*