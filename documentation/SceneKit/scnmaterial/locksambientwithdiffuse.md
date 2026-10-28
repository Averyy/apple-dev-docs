# locksAmbientWithDiffuse

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the material responds identically to both ambient and diffuse lighting. Animatable.

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
var locksAmbientWithDiffuse: Bool { get set }
```

```objc
@property (nonatomic) BOOL locksAmbientWithDiffuse;
```

## Discussion

When modeling real-world lighting, a surface is typically considered to have a single “base” color or texture that is visible under both ambient and diffuse light. When this property’s value is [`false`](../../Swift/false.md), SceneKit does not have this limitation: you may use a material’s [`diffuse`](./diffuse.md) property to provide a color or texture that is visible under direct lighting, and its [`ambient`](./ambient.md) property to provide a different color or texture for areas not directly illuminated.

When this property’s value is [`true`](../../Swift/true.md), or when using the [`physicallyBased`](./lightingmodel-swift.struct/physicallybased.md) shading mode, SceneKit uses the [`diffuse`](./diffuse.md) property for ambient lighting, ignoring the [`ambient`](./ambient.md) property and ensuring that the material responds identically to both ambient and diffuse light.

The default value for this property is [`true`](../../Swift/true.md) for new apps on all platforms. (In OS X v10.9 and earlier, the default value is [`false`](../../Swift/false.md).)

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md). Animating this property fades between the results of rendering with each state.

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
- [var fresnelExponent: CGFloat](./fresnelexponent.md)
  A factor affecting the material’s reflectivity. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/locksambientwithdiffuse)*