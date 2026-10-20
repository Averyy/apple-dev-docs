# reflective

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

An object that defines the reflected color for each point on a surface.

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
var reflective: SCNMaterialProperty { get }
```

```objc
@property (nonatomic, readonly) SCNMaterialProperty * reflective;
```

#### Discussion

You can simulate a mirrored or chromed finish on a surface by causing it to reflect its environment. SceneKit does not render real-time reflections of the objects in a scene, but it can use an *environment map* texture to simulate reflection of a static or animated image. When rendering each pixel on the surface, SceneKit traces the light from that point to a pixel in the environment map as if the surface was reflecting that image.

By default, the reflective property’s [`contents`](../scnmaterialproperty/contents.md) object is a white color, causing the property to have no visible effect. Setting the reflective property’s contents to any solid color adds uniform shading to the material. To create a reflective effect, set the property’s contents to an image or other texture-mapped content.

To produce a mirror-finish effect using an environment map, the texture image should take one of two forms:

- A sphere map, a square image whose content depicts an environment as reflected by a mirrored sphere.
- A cube map, an array of six square images which together form an imaginary cube enclosing the scene, whose inner surfaces are reflected by the material. You create a cube map by setting the reflective property’s [`contents`](../scnmaterialproperty/contents.md) object to an [`NSArray`](../../Foundation/nsarray.md) instance containing six images, each corresponding to a direction in the scene’s world coordinate space in the following order: +X, -X, +Y, -Y, +Z, -Z (or Right, Left, Top, Bottom, Near, Far).

The figure below shows a material (with a texture for its [`normal`](./normal.md) property) before and after providing a cube map for the reflective property.

![](https://developer.apple.com/tutorials/images/com.apple.scenekit/media-2934164@2x.png)

This material property does not apply to physically-based materials (see [`physicallyBased`](./lightingmodel-swift.struct/physicallybased.md)). Instead, such materials reflect environment-based lighting (see the [`SCNScene`](../scnscene.md) [`lightingEnvironment`](../scnscene/lightingenvironment.md) property) based on their [`metalness`](./metalness.md) and [`roughness`](./roughness.md) properties.

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

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/reflective)*