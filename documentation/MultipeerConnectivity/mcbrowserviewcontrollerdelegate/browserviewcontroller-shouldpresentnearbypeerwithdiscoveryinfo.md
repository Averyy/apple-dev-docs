# browserViewController(_:shouldPresentNearbyPeer:withDiscoveryInfo:)

**Framework**: Multipeer Connectivity  
**Kind**: method

Called when a new peer is discovered to decide whether to show it in the user interface.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
optional func browserViewController(_ browserViewController: MCBrowserViewController, shouldPresentNearbyPeer peerID: MCPeerID, withDiscoveryInfo info: [String : String]?) -> Bool
```

#### Return Value

This delegate method should return [`true`](https://developer.apple.com/documentation/Swift/true) if the newly discovered peer should be shown in the user interface, or [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

#### Discussion

If this method is not provided, all peers are shown.

## Parameters

- `browserViewController`: The browser view controller object that discovered the new peer.
- `peerID`: The unique ID of the nearby peer.
- `info`: The info dictionary advertised by the discovered peer. For more information on the contents of this dictionary, see the documentation for   in  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontrollerdelegate/browserviewcontroller(_:shouldpresentnearbypeer:withdiscoveryinfo:))*