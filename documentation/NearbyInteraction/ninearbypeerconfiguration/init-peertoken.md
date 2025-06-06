# init(peerToken:)

**Framework**: Nearby Interaction  
**Kind**: init

Creates a configuration for interaction between devices, including iPhone and Apple Watch.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- watchOS 7.3+

## Declaration

```swift
init(peerToken: NIDiscoveryToken)
```

## Mentions

- [Initiating and maintaining a session](initiating-and-maintaining-a-session.md)

#### Discussion

To acquire a peer’s discovery token, two instantiations of the app exchange their respective [`discoveryToken`](nisession/discoverytoken.md) over the network using a method you choose. For a discussion that covers sharing discovery tokens using [`Multipeer Connectivity`](https://developer.apple.com/documentation/MultipeerConnectivity), see [`Discovering peers with Multipeer Connectivity`](discovering-peers-with-multipeer-connectivity.md).

## Parameters

- `peerToken`: The value of another device’s discovery token. This value uniquely identifies the other peer in the interaction session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/ninearbypeerconfiguration/init(peertoken:))*