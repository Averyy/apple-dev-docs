# sessionMode

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The mode the session uses to find other peers.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported.

## Declaration

```swift
var sessionMode: GKSessionMode { get }
```

```objc
@property (readonly) GKSessionMode sessionMode;
```

#### Discussion

The session mode changes the behavior of the session when [`isAvailable`](./isavailable.md) is set to [`true`](../../Swift/true.md).

- A [`GKSessionMode.server`](../gksessionmode/server.md) session advertises itself to local devices using its session ID.
- A [`GKSessionMode.client`](../gksessionmode/client.md) session searches for local devices advertising the same session ID. As it discovers available and compatible peers, it calls the delegate’s  [`session(_:peer:didChange:)`](../gksessiondelegate/session%28_,peer,didchange%29.md) method.
- A [`GKSessionMode.peer`](../gksessionmode/peer.md) session both advertises as a server and searches as a client.

## See Also

### Related Documentation
- [var isAvailable: Bool](./isavailable.md)
  A Boolean value that determines whether or not the session wants to connect to new peers.
### Information about the Session
- [var displayName: String!](./displayname.md)
  The name of the user.
- [var peerID: String!](./peerid.md)
  A string that identifies your session to other peers.
- [var sessionID: String!](./sessionid.md)
  A string used to filter the list of peers who are allowed to see your session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksession/sessionmode)*