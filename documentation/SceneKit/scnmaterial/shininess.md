# shininess

**Framework**: SceneKit  
**Kind**: property

The sharpness of specular highlights. Animatable.

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
var shininess: CGFloat { get set }
```

#### Discussion

The shininess of a material interacts with its [`specular`](scnmaterial/specular.md) property and the lighting in a scene to produce bright highlights on a surface. A higher value produces more sharply defined highlights, making a surface appear more smooth and glossy.

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
- [var fresnelExponent: CGFloat](scnmaterial/fresnelexponent.md)
  A factor affecting the material’s reflectivity. Animatable.
- [var locksAmbientWithDiffuse: Bool](scnmaterial/locksambientwithdiffuse.md)
  A Boolean value that determines whether the material responds identically to both ambient and diffuse lighting. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/shininess)*