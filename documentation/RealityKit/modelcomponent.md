# ModelComponent

**Framework**: RealityKit  
**Kind**: struct

A component that contains a mesh and materials for the visual appearance of an entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
struct ModelComponent
```

## Mentions

- [Creating a plane with low-level mesh](creating-a-plane-with-low-level-mesh.md)

#### Overview

This component is a foundational component for all visual content in RealityKit. Use `ModelComponent` to render 3D models by attaching it to any [`Entity`](entity.md) in your RealityKit scene.

To create a `ModelComponent`, you need a mesh and the number of materials that mesh expects, which is typically one.

For example, here’s how to create a simple blue, metallic box using [`generateBox(size:cornerRadius:)`](meshresource/generatebox(size:cornerradius:)-8em0v.md), and [`SimpleMaterial`](simplematerial.md):

```swift
let mesh = MeshResource.generateBox(size: 1, cornerRadius: 0.05)
let material = SimpleMaterial(color: .blue, isMetallic: true)

let modelComponent = ModelComponent(mesh: mesh, materials: [material])

let entity = Entity()
entity.components.set(modelComponent)
```

![A screenshot of a reflective, metallic blue cube centered on the screen with a plain background.](https://docs-assets.developer.apple.com/published/945150be269ae400b094a53f46671006/modelcomponent-cube-simple.jpg)

Make different primitive shapes, like spheres with [`generateSphere(radius:)`](meshresource/generatesphere(radius:).md), or cylinders with [`generateCylinder(height:radius:)`](meshresource/generatecylinder(height:radius:).md), or create custom shapes with [`MeshDescriptor`](meshdescriptor.md). For more information about materials, see [`Applying realistic material and lighting effects to entities`](applying-realistic-material-and-lighting-effects-to-entities.md)

> 💡 **Tip**: To load a USDZ or reality file to your app, use an entity initializer such as [`init(named:in:)`](entity/init(named:in:).md) or [`init(contentsOf:withName:)`](entity/init(contentsof:withname:).md).

Use other components like [`CollisionComponent`](collisioncomponent.md), [`PhysicsBodyComponent`](physicsbodycomponent.md), [`PhysicsMotionComponent`](physicsmotioncomponent.md), and [`InputTargetComponent`](inputtargetcomponent.md) to make entities interactive and dynamic.

## Topics

### Creating a model component
- [init(mesh: MeshResource, materials: [any Material])](modelcomponent/init(mesh:materials:).md)
  Creates a model component from a mesh and a collection of materials.
### Configuring a mesh
- [var mesh: MeshResource](modelcomponent/mesh.md)
  The mesh that defines the model’s shape.
### Configuring the materials
- [var materials: [any Material]](modelcomponent/materials.md)
  The materials that define the model’s visual appearance.
### Modifying the bounding box for rendering
- [var boundsMargin: Float](modelcomponent/boundsmargin.md)
  A margin applied to an entity’s bounding box that determines object visibility.

## Relationships

### Conforms To
- [Component](component.md)
- [Copyable](../Swift/Copyable.md)

## See Also

- [class MeshResource](meshresource.md)
  A high-level representation of a collection of vertices and edges that define a shape.
- [class ModelEntity](modelentity.md)
  A representation of a physical object that RealityKit renders and optionally simulates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/modelcomponent)*