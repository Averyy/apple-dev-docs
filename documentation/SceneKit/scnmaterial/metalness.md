# metalness

**Framework**: SceneKit  
**Kind**: property

An object that provides color values to determine how metallic the material’s surface appears.

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
var metalness: SCNMaterialProperty { get }
```

#### Discussion

This property measures only the total intensity of color values; texture contents are best defined in grayscale.

This property generally approximates aspects of a physical surface—such as index of refraction, tendency to produce sharp reflections, and tendency to produce Fresnel reflections at grazing angles—that together produce an overall metallic or nonmetallic (also called dielectric) appearance. Lower values (darker colors) cause the material to appear more like a dielectric surface. Higher values (brighter colors) cause the surface to appear more metallic.

This property applies only when the material’s [`lightingModel`](scnmaterial/lightingmodel-swift.property.md) value is [`physicallyBased`](scnmaterial/lightingmodel-swift.struct/physicallybased.md).

## See Also

- [var diffuse: SCNMaterialProperty](scnmaterial/diffuse.md)
  An object that manages the material’s diffuse response to lighting.
- [var roughness: SCNMaterialProperty](scnmaterial/roughness.md)
  An object that provides color values to determine the apparent smoothness of the surface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/metalness)*