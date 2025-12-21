# ambient

**Framework**: SceneKit  
**Kind**: property

An object that manages the material’s response to ambient lighting.

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
var ambient: SCNMaterialProperty { get }
```

#### Discussion

Ambient shading describes the amount and color of ambient light reflected by the material. Ambient shading is uniform in all directions at all points on a surface. If a scene does not contain lights whose type is [`ambient`](scnlight/lighttype/ambient.md), this property has no effect on a material’s appearance.

By default, the ambient property’s [`contents`](scnmaterialproperty/contents.md) object is a dark gray color. Changing the ambient property’s contents lets you specify a different color or texture for the areas of a surface not directly illuminated by lights in a scene. To make the material respond identically to both ambient and diffuse light, set its [`locksAmbientWithDiffuse`](scnmaterial/locksambientwithdiffuse.md) property to [`true`](https://developer.apple.com/documentation/Swift/true).

The figure below shows a material (with a texture for its [`diffuse`](scnmaterial/diffuse.md) property) before and after setting the ambient property’s contents to a solid color.

![None](https://docs-assets.developer.apple.com/published/fb3885ad46a4a3606bfee6d4cd4b3cb7/media-2934161%402x.png)

The material’s [`lightingModel`](scnmaterial/lightingmodel-swift.property.md) property determines the formula SceneKit uses to combine its ambient color and other visual properties with lights and other contents in a scene to produce the final color for each rendered pixel in the rendered scene. For details, see `Lighting Models`.

This material property does not apply to physically-based materials (see [`physicallyBased`](scnmaterial/lightingmodel-swift.struct/physicallybased.md)).

## See Also

- [var normal: SCNMaterialProperty](scnmaterial/normal.md)
  An object that defines the nominal orientation of the surface at each point for use in lighting.
- [var emission: SCNMaterialProperty](scnmaterial/emission.md)
  An object that defines the color emitted by each point on a surface.
- [var diffuse: SCNMaterialProperty](scnmaterial/diffuse.md)
  An object that manages the material’s diffuse response to lighting.
- [var specular: SCNMaterialProperty](scnmaterial/specular.md)
  An object that manages the material’s specular response to lighting.
- [var reflective: SCNMaterialProperty](scnmaterial/reflective.md)
  An object that defines the reflected color for each point on a surface.
- [var multiply: SCNMaterialProperty](scnmaterial/multiply.md)
  An object that provides color values that are multiplied with pixels in a material after all other shading is complete.
- [var transparent: SCNMaterialProperty](scnmaterial/transparent.md)
  An object that determines the opacity of each point in a material.
- [var shininess: CGFloat](scnmaterial/shininess.md)
  The sharpness of specular highlights. Animatable.
- [var fresnelExponent: CGFloat](scnmaterial/fresnelexponent.md)
  A factor affecting the material’s reflectivity. Animatable.
- [var locksAmbientWithDiffuse: Bool](scnmaterial/locksambientwithdiffuse.md)
  A Boolean value that determines whether the material responds identically to both ambient and diffuse lighting. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/ambient)*