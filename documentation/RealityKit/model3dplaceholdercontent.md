# Model3DPlaceholderContent

**Framework**: RealityKit  
**Kind**: struct

A container view that presents either a 3D model or a placeholder for one.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency struct Model3DPlaceholderContent<Model, Placeholder> where Model : View, Placeholder : View
```

#### Overview

Don’t instantiate this type directly. [`Model3D`](model3d.md) creates it for you.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)

## See Also

- [struct Model3D](model3d.md)
  A view that asynchronously loads and displays a 3D model.
- [enum Model3DPhase](model3dphase.md)
  The current phase of the asynchronous model loading operation.
- [struct ResolvedModel3D](resolvedmodel3d.md)
  A view for displaying static three-dimensional models.
- [class Model3DAsset](model3dasset.md)
  A container used to represent the asset loaded into the Model3D View.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/model3dplaceholdercontent)*