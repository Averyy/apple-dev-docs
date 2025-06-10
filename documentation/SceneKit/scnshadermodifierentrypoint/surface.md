# surface

**Framework**: SceneKit  
**Kind**: property

Use this entry point to modify the surface properties of a material before lighting is computed.

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
static let surface: SCNShaderModifierEntryPoint
```

#### Discussion

Shader modifiers for this entry point execute in the fragment processing stage.

The surface entry point defines the following structure:

```objc
struct SCNShaderSurface {
   vec3 view;                // Direction from the point on the surface toward the camera (V)
   vec3 position;            // Position of the fragment
   vec3 normal;              // Normal of the fragment (N)
   vec3 tangent;             // Tangent of the fragment
   vec3 bitangent;           // Bitangent of the fragment
   vec4 ambient;             // Ambient property of the fragment
   vec2 ambientTexcoord;     // Ambient texture coordinates
   vec4 diffuse;             // Diffuse property of the fragment. Alpha contains the opacity.
   vec2 diffuseTexcoord;     // Diffuse texture coordinates
   vec4 specular;            // Specular property of the fragment
   vec2 specularTexcoord;    // Specular texture coordinates
   vec4 emission;            // Emission property of the fragment
   vec2 emissionTexcoord;    // Emission texture coordinates
   vec4 multiply;            // Multiply property of the fragment
   vec2 multiplyTexcoord;    // Multiply texture coordinates
   vec4 transparent;         // Transparent property of the fragment
   vec2 transparentTexcoord; // Transparent texture coordinates
   vec4 reflective;          // Reflective property of the fragment
   float shininess;          // Shininess property of the fragment.
   float fresnel;            // Fresnel property of the fragment.
} _surface;
```

Your shader modifier reads from this structure and writes new values to the same structure to alter the surface properties of each rendered fragment. After your shader modifier completes, SceneKit’s shader program uses these properties to compute lighting.

Geometric fields (such as `position` and `normal`) are expressed in view space. You can use SceneKit’s uniforms (such as `u_inverseViewTransform`) to operate in a different coordinate space, but you must convert back to view space before writing results.

Other fields of type `vec4` are colors provided by the contents of the corresponding [`SCNMaterialProperty`](scnmaterialproperty.md) object. Texture coordinate fields contain values transformed by the relevant material property’s [`contentsTransform`](scnmaterialproperty/contentstransform.md) transformation.

The below shader modifier produces black and white stripes on a surface:

```objc
uniform float Scale = 12.0;
uniform float Width = 0.25;
uniform float Blend = 0.3;
 
vec2 position = fract(_surface.diffuseTexcoord * Scale);
float f1 = clamp(position.y / Blend, 0.0, 1.0);
float f2 = clamp((position.y - Width) / Blend, 0.0, 1.0);
f1 = f1 * (1.0 - f2);
f1 = f1 * f1 * 2.0 * (3. * 2. * f1);
_surface.diffuse = mix(vec4(1.0), vec4(0.0), f1);
```

## See Also

- [static let fragment: SCNShaderModifierEntryPoint](scnshadermodifierentrypoint/fragment.md)
  Use this entry point to change the color of a fragment after all other shading has been performed.
- [static let geometry: SCNShaderModifierEntryPoint](scnshadermodifierentrypoint/geometry.md)
  Use this entry point to deform a geometry’s surface or alter its vertex attributes.
- [static let lightingModel: SCNShaderModifierEntryPoint](scnshadermodifierentrypoint/lightingmodel.md)
  Use this entry point to provide a custom lighting equation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnshadermodifierentrypoint/surface)*