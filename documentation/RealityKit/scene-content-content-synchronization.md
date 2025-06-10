# Content synchronization

**Framework**: RealityKit

Synchronize the contents of entities locally or across the network.

## Topics

### Entity ownership synchronization
- [protocol SynchronizationService](synchronizationservice.md)
  An interface that enables entity synchronization among a group of local peers.
- [SynchronizationService.Identifier](synchronizationservice/identifier.md)
  A type that represents a synchronization service identifier.
- [protocol SynchronizationPeerID](synchronizationpeerid.md)
  A type that represents a peer among a group of networked devices.
- [struct SynchronizationComponent](synchronizationcomponent.md)
  A component that synchronizes an entity between processes and networked applications.
- [SynchronizationComponent.OwnershipTransferMode](synchronizationcomponent/ownershiptransfermode-swift.enum.md)
  Modes of ownership transfer.
- [SynchronizationComponent.OwnershipTransferCompletionResult](synchronizationcomponent/ownershiptransfercompletionresult.md)
  The result of an ownership transfer request.
- [enum SynchronizationEvents](synchronizationevents.md)
  Events associated with network synchronization of scene information.
- [protocol HasSynchronization](hassynchronization.md)
  An interface that enables an entity to be synchronized between processes and networked applications.
### Multipeer synchronization
- [Loading remote assets in multiplayer apps](loading-remote-assets.md)
  Ensure assets load on all connected peers before using them.
- [class MultipeerConnectivityService](multipeerconnectivityservice.md)
  A service that provides scene synchronization among all peers in a multipeer connectivity session.
- [class NetworkCompatibilityToken](networkcompatibilitytoken.md)
  An opaque token used to check the networking compatibility between two peers in a multipeer connection.
- [NetworkCompatibilityToken.Compatibility](networkcompatibilitytoken/compatibility.md)
  Indicates whether two devices running RealityKit are compatible and able to connect and sync scenes.
- [protocol TransientComponent](transientcomponent.md)
  An interface for components that aren’t saved to file or cloned.

## See Also

- [Hello World](../visionOS/World.md)
  Use windows, volumes, and immersive spaces to teach people about the Earth.
- [Enabling video reflections in an immersive environment](../visionOS/enabling-video-reflections-in-an-immersive-environment.md)
  Create a more immersive experience by adding video reflections in a custom environment.
- [Creating a spatial drawing app with RealityKit](creating-a-spatial-drawing-app-with-realitykit.md)
  Use low-level mesh and texture APIs to achieve fast updates to a person’s brush strokes by integrating RealityKit with ARKit and SwiftUI.
- [Generating interactive geometry with RealityKit](generating-interactive-geometry-with-realitykit.md)
  Create an interactive mesh with low-level mesh and low-level texture.
- [Combining 2D and 3D views in an immersive app](combining-2d-and-3d-views-in-an-immersive-app.md)
  Use attachments to place 2D content relative to 3D content in your visionOS app.
- [Transforming RealityKit entities using gestures](transforming-realitykit-entities-with-gestures.md)
  Build a RealityKit component to support standard visionOS gestures on any entity.
- [Presenting images in RealityKit](presenting-images-in-realitykit.md)
  Create and display spatial scenes in RealityKit.
- [Models and meshes](scene-content-models-and-meshes.md)
  Display virtual objects in your scene with mesh-based models.
- [Materials, textures, and shaders](scene-content-materials-and-shaders.md)
  Apply textures to the surface of your scene’s 3D objects to give each object a unique appearance.
- [Anchors](scene-content-anchors.md)
  Lock virtual content to the real world.
- [Lights and cameras](scene-content-lights-and-cameras.md)
  Control the lighting and point of view for a scene.
- [Audio](scene-content-audio.md)
  Create personalized and realistic spatial audio experiences.
- [Videos](scene-content-videos.md)
  Present videos in your RealityKit experiences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene-content-content-synchronization)*