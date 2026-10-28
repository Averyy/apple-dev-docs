# blending

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The transparency of an entity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
var blending: PhysicallyBasedMaterial.Blending { get set }
```

## Mentions

- [Applying realistic material and lighting effects to entities](../applying-realistic-material-and-lighting-effects-to-entities.md)

## Discussion

Use this property to specify whether an entity is opaque or transparent. To create an entity that’s opaque, assign [`PhysicallyBasedMaterial.Blending.opaque`](./blending-swift.enum/opaque.md) to this property.

```swift
material.blending = .opaque
```

To create a translucent or transparent object using a single opacity value for the entire material, initialize [`PhysicallyBasedMaterial.Blending.transparent(opacity:)`](./blending-swift.enum/transparent%28opacity%29.md) using a `Float` value.

```swift
material.blending = .transparent(opacity: .init(floatLiteral:0.5))
```

To use a UV-mapped grayscale image texture to specify different opacity values for different parts of an entity, initialize [`PhysicallyBasedMaterial.Blending.transparent(opacity:)`](./blending-swift.enum/transparent%28opacity%29.md) using a texture. If you provide a color image, RealityKit only uses the intensity of the red channel.

```swift
if let opacityResource = try? TextureResource.load(named:
"entity_opacity") {
    let opacityMap = MaterialParameters.Texture(opacityResource)
    material.blending = .transparent(opacity: .init(texture: opacityMap))
}
```

## See Also

### Configuring transparency and highlights
- [var sheen: PhysicallyBasedMaterial.SheenColor?](./sheen.md)
  The intensity of an entity’s sheen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/blending-swift.property)*