# NetworkCompatibilityToken

**Framework**: RealityKit  
**Kind**: class

An opaque token used to check the networking compatibility between two peers in a multipeer connection.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
final class NetworkCompatibilityToken
```

#### Overview

[`RealityKit`](RealityKit.md) apps running on incompatible versions of RealityKit can’t connect and sync over the network. Use [`NetworkCompatibilityToken`](networkcompatibilitytoken.md) to check if two peers can synchronize [`RealityKit`](RealityKit.md) scenes over the network. With this class, host applications can prevent incompatible clients from joining.

Client apps send a copy of their token to the host when attempting to connect to a host app. The host deserializes that token and calls [`compatibilityWith(_:)`](networkcompatibilitytoken/compatibilitywith(_:).md) on [`NetworkCompatibilityToken`](networkcompatibilitytoken.md).[`local`](networkcompatibilitytoken/local.md). If [`compatibilityWith(_:)`](networkcompatibilitytoken/compatibilitywith(_:).md) returns [`NetworkCompatibilityToken.Compatibility.compatible`](networkcompatibilitytoken/compatibility/compatible.md), the client and host can sync and it’s safe to proceed with the connection. If [`compatibilityWith(_:)`](networkcompatibilitytoken/compatibilitywith(_:).md) returns any other value, the client that’s attempting to connect is incompatible and should be ignored.

A client running a [`MCNearbyServiceAdvertiser`](https://developer.apple.com/documentation/MultipeerConnectivity/MCNearbyServiceAdvertiser), for example, writes its own token into its [`discoveryInfo`](https://developer.apple.com/documentation/MultipeerConnectivity/MCNearbyServiceAdvertiser/discoveryInfo) dictionary. When the host (running a [`MCNearbyServiceBrowser`](https://developer.apple.com/documentation/MultipeerConnectivity/MCNearbyServiceBrowser)) discovers that client, it deserializes the client’s token from the `discoverInfo` dictionary and uses it to check compatibility before inviting the client to the [`MCSession`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSession).

> **Note**: Even if two peers are compatible, scene synchronization can fail for other reasons, such as packet corruption or a poor network connection.

## Topics

### Retrieving tokens
- [static let local: NetworkCompatibilityToken](networkcompatibilitytoken/local.md)
  A token containing the local peer’s networking compatibility info.
### Checking compatibility
- [func compatibilityWith(NetworkCompatibilityToken) -> NetworkCompatibilityToken.Compatibility](networkcompatibilitytoken/compatibilitywith(_:).md)
  Compares network compatibility tokens between the local device and another device.
### Serializing tokens
- [init(from: any Decoder) throws](networkcompatibilitytoken/init(from:).md)
  Creates a new instance from a decoder.
- [func encode(to: any Encoder) throws](networkcompatibilitytoken/encode(to:).md)
  Writes the token’s data into an encoder.
### Enumerations
- [NetworkCompatibilityToken.Compatibility](networkcompatibilitytoken/compatibility.md)
  Indicates whether two devices running RealityKit are compatible and able to connect and sync scenes.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)

## See Also

- [Loading remote assets in multiplayer apps](loading-remote-assets.md)
  Ensure assets load on all connected peers before using them.
- [class MultipeerConnectivityService](multipeerconnectivityservice.md)
  A service that provides scene synchronization among all peers in a multipeer connectivity session.
- [NetworkCompatibilityToken.Compatibility](networkcompatibilitytoken/compatibility.md)
  Indicates whether two devices running RealityKit are compatible and able to connect and sync scenes.
- [protocol TransientComponent](transientcomponent.md)
  An interface for components that aren’t saved to file or cloned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/networkcompatibilitytoken)*