# init(scale:texture:)

**Framework**: RealityKit  
**Kind**: init

Creates a clearcoat roughness object using a single value or a texture.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
init(scale: Float = 1.0, texture: PhysicallyBasedMaterial.Texture? = nil)
```

#### Discussion

A clearcoat is a separate layer of transparent specular highlights used to simulate a clear transparent coating, like the paint on a car, or the surface of lacquered objects. When you enable clearcoat rendering for a material, RealityKit renders the clearcoat as a separate layer just above the surface of the entity. You can specify a clearcoat roughness value for the clearcoat to indicate how much the clearcoat scatters light that bounces off of it, which softens and spreads out the highlights.

This initializer creates an object that specifies the clearcoat roughness for a material using a single value for the entire material, a UV-mapped image, or both.

If you specify `texture`, RealityKit calculates the clearcoat roughness for the entity by UV-mapping `texture` onto the entity and multiplying the value of each mapped pixel by `scale`. If you don’t specify a `texture`, then RealityKit uses `scale` as the entire entity’s clearcoat roughness. If you provide a color image for `texture` rather than a grayscale image, RealityKit only uses the intensity of the image’s red channel.

## Parameters

- `scale`: The clearcoat roughness value for the entire material.
- `texture`: The clearcoat roughness values as a UV-mapped image.

## See Also

- [init(floatLiteral: Float)](physicallybasedmaterial/clearcoatroughness-swift.struct/init(floatliteral:).md)
  Creates a clearcoat roughness object using a single value.
- [init(CustomMaterial.ClearcoatRoughness)](physicallybasedmaterial/clearcoatroughness-swift.struct/init(_:).md)
  Creates a clearcoat roughness object from a custom material’s clearcoat roughness property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/clearcoatroughness-swift.struct/init(scale:texture:))*