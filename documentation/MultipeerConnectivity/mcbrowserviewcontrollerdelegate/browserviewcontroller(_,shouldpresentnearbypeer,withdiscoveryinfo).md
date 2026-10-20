# browserViewController(_:shouldPresentNearbyPeer:withDiscoveryInfo:)

**Framework**: Multipeer Connectivity  
**Kind**: method  
**Role**: Instance Method

Called when a new peer is discovered to decide whether to show it in the user interface.

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
optional func browserViewController(_ browserViewController: MCBrowserViewController, shouldPresentNearbyPeer peerID: MCPeerID, withDiscoveryInfo info: [String : String]?) -> Bool
```

```objc
- (BOOL) browserViewController:(MCBrowserViewController *) browserViewController shouldPresentNearbyPeer:(MCPeerID *) peerID withDiscoveryInfo:(NSDictionary<NSString *,NSString *> *) info;
```

#### Return Value

This delegate method should return [`true`](../../Swift/true.md) if the newly discovered peer should be shown in the user interface, or [`false`](../../Swift/false.md) otherwise.

#### Discussion

If this method is not provided, all peers are shown.

## Parameters

- `browserViewController`: The browser view controller object that discovered the new peer.
- `peerID`: The unique ID of the nearby peer.
- `info`: The info dictionary advertised by the discovered peer. For more information on the contents of this dictionary, see the documentation for [`init(peer:discoveryInfo:serviceType:)`](../mcnearbyserviceadvertiser/init%28peer,discoveryinfo,servicetype%29.md) in [`MCNearbyServiceAdvertiser`](../mcnearbyserviceadvertiser.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontrollerdelegate/browserviewcontroller(_:shouldpresentnearbypeer:withdiscoveryinfo:))*