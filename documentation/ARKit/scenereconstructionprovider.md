# SceneReconstructionProvider

**Framework**: ARKit  
**Kind**: class

A source of live data about the shape of a person’s surroundings.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
final class SceneReconstructionProvider
```

## Topics

### Creating a scene reconstruction provider
- [init(modes: [SceneReconstructionProvider.Mode])](scenereconstructionprovider/init(modes:).md)
  Creates a provider that reconstructs a person’s surroundings.
- [let modes: [SceneReconstructionProvider.Mode]](scenereconstructionprovider/modes.md)
  The modes of scene reconstruction a provider supplies.
- [SceneReconstructionProvider.Mode](scenereconstructionprovider/mode.md)
  The additional kinds of information you can request about a person’s surroundings.
- [static var isSupported: Bool](scenereconstructionprovider/issupported.md)
  A Boolean value that indicates whether the current runtime environment supports scene reconstruction providers.
### Observing scene reconstruction
- [var anchorUpdates: AnchorUpdateSequence<MeshAnchor>](scenereconstructionprovider/anchorupdates.md)
  An asynchronous sequence of updates to scene meshes that the scene reconstruction provider detects.
- [var state: DataProviderState](scenereconstructionprovider/state.md)
  A value that indicates whether the scene reconstruction provider is currently supplying anchor updates.
### Inspecting a scene reconstruction provider
- [var description: String](scenereconstructionprovider/description.md)
  A textual representation of this scene reconstruction provider.
- [var allAnchors: [MeshAnchor]](scenereconstructionprovider/allanchors.md)
  An array that contains the mesh anchors the scene reconstruction provider is tracking.
- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](scenereconstructionprovider/requiredauthorizations.md)
  The types of authorizations necessary for running scene reconstruction.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [DataProvider](dataprovider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Incorporating real-world surroundings in an immersive experience](../visionOS/incorporating-real-world-surroundings-in-an-immersive-experience.md)
  Create an immersive experience by making your app’s content respond to the local shape of the world.
- [struct MeshAnchor](meshanchor.md)
  A volume of space that contains a mesh of a person’s surroundings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/scenereconstructionprovider)*