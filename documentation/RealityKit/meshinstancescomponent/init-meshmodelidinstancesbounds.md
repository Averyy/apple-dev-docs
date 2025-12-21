# init(mesh:modelID:instances:bounds:)

**Framework**: RealityKit  
**Kind**: init

Creates a mesh instances component with a mesh resource, optional model ID, instance data, and optional bounding box.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(mesh: MeshResource, modelID: String? = nil, instances: LowLevelInstanceData, bounds: BoundingBox? = nil) throws
```

## Parameters

- `mesh`: The mesh resource to instance.
- `modelID`: The name of the model to use. Set to   if there is only one model in the mesh resource.
- `instances`: The instance data containing the number of instances, and the transforms for each instance.
- `bounds`: The bounding box to use for the instance group this part draws.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshinstancescomponent/init(mesh:modelid:instances:bounds:))*