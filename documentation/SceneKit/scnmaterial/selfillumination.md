# selfIllumination

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

An object that provides color values representing the global illumination of the surface.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var selfIllumination: SCNMaterialProperty { get }
```

```objc
@property (nonatomic, readonly) SCNMaterialProperty * selfIllumination;
```

#### Discussion

Self-illumination applies to all materials, but is especially useful for those using physically-based shading (see [`physicallyBased`](./lightingmodel-swift.struct/physicallybased.md)). Physically-based materials work best with environment-based lighting (see the [`SCNScene`](../scnscene.md) property [`lightingEnvironment`](../scnscene/lightingenvironment.md)), but for some materials it can be useful to let a surface itself define part of its lighting—for example, an object whose position obscures it from the “sky” that provides the main lighting environment. When you assign contents to this property, they override the environmental lighting contribution to diffuse shading, but environmental lighting still contributes to specular effects.

## See Also

### Visual Properties for Special Effects
- [var normal: SCNMaterialProperty](./normal.md)
  An object that defines the nominal orientation of the surface at each point for use in lighting.
- [var displacement: SCNMaterialProperty](./displacement.md)
- [var emission: SCNMaterialProperty](./emission.md)
  An object that defines the color emitted by each point on a surface.
- [var ambientOcclusion: SCNMaterialProperty](./ambientocclusion.md)
  An object that provides color values to be multiplied with the ambient light affecting the material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/selfillumination)*