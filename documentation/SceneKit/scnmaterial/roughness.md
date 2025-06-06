# roughness

**Framework**: SceneKit  
**Kind**: property

An object that provides color values to determine the apparent smoothness of the surface.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var roughness: SCNMaterialProperty { get }
```

#### Discussion

This property measures only the total intensity of color values; texture contents are best defined in grayscale.

This property approximates the level of microscopic detail—for example tiny bumps and cracks—in a surface. By approximating these “microfacets” as a single term, this property helps produce lighting calculations that resemble the energy-conserving laws of real-world physics, resulting in more realistic variation between matte and shiny surfaces. Lower values (darker colors) cause the material to appear shiny, with well-defined specular highlights. Higher values (brighter colors) cause specular highlights to spread out and the diffuse color of the material to become more retroreflective.

This property applies only when the material’s [`lightingModel`](scnmaterial/lightingmodel-swift.property.md) value is [`physicallyBased`](scnmaterial/lightingmodel-swift.struct/physicallybased.md).

## See Also

- [var diffuse: SCNMaterialProperty](scnmaterial/diffuse.md)
  An object that manages the material’s diffuse response to lighting.
- [var metalness: SCNMaterialProperty](scnmaterial/metalness.md)
  An object that provides color values to determine how metallic the material’s surface appears.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/roughness)*