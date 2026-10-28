# fresnelExponent

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A factor affecting the material’s reflectivity. Animatable.

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
var fresnelExponent: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat fresnelExponent;
```

## Discussion

The Fresnel exponent of a material interacts with its [`reflective`](./reflective.md) property to determine the intensity of reflections in a surface based on its angle relative to the viewer. A higher Fresnel exponent increases the visibility of reflections when the material is viewed from a shallow angle.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

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
- [var transparent: SCNMaterialProperty](./transparent.md)
  An object that determines the opacity of each point in a material.
- [var shininess: CGFloat](./shininess.md)
  The sharpness of specular highlights. Animatable.
- [var locksAmbientWithDiffuse: Bool](./locksambientwithdiffuse.md)
  A Boolean value that determines whether the material responds identically to both ambient and diffuse lighting. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/fresnelexponent)*