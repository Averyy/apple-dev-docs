# fresnelExponent

**Framework**: SceneKit  
**Kind**: property

A factor affecting the material’s reflectivity. Animatable.

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
var fresnelExponent: CGFloat { get set }
```

#### Discussion

The Fresnel exponent of a material interacts with its [`reflective`](scnmaterial/reflective.md) property to determine the intensity of reflections in a surface based on its angle relative to the viewer. A higher Fresnel exponent increases the visibility of reflections when the material is viewed from a shallow angle.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var diffuse: SCNMaterialProperty](scnmaterial/diffuse.md)
  An object that manages the material’s diffuse response to lighting.
- [var ambient: SCNMaterialProperty](scnmaterial/ambient.md)
  An object that manages the material’s response to ambient lighting.
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
- [var locksAmbientWithDiffuse: Bool](scnmaterial/locksambientwithdiffuse.md)
  A Boolean value that determines whether the material responds identically to both ambient and diffuse lighting. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/fresnelexponent)*