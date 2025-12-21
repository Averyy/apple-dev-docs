# PortalMaterial

**Framework**: RealityKit  
**Kind**: struct

A material that makes the mesh part a portal to a different world.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct PortalMaterial
```

#### Overview

You use a `PortalMaterial` with [`PortalComponent`](portalcomponent.md) and [`WorldComponent`](worldcomponent.md) to enable portal features.

You can set this material on individual mesh parts. For example, create a box with [`generateBox(width:height:depth:cornerRadius:splitFaces:)`](meshresource/generatebox(width:height:depth:cornerradius:splitfaces:).md). It can have some faces using [`PhysicallyBasedMaterial`](physicallybasedmaterial.md) and some faces using `PortalMaterial`.

```swift
let portal = Entity()
// When you set `splitFaces` to `true`, each face takes up a different material slot.
let cyanMaterial = SimpleMaterial(color: .cyan, isMetallic: false)
portal.components.set(ModelComponent(
    mesh: .generateBox(width: 0.5, height: 0.5, depth: 0.5, splitFaces: true),
    materials: [PortalMaterial(),
                cyanMaterial,
                cyanMaterial,
                cyanMaterial,
                cyanMaterial,
                cyanMaterial]
))
// Because the box has `0.5 x 0.5 x 0.5` dimensions,
// offset the portal plane on the z-axis by 0.25 so that
// it's at the front of the cube.
// Make sure it faces toward the positive z-direction.
portal.components.set(PortalComponent(
    target: world,
    clippingMode: .disabled,
    crossingMode: .plane(PortalComponent.Plane(position: [0, 0, 0.25], normal: [0, 0, 1]))
))
```

![A screenshot of cyan color box with only one face using portal material and a spaceship poking out of it](https://docs-assets.developer.apple.com/published/1e829c989c7a4cb292bc1ec6409b7bb4/portal-material-box.png)

RealityKit treats each mesh part with a `PortalMaterial` as a different portal, even if they are pointing to the same world. Beware of the performance impact of this usage.

See [`PortalComponent`](portalcomponent.md) for example usage.

## Topics

### Initializers
- [init()](portalmaterial/init.md)
### Instance Properties
- [var faceCulling: PortalMaterial.FaceCulling](portalmaterial/faceculling-swift.property.md)
  A process in which the system specifies polygons to remove before rendering a mesh using this material.
- [var triangleFillMode: PortalMaterial.TriangleFillMode](portalmaterial/trianglefillmode-swift.property.md)
  The object that controls how RealityKit draws triangles.
### Type Aliases
- [PortalMaterial.FaceCulling](portalmaterial/faceculling-swift.typealias.md)
  An alias for the cull mode object that’s appropriate for this material class.
- [PortalMaterial.TriangleFillMode](portalmaterial/trianglefillmode-swift.typealias.md)
  An alias for the triangle fill mode object that’s appropriate for this material class.

## Relationships

### Conforms To
- [Material](material.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [PortalMaterial.FaceCulling](portalmaterial/faceculling-swift.typealias.md)
  An alias for the cull mode object that’s appropriate for this material class.
- [PortalMaterial.TriangleFillMode](portalmaterial/trianglefillmode-swift.typealias.md)
  An alias for the triangle fill mode object that’s appropriate for this material class.
- [struct PortalComponent](portalcomponent.md)
  A component that turns mesh surfaces into portals to a different world.
- [struct WorldComponent](worldcomponent.md)
  A component that defines a portal world.
- [struct PortalCrossingComponent](portalcrossingcomponent.md)
  A component that allows entities to cross portal boundaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalmaterial)*