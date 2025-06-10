# selfIllumination

**Framework**: SceneKit  
**Kind**: property

An object that provides color values representing the global illumination of the surface.

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
var selfIllumination: SCNMaterialProperty { get }
```

#### Discussion

Self-illumination applies to all materials, but is especially useful for those using physically-based shading (see [`physicallyBased`](scnmaterial/lightingmodel-swift.struct/physicallybased.md)). Physically-based materials work best with environment-based lighting (see the [`SCNScene`](scnscene.md) property [`lightingEnvironment`](scnscene/lightingenvironment.md)), but for some materials it can be useful to let a surface itself define part of its lighting—for example, an object whose position obscures it from the “sky” that provides the main lighting environment. When you assign contents to this property, they override the environmental lighting contribution to diffuse shading, but environmental lighting still contributes to specular effects.

## See Also

- [var normal: SCNMaterialProperty](scnmaterial/normal.md)
  An object that defines the nominal orientation of the surface at each point for use in lighting.
- [var displacement: SCNMaterialProperty](scnmaterial/displacement.md)
- [var emission: SCNMaterialProperty](scnmaterial/emission.md)
  An object that defines the color emitted by each point on a surface.
- [var ambientOcclusion: SCNMaterialProperty](scnmaterial/ambientocclusion.md)
  An object that provides color values to be multiplied with the ambient light affecting the material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/selfillumination)*