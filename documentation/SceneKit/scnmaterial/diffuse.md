# diffuse

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

An object that manages the material’s diffuse response to lighting.

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
var diffuse: SCNMaterialProperty { get }
```

```objc
@property (nonatomic, readonly) SCNMaterialProperty * diffuse;
```

## Discussion

Diffuse shading describes the amount and color of light reflected equally in all directions from each point on the material’s surface. The diffuse color of a pixel is independent of the point of view, so it can be thought of as a material’s “base” color or texture.

By default, the diffuse property’s [`contents`](../scnmaterialproperty/contents.md) object is a white color. The figure below shows the effect of setting the diffuse property’s contents to a texture image on a material whose other properties have default contents.

![](https://developer.apple.com/tutorials/images/com.apple.scenekit/media-2934160@2x.png)

The material’s [`lightingModel`](./lightingmodel-swift.property.md) property determines the formula SceneKit uses to combine its diffuse color and other visual properties with lights and other contents in a scene to produce the final color for each rendered pixel in the rendered scene. For details, see `Lighting Models`.

## See Also

### Related Documentation
- [var specular: SCNMaterialProperty](./specular.md)
  An object that manages the material’s specular response to lighting.
- [var reflective: SCNMaterialProperty](./reflective.md)
  An object that defines the reflected color for each point on a surface.
- [var multiply: SCNMaterialProperty](./multiply.md)
  An object that provides color values that are multiplied with pixels in a material after all other shading is complete.
- [var ambient: SCNMaterialProperty](./ambient.md)
  An object that manages the material’s response to ambient lighting.
- [var normal: SCNMaterialProperty](./normal.md)
  An object that defines the nominal orientation of the surface at each point for use in lighting.
- [var emission: SCNMaterialProperty](./emission.md)
  An object that defines the color emitted by each point on a surface.
- [var transparent: SCNMaterialProperty](./transparent.md)
  An object that determines the opacity of each point in a material.
### Visual Properties for Physically Based Shading
- [var metalness: SCNMaterialProperty](./metalness.md)
  An object that provides color values to determine how metallic the material’s surface appears.
- [var roughness: SCNMaterialProperty](./roughness.md)
  An object that provides color values to determine the apparent smoothness of the surface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/diffuse)*