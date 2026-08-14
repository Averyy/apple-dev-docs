# Model3DAsset

**Framework**: RealityKit  
**Kind**: class

A container used to represent the asset loaded into the Model3D View.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
class Model3DAsset
```

## Topics

### Structures
- [Model3DAsset.EntityAnimation](model3dasset/entityanimation.md)
  An animation resource for an entity loaded from a bundle.
### Initializers
- [init(named: String, in: Bundle?) async throws](model3dasset/init(named:in:).md)
  Creates a named 3D model asset from the provided bundle.
- [init(url: URL) async throws](model3dasset/init(url:).md)
  Creates a 3D model asset from the provided URL.
### Instance Properties
- [var animationPlaybackController: AnimationPlaybackController?](model3dasset/animationplaybackcontroller.md)
  Reference to the animation playback controller instance that corresponds to the active animation on the entity.
- [var availableAnimations: [Model3DAsset.EntityAnimation]](model3dasset/availableanimations.md)
  List of all available animations on the entity.
- [var selectedAnimation: Model3DAsset.EntityAnimation?](model3dasset/selectedanimation.md)
  The currently active animation on the entity.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Escapable](../swift/escapable.md)
- [Observable](../observation/observable.md)

## See Also

- [struct Model3D](model3d.md)
  A view that asynchronously loads and displays a 3D model.
- [enum Model3DPhase](model3dphase.md)
  The current phase of the asynchronous model loading operation.
- [struct ResolvedModel3D](resolvedmodel3d.md)
  A view for displaying static three-dimensional models.
- [struct Model3DPlaceholderContent](model3dplaceholdercontent.md)
  A container view that presents either a 3D model or a placeholder for one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/model3dasset)*