# advertiser(_:didReceiveInvitationFromPeer:withContext:invitationHandler:)

**Framework**: Multipeer Connectivity  
**Kind**: method  
**Required**: Yes

Called when an invitation to join a session is received from a nearby peer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func advertiser(_ advertiser: MCNearbyServiceAdvertiser, didReceiveInvitationFromPeer peerID: MCPeerID, withContext context: Data?, invitationHandler: @escaping (Bool, MCSession?) -> Void)
```

## Parameters

- `advertiser`: The advertiser object that was invited to join the session.
- `peerID`: The peer ID of the nearby peer that invited your app to join the session.
- `context`: An arbitrary piece of data received from the nearby peer. This can be used to provide further information to the user about the nature of the invitation.
- `invitationHandler`: A block that your code must call to indicate whether the advertiser should accept or decline the invitation, and to provide a session with which to associate the peer that sent the invitation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiserdelegate/advertiser(_:didreceiveinvitationfrompeer:withcontext:invitationhandler:))*