# fragment

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

Use this entry point to change the color of a fragment after all other shading has been performed.

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
static let fragment: SCNShaderModifierEntryPoint
```

```c
extern SCNShaderModifierEntryPoint const SCNShaderModifierEntryPointFragment;
```

#### Discussion

Shader modifiers for this entry point execute in the fragment processing stage.

The fragment entry point defines the following structure:

```objc
struct SCNShaderOutput {
   vec4 color;
} _output;
```

Your shader modifier reads from this structure and writes a new color to the same structure to produce the final output color for each rendered fragment.

This shader modifier inverts the output color:

```objc
_output.color.rgb = vec3(1.0) - _output.color.rgb;
```

## See Also

### Type Properties
- [static let geometry: SCNShaderModifierEntryPoint](./geometry.md)
  Use this entry point to deform a geometry’s surface or alter its vertex attributes.
- [static let lightingModel: SCNShaderModifierEntryPoint](./lightingmodel.md)
  Use this entry point to provide a custom lighting equation.
- [static let surface: SCNShaderModifierEntryPoint](./surface.md)
  Use this entry point to modify the surface properties of a material before lighting is computed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnshadermodifierentrypoint/fragment)*