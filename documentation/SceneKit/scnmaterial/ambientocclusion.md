# ambientOcclusion

**Framework**: SceneKit  
**Kind**: property

An object that provides color values to be multiplied with the ambient light affecting the material.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var ambientOcclusion: SCNMaterialProperty { get }
```

#### Discussion

Use this property to assign an ambient occlusion texture map to a surface. This property has no effect if there is no ambient light in the scene. If this property is not `nil`, SceneKit ignores the [`ambient`](scnmaterial/ambient.md) property.

When using physically-based shading (see [`physicallyBased`](scnmaterial/lightingmodel-swift.struct/physicallybased.md)), ambient occlusion approximates large-scale surface details that obscure global illumination.

## See Also

- [var normal: SCNMaterialProperty](scnmaterial/normal.md)
  An object that defines the nominal orientation of the surface at each point for use in lighting.
- [var displacement: SCNMaterialProperty](scnmaterial/displacement.md)
- [var emission: SCNMaterialProperty](scnmaterial/emission.md)
  An object that defines the color emitted by each point on a surface.
- [var selfIllumination: SCNMaterialProperty](scnmaterial/selfillumination.md)
  An object that provides color values representing the global illumination of the surface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/ambientocclusion)*