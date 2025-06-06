# invitePeer(_:to:withContext:timeout:)

**Framework**: Multipeer Connectivity  
**Kind**: method

Invites a discovered peer to join a Multipeer Connectivity session.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func invitePeer(_ peerID: MCPeerID, to session: MCSession, withContext context: Data?, timeout: TimeInterval)
```

## Parameters

- `session`: The session you wish the invited peer to join.
- `context`: An arbitrary piece of data that is passed to the nearby peer. This can be used to provide further information to the user about the nature of the invitation.
- `timeout`: This timeout is measured in seconds, and must be a positive value. If a negative value or zero is specified, the default timeout (30 seconds) is used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/invitepeer(_:to:withcontext:timeout:))*