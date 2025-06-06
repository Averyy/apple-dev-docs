# Loading remote assets in multiplayer apps

**Framework**: RealityKit

Ensure assets load on all connected peers before using them.

#### Overview

When a networked RealityKit app relies on assets stored on a remote server or loaded from the device’s file system outside of the app bundle, there are special precautions you must take to ensure RealityKit is able to sync those assets between peers. Because load times on different devices can vary greatly when loading assets such as 3D models, sound files, images, or movies, especially when those assets are stored on a remote server, it’s possible for network errors or other issues to prevent assets from loading on some connected peers. The host app must ensure that all exist on all peers before it attempts to add them to the synchronized RealityKit scene. If any peers are missing a resource, or are still in the process of loading a resource when the host attempts to sync with it, the sync fails and the app errors.

#### Assign Non Bundle Assets a Name When Loading

When loading networked assets from a remote server or from the local file system, it’s important to specify a name for the loaded asset. RealityKit uses this name to match up and sync objects on different devices, so the same asset must have the same on all connected peers in order for RealityKit to sync correctly.

When loading assets from the app’s bundle, RealityKit automatically assigns the asset’s name based on its filename, but when loading assets from other locations, you must specify the name manually using [`load(named:in:)`](entity/load(named:in:).md) or [`loadAsync(named:in:)`](entity/loadasync(named:in:).md). If your app fails to specify a name, or uses different names on different devices, RealityKit will see those assets as different entities and won’t attempt to sync them.

#### Load Assets Before You Need Them

One way to ensure that non-bundle assets have been successfully loaded on all peers before attempting to sync them, is to load them well before they are needed. Loading assets during app launch, before the user has a chance to start or join a multipeer session, for example, ensures that all peers load asset before they’re synced. In the case of apps with multiple or very large scenes, this approach may not be feasible, but for many apps, this is the best way to avoid issues caused by a peer’s resource load issues.

#### Communicate Load Status

If you’re not able to load all assets ahead of time, one way to ensure that all peers have finished loading assets is to broadcast a message using [`send(_:toPeers:with:)`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSession/send(_:toPeers:with:)) when each peer is done loading. The host app can then keep track of which peers have sent that message and only add the resources to the [`ARView`](arview.md) once all peers have notified it that they have finished loading. You can also have your app broadcast a different message when a peer is unable to load a particular asset. If a peer is unable to load an asset, the host can choose to send that peer a copy of the resource or to disconnect that peer.

Here’s a simple example of sending a sync message to connected peers:

```swift
enum SyncMessage: String {
    case beganAssetLoad
    case assetLoadFinishedSuccessfully
    case assetLoadFailed
}

private func notifyPeers(message: SyncMessage) {
    do {
        let messageData = Data(message.rawValue.utf8)
        let messageJSON = try JSONEncoder().encode(messageData)
        try session.send(messageJSON, toPeers: myPeers, with: .reliable)
    } catch {
        // Handle error here.
    }
}
```

For more information on sending data between connected peers, see [`Creating a collaborative session`](https://developer.apple.com/documentation/ARKit/creating-a-collaborative-session).

#### Send Missing Resources to Peers

Because a non-bundle resource load can fail for a number of reasons, a networked RealityKit app can implement a mechanism to allow peers to request resources they’re unable to load themselves. If one peer has successfully loaded an asset, it can use [`sendResource(at:withName:toPeer:withCompletionHandler:)`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSession/sendResource(at:withName:toPeer:withCompletionHandler:)) to send it to any other connected peer. Once any missing asset are successfully sent to the peers that need it, the host can safely add those assets to the shared RealityKit scene.

## See Also

- [static func load(named: String, in: Bundle?) throws -> Entity](entity/load(named:in:).md)
  Returns an entity by synchronously loading it from a bundle.
- [static func loadAsync(named: String, in: Bundle?) -> LoadRequest<Entity>](entity/loadasync(named:in:).md)
  Returns a load request that creates an entity by asynchronously loading it from a bundle.
- [Loading entities from a file](loading-entities-from-a-file.md)
  Retrieve an entity from storage on disk using a synchronous or an asynchronous load operation.
- [class MultipeerConnectivityService](multipeerconnectivityservice.md)
  A service that provides scene synchronization among all peers in a multipeer connectivity session.
- [class NetworkCompatibilityToken](networkcompatibilitytoken.md)
  An opaque token used to check the networking compatibility between two peers in a multipeer connection.
- [NetworkCompatibilityToken.Compatibility](networkcompatibilitytoken/compatibility.md)
  Indicates whether two devices running RealityKit are compatible and able to connect and sync scenes.
- [protocol TransientComponent](transientcomponent.md)
  An interface for components that aren’t saved to file or cloned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/loading-remote-assets)*