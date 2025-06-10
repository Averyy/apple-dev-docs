# sheen

**Framework**: RealityKit  
**Kind**: property

The intensity of an entity’s sheen.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
var sheen: PhysicallyBasedMaterial.SheenColor? { get set }
```

## Mentions

- [Applying realistic material and lighting effects to entities](applying-realistic-material-and-lighting-effects-to-entities.md)

#### Discussion

For a [`PhysicallyBasedMaterial`](physicallybasedmaterial.md), object, you can use `sheen` to add soft specular highlights that simulate subtle reflections like the ones that occur with some materials, primarily fabrics. You can specify `sheen` using a single color, or you can provide a UV-mapped image.

![An illustration showing two spheres. The one on the right has very](https://docs-assets.developer.apple.com/published/359c94162d7f5fc848064f68f22585d1/PhysicallyBasedMaterial-sheen-1%402x.png)

The following example specifies `sheen` using a single value for the entire material:

```swift
let sheenColor = PhysicallyBasedMaterial.Color(deviceRed: 0.8,
green: 0.8, blue: 0.8, alpha: 1.0)
material.sheen = .init(tint:sheenColor)
```

This example shows how to specify sheen using a UV-mapped image texture:

```swift
if let sheenResource = try? TextureResource.load(named:
"entity_sheen") {
    let sheenMap = MaterialParameters.Texture(sheenResource)
    material.sheen = .init(texture: sheenMap)
}
```

## See Also

- [var blending: PhysicallyBasedMaterial.Blending](physicallybasedmaterial/blending-swift.property.md)
  The transparency of an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/sheen)*