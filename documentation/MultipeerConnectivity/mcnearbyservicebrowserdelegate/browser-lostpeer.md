# browser(_:lostPeer:)

**Framework**: Multipeer Connectivity  
**Kind**: method  
**Required**: Yes

Called when a nearby peer is lost.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func browser(_ browser: MCNearbyServiceBrowser, lostPeer peerID: MCPeerID)
```

#### Discussion

This callback informs your app that invitations can no longer be sent to a peer, and that your app should remove that peer from its user interface.

> ❗ **Important**:  Because there is a delay between when a host leaves a network and when the underlying Bonjour layer detects that it has left, the fact that your app has not yet received a disappearance callback does not guarantee that it can communicate with the peer successfully.

 Because there is a delay between when a host leaves a network and when the underlying Bonjour layer detects that it has left, the fact that your app has not yet received a disappearance callback does not guarantee that it can communicate with the peer successfully.

## Parameters

- `browser`: The browser object that lost the nearby peer.
- `peerID`: The unique ID of the nearby peer that was lost.

## See Also

- [func browser(MCNearbyServiceBrowser, foundPeer: MCPeerID, withDiscoveryInfo: [String : String]?)](mcnearbyservicebrowserdelegate/browser(_:foundpeer:withdiscoveryinfo:).md)
  Called when a nearby peer is found.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowserdelegate/browser(_:lostpeer:))*