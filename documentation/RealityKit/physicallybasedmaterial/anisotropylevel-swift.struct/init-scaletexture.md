# init(scale:texture:)

**Framework**: RealityKit  
**Kind**: init

Creates an anisotropy level object using a single value or a texture.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
init(scale: Float = 1.0, texture: PhysicallyBasedMaterial.Texture? = nil)
```

#### Discussion

By default, PBR materials are isotropic; in other words, an entity that uses [`PhysicallyBasedMaterial`](physicallybasedmaterial.md) reflects light uniformly in all directions, mimicking the behavior of most real-world objects. Some objects, including those with many small parallel striations such as vinyl records, CDs, or straight hair, reflect light more in some directions than others, resulting in stretched or oblong specular highlights, as shown in the following figure.

![An illustration showing 11 metallic spheres in a horizontal row.](https://docs-assets.developer.apple.com/published/6f0766c25dba1110d0837ce67286adee/PhysicallyBasedMaterial-AnisotropyLevel-swift-struct-init%28scale%3Atexture%3A%29-1%402x.png)

Use this initializer to create an object to set the [`anisotropyLevel`](physicallybasedmaterial/anisotropylevel-swift.property.md) for a material using either a single value for the entire material, or a UV-mapped image. If you specify `texture`, RealityKit calculates the anistotropy level for the entity by UV-mapping `texture` onto the entity and multiplying the value of each mapped pixel by `scale`. If you don’t specify `texture`, then RealityKit uses `scale` as the entire entity’s anisotropy level. If you provide a color image for `texture` rather than a grayscale image, RealityKit only uses the intensity of the image’s red channel.

## Parameters

- `scale`: The anisotropy level value for the entire material.
- `texture`: The anisotropy level values as a UV-mapped image.

## See Also

- [init(floatLiteral: Float)](physicallybasedmaterial/anisotropylevel-swift.struct/init(floatliteral:).md)
  Creates an anisotropy level object from a single value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/anisotropylevel-swift.struct/init(scale:texture:))*