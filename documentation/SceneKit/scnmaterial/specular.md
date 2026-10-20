# specular

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

An object that manages the material’s specular response to lighting.

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
var specular: SCNMaterialProperty { get }
```

```objc
@property (nonatomic, readonly) SCNMaterialProperty * specular;
```

#### Discussion

Specular shading describes the amount and color of light reflected by the material directly toward the viewer, forming a bright highlight on the surface and simulating a glossy or shiny appearance. You adjust the sharpness of specular highlights using the material’s [`shininess`](./shininess.md) property.

By default, the specular property’s [`contents`](../scnmaterialproperty/contents.md) object is a black color, causing the material to appear dull or matte. Changing the specular property’s contents to a brighter color causes specular highlights to appear in that color, making the surface appear shiny. When you apply a texture to the specular property, the texture image becomes a *specular map*—the brightness of each pixel in the image determines the tendency of each point on the material’s surface to create specular highlights when lit.

The figure below shows a material (with a texture for its [`diffuse`](./diffuse.md) property) before and after providing a specular map image. Notice that the bright specular highlights appear only on portions of the surface where the specular map image is white.

![](https://developer.apple.com/tutorials/images/com.apple.scenekit/media-2934162@2x.png)

The material’s [`lightingModel`](./lightingmodel-swift.property.md) property determines the formula SceneKit uses to combine its specularity and other visual properties with lights and other contents in a scene to produce the final color for each rendered pixel in the rendered scene. For details, see `Lighting Models`.

This material property does not apply to physically-based materials (see [`physicallyBased`](./lightingmodel-swift.struct/physicallybased.md)).

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
- [var reflective: SCNMaterialProperty](./reflective.md)
  An object that defines the reflected color for each point on a surface.
- [var multiply: SCNMaterialProperty](./multiply.md)
  An object that provides color values that are multiplied with pixels in a material after all other shading is complete.
- [var transparent: SCNMaterialProperty](./transparent.md)
  An object that determines the opacity of each point in a material.
- [var shininess: CGFloat](./shininess.md)
  The sharpness of specular highlights. Animatable.
- [var fresnelExponent: CGFloat](./fresnelexponent.md)
  A factor affecting the material’s reflectivity. Animatable.
- [var locksAmbientWithDiffuse: Bool](./locksambientwithdiffuse.md)
  A Boolean value that determines whether the material responds identically to both ambient and diffuse lighting. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/specular)*