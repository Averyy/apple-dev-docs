# init(blendShapeName:weightNames:)

**Framework**: RealityKit  
**Kind**: init

Creates a mapping that applies the weight names to mesh parts in a model component.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
init(blendShapeName: String, weightNames: [String])
```

#### Discussion

This creates a mapping that applies the weight names to every mesh part in the [`ModelComponent`](modelcomponent.md) associated with the [`BlendShapeWeightsComponent`](blendshapeweightscomponent.md)’s entity.

Make sure the weight names match the weight names in the mesh resource data.  RealityKit will ignore weight names that do not match.

## Parameters

- `blendShapeName`: The user-defined name of the blend shape.
- `weightNames`: The names of the weights that are managed by this mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/blendshapeweightsmapping/init(blendshapename:weightnames:))*