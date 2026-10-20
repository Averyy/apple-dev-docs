# ambientOcclusion

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

An object that provides color values to be multiplied with the ambient light affecting the material.

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
var ambientOcclusion: SCNMaterialProperty { get }
```

```objc
@property (nonatomic, readonly) SCNMaterialProperty * ambientOcclusion;
```

#### Discussion

Use this property to assign an ambient occlusion texture map to a surface. This property has no effect if there is no ambient light in the scene. If this property is not `nil`, SceneKit ignores the [`ambient`](./ambient.md) property.

When using physically-based shading (see [`physicallyBased`](./lightingmodel-swift.struct/physicallybased.md)), ambient occlusion approximates large-scale surface details that obscure global illumination.

## See Also

### Visual Properties for Special Effects
- [var normal: SCNMaterialProperty](./normal.md)
  An object that defines the nominal orientation of the surface at each point for use in lighting.
- [var displacement: SCNMaterialProperty](./displacement.md)
- [var emission: SCNMaterialProperty](./emission.md)
  An object that defines the color emitted by each point on a surface.
- [var selfIllumination: SCNMaterialProperty](./selfillumination.md)
  An object that provides color values representing the global illumination of the surface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/ambientocclusion)*