# locksAmbientWithDiffuse

**Framework**: SceneKit  
**Kind**: property

A Boolean value that determines whether the material responds identically to both ambient and diffuse lighting. Animatable.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var locksAmbientWithDiffuse: Bool { get set }
```

#### Discussion

When modeling real-world lighting, a surface is typically considered to have a single “base” color or texture that is visible under both ambient and diffuse light. When this property’s value is [`false`](https://developer.apple.com/documentation/swift/false), SceneKit does not have this limitation: you may use a material’s [`diffuse`](scnmaterial/diffuse.md) property to provide a color or texture that is visible under direct lighting, and its [`ambient`](scnmaterial/ambient.md) property to provide a different color or texture for areas not directly illuminated.

When this property’s value is [`true`](https://developer.apple.com/documentation/swift/true), or when using the [`physicallyBased`](scnmaterial/lightingmodel-swift.struct/physicallybased.md) shading mode, SceneKit uses the [`diffuse`](scnmaterial/diffuse.md) property for ambient lighting, ignoring the [`ambient`](scnmaterial/ambient.md) property and ensuring that the material responds identically to both ambient and diffuse light.

The default value for this property is [`true`](https://developer.apple.com/documentation/swift/true) for new apps on all platforms. (In OS X v10.9 and earlier, the default value is [`false`](https://developer.apple.com/documentation/swift/false).)

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md). Animating this property fades between the results of rendering with each state.

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
- [var fresnelExponent: CGFloat](scnmaterial/fresnelexponent.md)
  A factor affecting the material’s reflectivity. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/locksambientwithdiffuse)*