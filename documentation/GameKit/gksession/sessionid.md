# sessionID

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

A string used to filter the list of peers who are allowed to see your session.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

## Declaration

```swift
var sessionID: String! { get }
```

```objc
@property (readonly) NSString * sessionID;
```

#### Discussion

The session ID is used by sessions configured as servers to advertise itself to other peers and by sessions configured as clients to search for compatible servers. The session ID should be the short name of an approved Bonjour service type.

## See Also

### Information about the Session
- [var displayName: String!](./displayname.md)
  The name of the user.
- [var peerID: String!](./peerid.md)
  A string that identifies your session to other peers.
- [var sessionMode: GKSessionMode](./sessionmode.md)
  The mode the session uses to find other peers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksession/sessionid)*