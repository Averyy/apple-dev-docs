# multiply

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

An object that provides color values that are multiplied with pixels in a material after all other shading is complete.

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
var multiply: SCNMaterialProperty { get }
```

```objc
@property (nonatomic, readonly) SCNMaterialProperty * multiply;
```

## Discussion

After combining a material’s other visual properties with lighting and other information about a scene, Scene kit multiplies the color of each rendered pixel by the color this property provides. You can use this property to darken or tint a surface independent of the effects of lighting and other properties, or to add precomputed lighting to a scene via a shadow map.

By default, the multiply property’s [`contents`](../scnmaterialproperty/contents.md) object is a white color, causing the property to have no visible effect.

The figure below shows a material (with textures for its [`diffuse`](./diffuse.md) and [`emission`](./emission.md) properties) before and after setting the multiply property’s contents to a solid color. Notice that the multiply color modulates even the bright areas added by the emissive map.

![](https://developer.apple.com/tutorials/images/com.apple.scenekit/media-2934159@2x.png)

## See Also

### Related Documentation
- [var normal: SCNMaterialProperty](./normal.md)
  An object that defines the nominal orientation of the surface at each point for use in lighting.
- [var emission: SCNMaterialProperty](./emission.md)
  An object that defines the color emitted by each point on a surface.
### Visual Properties for Basic Shading
- [var diffuse: SCNMaterialProperty](./diffuse.md)
  An object that manages the material’s diffuse response to lighting.
- [var ambient: SCNMaterialProperty](./ambient.md)
  An object that manages the material’s response to ambient lighting.
- [var specular: SCNMaterialProperty](./specular.md)
  An object that manages the material’s specular response to lighting.
- [var reflective: SCNMaterialProperty](./reflective.md)
  An object that defines the reflected color for each point on a surface.
- [var transparent: SCNMaterialProperty](./transparent.md)
  An object that determines the opacity of each point in a material.
- [var shininess: CGFloat](./shininess.md)
  The sharpness of specular highlights. Animatable.
- [var fresnelExponent: CGFloat](./fresnelexponent.md)
  A factor affecting the material’s reflectivity. Animatable.
- [var locksAmbientWithDiffuse: Bool](./locksambientwithdiffuse.md)
  A Boolean value that determines whether the material responds identically to both ambient and diffuse lighting. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/multiply)*