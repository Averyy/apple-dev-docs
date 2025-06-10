# ResolvedModel3D

**Framework**: RealityKit  
**Kind**: struct

A view for displaying static three-dimensional models.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency struct ResolvedModel3D
```

#### Overview

You don’t instantiate this type directly, instead [`Model3D`](model3d.md) creates instances for you.

## Topics

### Instance Methods
- [func resizable(Bool) -> ResolvedModel3D](resolvedmodel3d/resizable(_:).md)
  Allows this model to resize itself to fit its container.

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
- [struct Model3DPlaceholderContent](model3dplaceholdercontent.md)
  A container view that presents either a 3D model or a placeholder for one.
- [class Model3DAsset](model3dasset.md)
  A container used to represent the asset loaded into the Model3D View.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/resolvedmodel3d)*