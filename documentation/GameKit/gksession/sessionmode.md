# sessionMode

**Framework**: GameKit  
**Kind**: property

The mode the session uses to find other peers.

**Availability**:
- macOS 10.8+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var sessionMode: GKSessionMode { get }
```

#### Discussion

The session mode changes the behavior of the session when [`isAvailable`](gksession/isavailable.md) is set to [`true`](https://developer.apple.com/documentation/Swift/true).

- A [`GKSessionMode.server`](gksessionmode/server.md) session advertises itself to local devices using its session ID.
- A [`GKSessionMode.client`](gksessionmode/client.md) session searches for local devices advertising the same session ID. As it discovers available and compatible peers, it calls the delegate’s  [`session(_:peer:didChange:)`](gksessiondelegate/session(_:peer:didchange:).md) method.
- A [`GKSessionMode.peer`](gksessionmode/peer.md) session both advertises as a server and searches as a client.

## See Also

- [var isAvailable: Bool](gksession/isavailable.md)
  A Boolean value that determines whether or not the session wants to connect to new peers.
- [var displayName: String!](gksession/displayname.md)
  The name of the user.
- [var peerID: String!](gksession/peerid.md)
  A string that identifies your session to other peers.
- [var sessionID: String!](gksession/sessionid.md)
  A string used to filter the list of peers who are allowed to see your session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksession/sessionmode)*