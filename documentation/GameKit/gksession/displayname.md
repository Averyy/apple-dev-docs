# displayName

**Framework**: GameKit  
**Kind**: property

The name of the user.

**Availability**:
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var displayName: String! { get }
```

#### Discussion

The display name is transmitted to visible peers so that they can present a human-readable name for your session.

## See Also

- [func displayName(forPeer: String!) -> String!](gksession/displayname(forpeer:).md)
  Returns a user-readable name for a peer.
- [var peerID: String!](gksession/peerid.md)
  A string that identifies your session to other peers.
- [var sessionID: String!](gksession/sessionid.md)
  A string used to filter the list of peers who are allowed to see your session.
- [var sessionMode: GKSessionMode](gksession/sessionmode.md)
  The mode the session uses to find other peers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksession/displayname)*