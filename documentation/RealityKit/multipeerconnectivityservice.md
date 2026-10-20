# MultipeerConnectivityService

**Framework**: RealityKit  
**Kind**: class  
**Role**: Class

A service that provides scene synchronization among all peers in a multipeer connectivity session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+

## Declaration

```swift
class MultipeerConnectivityService
```

#### Overview

RealityKit uses this class to automatically sync scenes with other connected devices running the same app. It leverages the [Multipeer Connectivity](../MultipeerConnectivity/MultipeerConnectivity.md) framework to automatically keep the scenes of all connected devices synchronized. To sync a RealityKit scene, create a [`MultipeerConnectivityService`](./multipeerconnectivityservice.md) object initialized with an [`MCSession`](../MultipeerConnectivity/mcsession.md) and assign it to your scene’s [`synchronizationService`](./scene/synchronizationservice.md) property.

```swift
let peerID = MCPeerID(displayName: UIDevice.current.name)
let session = MCSession(peer: peerID, securityIdentity: nil, encryptionPreference: .required)
arView.scene.synchronizationService = try?
MultipeerConnectivityService(session: self.session)
```

For more information on browsing for, and connecting to, other devices, see [Multipeer Connectivity](../MultipeerConnectivity/MultipeerConnectivity.md).

## Topics

### Creating a connectivity service
- [init(session: MCSession) throws](./multipeerconnectivityservice/init%28session%29.md)
  Creates a new connectivity service.
### Getting the session
- [let session: MCSession](./multipeerconnectivityservice/session.md)
  The multipeer connectivity session used by the service.
### Managing ownership
- [func owner(of: Entity) -> (any SynchronizationPeerID)?](./multipeerconnectivityservice/owner%28of%29.md)
  Gets the device that owns a given entity.
- [func giveOwnership(of: Entity, toPeer: any SynchronizationPeerID) -> Bool](./multipeerconnectivityservice/giveownership%28of,topeer%29.md)
  Transfers ownership of the given entity to the named network device.
### Finding an entity
- [func entity(for: MultipeerConnectivityService.Identifier) -> Entity?](./multipeerconnectivityservice/entity%28for%29.md)
  Gets the entity with the given identifier.
### Pausing and resuming
- [func stopSync()](./multipeerconnectivityservice/stopsync%28%29.md)
  Stops multipeer synchronization.
- [func startSync()](./multipeerconnectivityservice/startsync%28%29.md)
  Begins multipeer synchronization.
### Configuring the session
- [func setHandshake(count: UInt32, timeoutMs: UInt32)](./multipeerconnectivityservice/sethandshake%28count,timeoutms%29.md)
  Configures handshake and timeout settings.

## Relationships

### Conforms To
- [SynchronizationService](./synchronizationservice.md)

## See Also

### Multipeer synchronization
- [Loading remote assets in multiplayer apps](./loading-remote-assets.md)
  Ensure assets load on all connected peers before using them.
- [class NetworkCompatibilityToken](./networkcompatibilitytoken.md)
  An opaque token used to check the networking compatibility between two peers in a multipeer connection.
- [NetworkCompatibilityToken.Compatibility](./networkcompatibilitytoken/compatibility.md)
  Indicates whether two devices running RealityKit are compatible and able to connect and sync scenes.
- [protocol TransientComponent](./transientcomponent.md)
  An interface for components that aren’t saved to file or cloned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/multipeerconnectivityservice)*