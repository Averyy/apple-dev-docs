# MeshInstancesComponent

**Framework**: RealityKit  
**Kind**: struct

A component that performs GPU instancing on the ModelComponent on the same Entity.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct MeshInstancesComponent
```

#### Overview

RealityKit applies the transform hierarchy of this component’s entity to the individual transforms specified by LowLevelInstanceData. You can think of these instances as children of the MeshInstancesComponent’s entity, meaning LowLevelInstanceData is specified in the local space of the entity.

Due to this transform hierarchy, use the entity’s scale, translation, and orientation to transform the overall group of instances. Use the transforms within LowLevelInstanceData to transform the individual instances.

To use this component, add it to an entity, then populate a LowLevelInstanceData structure for the index of the mesh part you want to instance on the ModelComponent.

```swift
let instanceCount = 10

let entity = ModelEntity(named: "robot")
var instancesComponent = MeshInstancesComponent()
let instanceData = try LowLevelInstanceData.init(instanceCount: instanceCount)
instancesComponent[partIndex: 0] = instanceData
entity.components[MeshInstancesComponent.self] = instancesComponent

instances.withMutableTransforms { transforms in
  for i in 0..<instanceCount {

    // Scale each robot down to a reasonable size
    var scale = SIMD4<Float>(x: 0.5, y: 0.5, z: 0.5, w: 1.0)

    var matrix = float4x4(diagonal: scale)
    matrix.columns.3 = .init(x: -1 + i * 0.1, y: 0, z: 0)
  }
}

// Place the instance group into position.
entity.scale = .init(x: 0.25, y: 0.25, z: 0.25)
entity.position = .init(x: 0, y: 1.5, z: 0)
```

## Topics

### Initializers
- [init()](meshinstancescomponent/init.md)
### Subscripts
- [subscript(partIndex _: Int) -> LowLevelInstanceData?](meshinstancescomponent/subscript(partindex:).md)

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [struct ModelSortGroupComponent](modelsortgroupcomponent.md)
  A component that configures the rendering order for an entity’s model.
- [struct ModelSortGroup](modelsortgroup.md)
  A group that you assign to multiple entities to tell the renderer what order and how to render the entities in the group.
- [struct OpacityComponent](opacitycomponent.md)
  A component that controls the opacity of an entity and its descendants.
- [struct AdaptiveResolutionComponent](adaptiveresolutioncomponent.md)
  A component that provides the suggested pixels per meter necessary to render an object.
- [struct ModelDebugOptionsComponent](modeldebugoptionscomponent.md)
  A component that changes how RealityKit renders its entity to help with debugging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshinstancescomponent)*