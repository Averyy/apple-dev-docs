# PhysicallyBasedDecalComponent

**Framework**: RealityKit  
**Kind**: struct

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
  Creates a new instance with PhysicallBasedMaterial.BaseColor The tint color is multiplied with the baseColor If base color is not specified, the tint color is applied as a solid color
### Configuring decal appearance
- [var opacity: PhysicallyBasedMaterial.Opacity?](physicallybaseddecalcomponent/opacity.md)
  An optional opacity texture for the decal
### Controlling decal rendering
- [var layers: RenderLayer.Set](physicallybaseddecalcomponent/layers.md)
  The layers this decal affects. Only entities whose RenderLayerComponent.layers intersect with these layers will be affected.
- [var sortOrder: Int32](physicallybaseddecalcomponent/sortorder.md)
  The sort layer for the decal Higher layers show up on top of lower layers
- [var receiverEntities: Set<Entity>](physicallybaseddecalcomponent/receiverentities.md)
  An optional set of receiver entities that are not part of any layers The limit on the number of receiver entities is 8, extra entities are ignored
### Initializers
- [init()](physicallybaseddecalcomponent/init.md)
  Creates a new instance without a base color
### Instance Properties
- [var baseColor: PhysicallyBasedMaterial.BaseColor?](physicallybaseddecalcomponent/basecolor.md)
  The optional base color texture for the decal Expects pre-multiplied alpha texture
- [var bounds: SIMD3<Float>](physicallybaseddecalcomponent/bounds.md)
  The bounds of the decal volume defined in entity local space
- [var emissive: PhysicallyBasedMaterial.EmissiveColor?](physicallybaseddecalcomponent/emissive.md)
  An optional emissive  texture for the decal
- [var metallic: PhysicallyBasedMaterial.Metallic?](physicallybaseddecalcomponent/metallic.md)
  An optional metallic texture for the decal
- [var normal: PhysicallyBasedMaterial.Normal?](physicallybaseddecalcomponent/normal.md)
  An optional normal texture for the decal
- [var roughness: PhysicallyBasedMaterial.Roughness?](physicallybaseddecalcomponent/roughness.md)
  An optional roughness texture for the decal
- [var specular: PhysicallyBasedMaterial.Specular?](physicallybaseddecalcomponent/specular.md)
  An optional specular  texture for the decal

## Relationships

### Conforms To
- [Component](component.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybaseddecalcomponent)*