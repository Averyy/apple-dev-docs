# Discovering peers with Multipeer Connectivity

**Framework**: Nearby Interaction

Exchange discovery tokens over the local network.

#### Overview

To start an interaction session with a nearby device, an app checks for nearby peer devices. When the app finds a peer, it creates an [`NISession`](nisession.md) and sends the session’s [`discoveryToken`](nisession/discoverytoken.md) to the peer using the network technology on which they have agreed. An app can use [`Multipeer Connectivity`](https://developer.apple.com/documentation/MultipeerConnectivity) to find nearby peers and exchange discovery tokens over the local network.

For an example app that find peer devices using Multipeer Connectivity, see [`Implementing Interactions Between Users in Close Proximity`](implementing-interactions-between-users-in-close-proximity.md).

##### Add Bonjour Services Plist Keys

To use the local network on iOS and iPadOS 14, your app requires the [`NSBonjourServices`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSBonjourServices) key present in its `Info.plist`. The value of the key adheres to the following convention, including `.tcp` and `.udp` extensions.

```swift
<key>NSBonjourServices</key>
<array>
    <string>_myAppName._tcp</string>
    <string>_myAppName._udp</string>
</array>
```

In addition, the system prompts users to grant the app explicit permission to use the local network. To control the messaging of this prompt, your app can include the `NSLocalNetworkUsageDescription` key.

##### Check for a Nearby Peer

To broadcast a device’s ability to communicate through Multipeer Connectivity, your app creates an [`MCNearbyServiceAdvertiser`](https://developer.apple.com/documentation/MultipeerConnectivity/MCNearbyServiceAdvertiser). The app creates an [`MCNearbyServiceBrowser`](https://developer.apple.com/documentation/MultipeerConnectivity/MCNearbyServiceBrowser) to find other devices advertising with the same technology. When the browser finds another device, it calls [`browser(_:foundPeer:withDiscoveryInfo:)`](https://developer.apple.com/documentation/MultipeerConnectivity/MCNearbyServiceBrowserDelegate/browser(_:foundPeer:withDiscoveryInfo:)) and invites the peer to exchange tokens by calling [`invitePeer(_:to:withContext:timeout:)`](https://developer.apple.com/documentation/MultipeerConnectivity/MCNearbyServiceBrowser/invitePeer(_:to:withContext:timeout:)).

After the other device receives the invitation, [`MCNearbyServiceAdvertiser`](https://developer.apple.com/documentation/MultipeerConnectivity/MCNearbyServiceAdvertiser) calls [`advertiser(_:didReceiveInvitationFromPeer:withContext:invitationHandler:)`](https://developer.apple.com/documentation/MultipeerConnectivity/MCNearbyServiceAdvertiserDelegate/advertiser(_:didReceiveInvitationFromPeer:withContext:invitationHandler:)), in which the apps can begin sharing their discovery tokens.

> ❗ **Important**:  This process invites any nearby device to interact, but depending on the level of security an app requires, the app can more precisely control broadcasting, invitation, and acceptance behavior. For more information, see [`Multipeer Connectivity`](https://developer.apple.com/documentation/MultipeerConnectivity).

 This process invites any nearby device to interact, but depending on the level of security an app requires, the app can more precisely control broadcasting, invitation, and acceptance behavior. For more information, see [`Multipeer Connectivity`](https://developer.apple.com/documentation/MultipeerConnectivity).

##### Exchange Discovery Tokens

To respond to the invitation, the app sends its NI session’s [`discoveryToken`](ninearbyobject/discoverytoken.md) to the peer. Because Multipeer Connectivity requires serialization of the data it transmits, the app archives it first.

```swift
let data = try! NSKeyedArchiver.archivedData(withRootObject: niSession.discoverToken, requiringSecureCoding: true)

```

When the receiving peer accepts data from the Multipeer Connectivity session, the app unarchives the data to deserialize the peer’s discovery token.

```swift
let peerDiscoverToken = try! NSKeyedUnarchiver.unarchivedObject(ofClass: NIDiscoverToken, from: data) 
```

## See Also

- [Implementing Interactions Between Users in Close Proximity](implementing-interactions-between-users-in-close-proximity.md)
  Enable devices to access relative positioning information.
- [Extending advanced direction finding and ranging](extending-advanced-direction-finding-and-ranging.md)
  Extend your app’s direction finding capabilities with data from Ultra Wideband devices.
- [class NINearbyPeerConfiguration](ninearbypeerconfiguration.md)
  A configuration that enables interaction between iPhone or Apple Watch devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/discovering-peers-with-multipeer-connectivity)*