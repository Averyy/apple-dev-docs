# sessionID

**Framework**: GameKit  
**Kind**: property

A string used to filter the list of peers who are allowed to see your session.

**Availability**:
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var sessionID: String! { get }
```

#### Discussion

The session ID is used by sessions configured as servers to advertise itself to other peers and by sessions configured as clients to search for compatible servers. The session ID should be the short name of an approved Bonjour service type.

## See Also

- [var displayName: String!](gksession/displayname.md)
  The name of the user.
- [var peerID: String!](gksession/peerid.md)
  A string that identifies your session to other peers.
- [var sessionMode: GKSessionMode](gksession/sessionmode.md)
  The mode the session uses to find other peers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksession/sessionid)*