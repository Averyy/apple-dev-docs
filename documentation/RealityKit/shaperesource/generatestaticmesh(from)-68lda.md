# generateStaticMesh(from:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Creates a mesh-based collision shape derived from an ARKit Scene Understanding mesh anchor.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
nonisolated
static func generateStaticMesh(from meshAnchor: ARMeshAnchor) async throws -> ShapeResource
```

**Other overloads**:

```swift
@MainActor
@preconcurrency static func generateStaticMesh(from mesh: MeshResource) async throws -> ShapeResource
```

```swift
nonisolated
static func generateStaticMesh(from meshAnchor: MeshAnchor) async throws -> ShapeResource
```

## Return Value

The new shape.

## Discussion

The returned `ShapeResource` can only be used under the following circumstances:

- This shape can only be used with `PhysicsBodyMode.static` (not `.dynamic` or `.kinematic`)
- This shape cannot be used with `CollisionComponent.Mode.trigger`

In other words, the returned shape can only be used for static world geometry.

> **Note**: Generating a shape resource from the AR mesh takes time, because the input mesh needs to be preprocessed (“cooked”) by the physics engine before it can be used.  This function is marked `async` because ideally this precomputation should occur in the background.  For example, when calling from non-`async` code, you can use Swift’s `Task` API to assign a priority (see the example below).

Below is example usage of this function, assumed to be called from a non-async block:

```swift
let myAnchor: ARMeshAnchor = ...
// It is recommended to use a low-priority task, since generating the collision mesh can take a while.
let myShapeTask = Task(priority: .low) {
    let shape = await ShapeResource.generateStaticMesh(from: myAnchor)

    // Now we can do something with `shape`, such as create an entity with it.
    // Make sure to call non-async RealityKit methods from the main actor:
    await MainActor.run {
        let entity = Entity()
        entity.components[CollisionComponent.self] = .init(shapes: [shape])

        // Note that `mode` can not be set to `.dynamic`.  Only `.static` is supported.
        entity.components[PhysicsBodyComponent.self] = .init(massProperties: .default,
                                                             material: nil,
                                                             mode: .static)
        // ...
    }
}
```

## Parameters

- `meshAnchor`: The mesh anchor which will be used for the collision shape.  This anchor needs to have `meshAnchor.geometry.faces.primitiveType == ARGeometryPrimitiveTypeTriangle`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shaperesource/generatestaticmesh(from:)-68lda)*