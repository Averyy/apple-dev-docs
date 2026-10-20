# transparent

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

An object that determines the opacity of each point in a material.

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
var transparent: SCNMaterialProperty { get }
```

```objc
@property (nonatomic, readonly) SCNMaterialProperty * transparent;
```

#### Discussion

Use this property to selectively make parts of a material appear transparent. You can uniformly adjust the opacity of a material using its [`transparency`](./transparency.md) property, or of all the content attached to a node using the node’s [`opacity`](../scnnode/opacity.md) property.

By default, the transparent property’s [`contents`](../scnmaterialproperty/contents.md) object is a fully opaque black color, causing the property to have no visible effect. Setting the transparent property’s contents to any solid color uniformly fades the opacity of the material based on that color’s opacity value. To make parts of a material appear transparent, set the property’s contents to an image or other texture-mapped content whose alpha channel defines areas of full or partial opacity.

The figure below shows a semitransparent material before and after providing a texture image for its transparent property. (To make the transparency effect more visible, a blue sphere is shown behind the transparent material.)

![](https://developer.apple.com/tutorials/images/com.apple.scenekit/media-2934166@2x.png)

The [`transparencyMode`](./transparencymode.md) property controls how SceneKit interprets color information from the transparent property’s contents.

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
- [var multiply: SCNMaterialProperty](./multiply.md)
  An object that provides color values that are multiplied with pixels in a material after all other shading is complete.
- [var shininess: CGFloat](./shininess.md)
  The sharpness of specular highlights. Animatable.
- [var fresnelExponent: CGFloat](./fresnelexponent.md)
  A factor affecting the material’s reflectivity. Animatable.
- [var locksAmbientWithDiffuse: Bool](./locksambientwithdiffuse.md)
  A Boolean value that determines whether the material responds identically to both ambient and diffuse lighting. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/transparent)*