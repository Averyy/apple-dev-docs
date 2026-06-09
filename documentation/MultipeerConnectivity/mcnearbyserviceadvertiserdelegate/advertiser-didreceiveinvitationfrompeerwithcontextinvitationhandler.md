# advertiser(_:didReceiveInvitationFromPeer:withContext:invitationHandler:)

**Framework**: Multipeer Connectivity  
**Kind**: method  
**Required**: Yes

Called when an invitation to join a session is received from a nearby peer.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func advertiser(_ advertiser: MCNearbyServiceAdvertiser, didReceiveInvitationFromPeer peerID: MCPeerID, withContext context: Data?, invitationHandler: @escaping (Bool, MCSession?) -> Void)
```

## Parameters

- `advertiser`: The advertiser object that was invited to join the session.
- `peerID`: The peer ID of the nearby peer that invited your app to join the session.
- `context`: An arbitrary piece of data received from the nearby peer. This can be used to provide further information to the user about the nature of the invitation. > ❗ **Important**:  The nearby peer should treat any data it receives as potentially untrusted. To learn more about working with untrusted data, read [`Secure Coding Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Introduction.html#//apple_ref/doc/uid/TP40002415).
- `invitationHandler`: A block that your code must call to indicate whether the advertiser should accept or decline the invitation, and to provide a session with which to associate the peer that sent the invitation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiserdelegate/advertiser(_:didreceiveinvitationfrompeer:withcontext:invitationhandler:))*