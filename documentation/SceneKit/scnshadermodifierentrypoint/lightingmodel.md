# lightingModel

**Framework**: SceneKit  
**Kind**: property

Use this entry point to provide a custom lighting equation.

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
static let lightingModel: SCNShaderModifierEntryPoint
```

#### Discussion

Shader modifiers for this entry point may execute in either the vertex or fragment processing stage. If the litPerPixel property of a material affected by the shader modifier is [`true`](https://developer.apple.com/documentation/swift/true), the snippet executes in the fragment processing stage; otherwise the snippet executes in the vertex processing stage.

The surface entry point defines the following structures:

```objc
struct SCNShaderLightingContribution {
   vec3 ambient;
   vec3 diffuse;
   vec3 specular;
} _lightingContribution;
 
struct SCNShaderLight {
   vec4 intensity;
   vec3 direction; // Direction from the point on the surface toward the light (L)
} _light;
```

When rendering a fragment, SceneKit executes this shader modifier once for each active light in the scene. Your shader modifier reads from the `_light` structure and accumulates the results of your lighting computations into the `_lightingContribution` structure. After your shader modifier completes, SceneKit’s shader program combines the lighting contribution with the surface properties to determine the fragment’s color.

All fields in the `_lightingContribution` structure and the `intensity` field in the `_light` structure are colors. The `direction` field is expressed in view space.

The shader modifier below wraps diffuse lighting—that is, it increases all input lighting values by `0.5`, and if the resulting value is greater than `1.0` it “wraps around” back to `0.0`:

```objc
uniform float WrapFactor = 0.5;
 
float dotProduct = (WrapFactor + max(0.0, dot(_surface.normal,_light.direction))) / (1 + WrapFactor);
_lightingContribution.diffuse += (dotProduct * _light.intensity.rgb);
vec3 halfVector = normalize(_light.direction + _surface.view);
dotProduct = max(0.0, pow(max(0.0, dot(_surface.normal, halfVector)), _surface.shininess));
_lightingContribution.specular += (dotProduct * _light.intensity.rgb);
```

## See Also

- [static let fragment: SCNShaderModifierEntryPoint](scnshadermodifierentrypoint/fragment.md)
  Use this entry point to change the color of a fragment after all other shading has been performed.
- [static let geometry: SCNShaderModifierEntryPoint](scnshadermodifierentrypoint/geometry.md)
  Use this entry point to deform a geometry’s surface or alter its vertex attributes.
- [static let surface: SCNShaderModifierEntryPoint](scnshadermodifierentrypoint/surface.md)
  Use this entry point to modify the surface properties of a material before lighting is computed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnshadermodifierentrypoint/lightingmodel)*