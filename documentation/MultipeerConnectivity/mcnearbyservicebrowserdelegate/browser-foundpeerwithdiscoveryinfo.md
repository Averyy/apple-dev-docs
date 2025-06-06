# browser(_:foundPeer:withDiscoveryInfo:)

**Framework**: Multipeer Connectivity  
**Kind**: method  
**Required**: Yes

Called when a nearby peer is found.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func browser(_ browser: MCNearbyServiceBrowser, foundPeer peerID: MCPeerID, withDiscoveryInfo info: [String : String]?)
```

#### Discussion

The peer ID provided to this delegate method can be used to invite the nearby peer to join a session.

## Parameters

- `browser`: The browser object that found the nearby peer.
- `peerID`: The unique ID of the peer that was found.
- `info`: The info dictionary advertised by the discovered peer. For more information on the contents of this dictionary, see the documentation for   in  .

## See Also

- [func browser(MCNearbyServiceBrowser, lostPeer: MCPeerID)](mcnearbyservicebrowserdelegate/browser(_:lostpeer:).md)
  Called when a nearby peer is lost.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowserdelegate/browser(_:foundpeer:withdiscoveryinfo:))*