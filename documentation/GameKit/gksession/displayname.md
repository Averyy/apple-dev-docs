# displayName

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The name of the user.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

## Declaration

```swift
var displayName: String! { get }
```

```objc
@property (readonly) NSString * displayName;
```

#### Discussion

The display name is transmitted to visible peers so that they can present a human-readable name for your session.

## See Also

### Related Documentation
- [func displayName(forPeer: String!) -> String!](./displayname%28forpeer%29.md)
  Returns a user-readable name for a peer.
### Information about the Session
- [var peerID: String!](./peerid.md)
  A string that identifies your session to other peers.
- [var sessionID: String!](./sessionid.md)
  A string used to filter the list of peers who are allowed to see your session.
- [var sessionMode: GKSessionMode](./sessionmode.md)
  The mode the session uses to find other peers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksession/displayname)*