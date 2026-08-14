# PhysicallyBasedDecalComponent

**Framework**: RealityKit  
**Kind**: struct

A component that specifies a decal to be applied on the scene. A decal is essentially a projective texture applied to any mesh on the scene. The transform of the decal is inherited from the entity’s transform. The decal is projected along the local space negative z onto the meshes within its volume. All decal textures expect 2D texture resources. Decal textures do not support custom sampler, UV index, or swizzle options from [`PhysicallyBasedMaterial`](physicallybasedmaterial.md) parameter types. All textures are sampled using bilinear filtering, projected UVs from the decal volume, and fixed channel mapping. Decals are available on devices with Apple6 GPU family feature support.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct PhysicallyBasedDecalComponent
```

## Topics

### Creating a decal component
- [init(baseColor: PhysicallyBasedMaterial.BaseColor)](physicallybaseddecalcomponent/init(basecolor:).md)
  Creates a new instance with [`PhysicallyBasedMaterial.BaseColor`](physicallybasedmaterial/basecolor-swift.struct.md). The tint color is multiplied with the baseColor. If base color texture is not specified, the tint color is applied as a solid color.
### Configuring decal appearance
- [var opacity: PhysicallyBasedMaterial.Opacity?](physicallybaseddecalcomponent/opacity.md)
  An optional opacity texture for the decal.
### Controlling decal rendering
- [var layers: RenderLayer.Set](physicallybaseddecalcomponent/layers.md)
  The layers this decal affects. Only entities whose [`layers`](renderlayercomponent/layers.md) intersect with these layers will be affected.
- [var sortOrder: Int32](physicallybaseddecalcomponent/sortorder.md)
  The sort layer for the decal. Higher layers show up on top of lower layers.
- [var receiverEntities: Set<Entity>](physicallybaseddecalcomponent/receiverentities.md)
  An optional set of receiver entities that are not part of any layers. The limit on the number of receiver entities is 8, extra entities are ignored.
### Initializers
- [init()](physicallybaseddecalcomponent/init.md)
  Creates a new instance without a base color.
### Instance Properties
- [var baseColor: PhysicallyBasedMaterial.BaseColor?](physicallybaseddecalcomponent/basecolor.md)
  The optional base color texture for the decal. Expects pre-multiplied alpha texture.
- [var bounds: SIMD3<Float>](physicallybaseddecalcomponent/bounds.md)
  The bounds of the decal volume defined in entity local space.
- [var emissive: PhysicallyBasedMaterial.EmissiveColor?](physicallybaseddecalcomponent/emissive.md)
  An optional emissive texture for the decal.
- [var metallic: PhysicallyBasedMaterial.Metallic?](physicallybaseddecalcomponent/metallic.md)
  An optional metallic texture for the decal.
- [var normal: PhysicallyBasedMaterial.Normal?](physicallybaseddecalcomponent/normal.md)
  An optional normal texture for the decal.
- [var roughness: PhysicallyBasedMaterial.Roughness?](physicallybaseddecalcomponent/roughness.md)
  An optional roughness texture for the decal.
- [var specular: PhysicallyBasedMaterial.Specular?](physicallybaseddecalcomponent/specular.md)
  An optional specular texture for the decal.

## Relationships

### Conforms To
- [Component](component.md)
- [Copyable](../swift/copyable.md)
- [Escapable](../swift/escapable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybaseddecalcomponent)*