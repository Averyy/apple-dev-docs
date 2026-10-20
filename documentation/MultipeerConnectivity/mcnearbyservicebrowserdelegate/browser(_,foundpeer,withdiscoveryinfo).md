# browser(_:foundPeer:withDiscoveryInfo:)

**Framework**: Multipeer Connectivity  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Called when a nearby peer is found.

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
func browser(_ browser: MCNearbyServiceBrowser, foundPeer peerID: MCPeerID, withDiscoveryInfo info: [String : String]?)
```

```objc
- (void) browser:(MCNearbyServiceBrowser *) browser foundPeer:(MCPeerID *) peerID withDiscoveryInfo:(NSDictionary<NSString *,NSString *> *) info;
```

#### Discussion

The peer ID provided to this delegate method can be used to invite the nearby peer to join a session.

## Parameters

- `browser`: The browser object that found the nearby peer.
- `peerID`: The unique ID of the peer that was found.
- `info`: The info dictionary advertised by the discovered peer. For more information on the contents of this dictionary, see the documentation for [`init(peer:discoveryInfo:serviceType:)`](../mcnearbyserviceadvertiser/init%28peer,discoveryinfo,servicetype%29.md) in [`MCNearbyServiceAdvertiser`](../mcnearbyserviceadvertiser.md).

## See Also

### Peer Discovery Delegate Methods
- [func browser(MCNearbyServiceBrowser, lostPeer: MCPeerID)](./browser%28_,lostpeer%29.md)
  Called when a nearby peer is lost.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowserdelegate/browser(_:foundpeer:withdiscoveryinfo:))*