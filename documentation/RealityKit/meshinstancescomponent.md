# MeshInstancesComponent

**Framework**: RealityKit  
**Kind**: struct

A component that performs GPU instancing on the model of the same entity.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct MeshInstancesComponent
```

#### Overview

RealityKit applies the transform hierarchy of this component’s entity to the individual transforms specified by [`LowLevelInstanceData`](lowlevelinstancedata.md). You can think of these instances as sub-entities of the entity you apply this component to, meaning [`LowLevelInstanceData`](lowlevelinstancedata.md) is in the local space of that same entity.

Due to this transform hierarchy, use the entity’s [`scale`](hastransform/scale.md), [`position`](hastransform/position.md), and [`orientation`](hastransform/orientation.md) to transform the overall group of instances. Use the transforms within [`LowLevelInstanceData`](lowlevelinstancedata.md) to transform the individual instances.

To use this component, create a [`LowLevelInstanceData`](lowlevelinstancedata.md) instance and use the convenience initializer, [`init(mesh:modelID:instances:bounds:)`](meshinstancescomponent/init(mesh:modelid:instances:bounds:).md) to create the `MeshInstancesComponent` directly from a [`MeshResource`](meshresource.md).

```swift
let entity = try await ModelEntity(named: "robot")

guard let mesh = entity.components[ModelComponent.self]?.mesh else { return }

let instanceCount = 10
let instanceData = try LowLevelInstanceData(instanceCount: instanceCount)

instanceData.withMutableTransforms { transforms in
    for i in 0..<instanceCount {

        let instanceAngle = 2 * .pi * Float(i) / Float(instanceCount)
        let radialTranslation: SIMD3<Float> = [-sin(instanceAngle), cos(instanceAngle), 0] * 2

        // Position each robot around a circle.
        let transform = Transform(
            scale: .one / 10,
            rotation: simd_quatf(angle: instanceAngle, axis: [0, 0, 1]),
            translation: radialTranslation
        )
        transforms[i] = transform.matrix
    }
}

// Instance only the first model.
let modelID = mesh.contents.models.first?.id

// Create the component using the convenience initializer.
let instancesComponent = try MeshInstancesComponent(
    mesh: mesh,
    modelID: modelID,
    instances: instanceData
)
entity.components.set(instancesComponent)

// Place the instance group into position.
entity.position = [0, 0, -1]
```

![A screenshot of ten robots placed around a circle.](https://docs-assets.developer.apple.com/published/b304a9ca60c5f1d74a82d684491a64ee/robot-instancing.jpg)

## Topics

### Structures
- [MeshInstancesComponent.Part](meshinstancescomponent/part.md)
  A group of instances to render.
### Initializers
- [init()](meshinstancescomponent/init.md)
  Creates an empty mesh instances component.
- [init(mesh: MeshResource, modelID: String?, instances: LowLevelInstanceData, bounds: BoundingBox?) throws](meshinstancescomponent/init(mesh:modelid:instances:bounds:).md)
  Creates a mesh instances component with a mesh resource, optional model ID, instance data, and optional bounding box.
### Subscripts
- [subscript(partIndex _: Int) -> MeshInstancesComponent.Part?](meshinstancescomponent/subscript(partindex:).md)

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