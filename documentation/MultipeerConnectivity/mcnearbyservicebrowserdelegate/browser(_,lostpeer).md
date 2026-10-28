# browser(_:lostPeer:)

**Framework**: Multipeer Connectivity  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Called when a nearby peer is lost.

**Availability**:
- iOS 7.0+ - Deprecated in 27.0
- iPadOS 7.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use Network Framework instead

## Declaration

```swift
func browser(_ browser: MCNearbyServiceBrowser, lostPeer peerID: MCPeerID)
```

```objc
- (void) browser:(MCNearbyServiceBrowser *) browser lostPeer:(MCPeerID *) peerID;
```

## Discussion

This callback informs your app that invitations can no longer be sent to a peer, and that your app should remove that peer from its user interface.

> ❗ **Important**:  Because there is a delay between when a host leaves a network and when the underlying Bonjour layer detects that it has left, the fact that your app has not yet received a disappearance callback does not guarantee that it can communicate with the peer successfully.

## Parameters

- `browser`: The browser object that lost the nearby peer.
- `peerID`: The unique ID of the nearby peer that was lost.

## See Also

### Peer Discovery Delegate Methods
- [func browser(MCNearbyServiceBrowser, foundPeer: MCPeerID, withDiscoveryInfo: [String : String]?)](./browser%28_,foundpeer,withdiscoveryinfo%29.md)
  Called when a nearby peer is found.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowserdelegate/browser(_:lostpeer:))*