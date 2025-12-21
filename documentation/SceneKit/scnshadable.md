# SCNShadable

**Framework**: SceneKit  
**Kind**: protocol

Methods for customizing SceneKit’s rendering of geometry and materials using Metal or OpenGL shader programs.

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
protocol SCNShadable : NSObjectProtocol
```

#### Overview

SceneKit provides two ways to integrate custom GPU shader programs into the rendering of your scene: program objects and shader modifiers.

##### Use Program Objects to Replace Scenekit Shading

For complete control of the vertex and fragment shaders used to render an object, assign an [`SCNProgram`](scnprogram.md) instance to the object’s program property. A custom program completely replaces all other rendering parameters, including material settings. Your custom program takes inputs from SceneKit and is responsible for all transform, lighting, and shading effects you want it to produce. For details on custom programs, see [`SCNProgram`](scnprogram.md).

When you specify a custom program, you can provide handler blocks that SceneKit calls at render time to update the values of custom variables in your shaders. See the methods in Handling Parameters in Custom OpenGL Shader Programs.

##### Use Shader Modifiers to Extend Scenekit Shading

Shader modifiers are an alternative to entirely replacing SceneKit’s shaders with your own. You can use shader modifiers to, for example:

- Parametrically deform the surface of a geometry
- Simulate realistic surfaces with complex material properties
- Add artistic lighting effects such as cartoon-style shading
- Create special effects by post-processing pixels after SceneKit’s shading is complete

A shader modifier is a snippet of source code in the Metal shader language or OpenGL Shader Language (GLSL) that SceneKit injects into its own shader programs at a defined entry point. Because your shader modifiers are additions to SceneKit’s shader program, using shader modifiers leaves SceneKit’s rendering system intact. That is, you can still use material properties, lighting models, and camera effects to affect the rendered image.

You attach a snippet to a [`SCNGeometry`](scngeometry.md) or [`SCNMaterial`](scnmaterial.md) object using its [`shaderModifiers`](scnshadable/shadermodifiers.md) property, associating it with an entry point corresponding to the stage of SceneKit’s shader program that it modifies: geometry, surface, lighting, or fragment. Each entry point defines a context for the associated snippet, with input variables providing SceneKit’s rendering parameters in that stage and output variables that the snippet writes its results to.

For definitions of each entry point and its inputs and outputs, see `Shader Modifier Entry Point Keys`. SceneKit inserts your shader modifiers into its shader program a specific order:

1. [`geometry`](scnshadermodifierentrypoint/geometry.md)
2. [`surface`](scnshadermodifierentrypoint/surface.md)
3. [`lightingModel`](scnshadermodifierentrypoint/lightingmodel.md)
4. [`fragment`](scnshadermodifierentrypoint/fragment.md)

You can use the structures defined by earlier entry points in later entry points. For example, a snippet associated with the [`fragment`](scnshadermodifierentrypoint/fragment.md) entry point can read from the `_surface` structure defined by the [`surface`](scnshadermodifierentrypoint/surface.md) entry point.

###### Writing a Shader Modifier Snippet

The code you provide for a shader modifier must be organized in a specific structure, as illustrated in the example below:

```objc
// 1. Custom variable declarations (optional)
// For Metal, a pragma directive and one custom variable on each line:
#pragma arguments
float intensity;
// For OpenGL, a separate uniform declaration for each custom variable
uniform float intensity;
 
// 2. Custom global functions (optional)
vec2 sincos(float t) { return vec2(sin(t), cos(t)); }
 
// 3. Pragma directives (optional)
#pragma transparent
#pragma body
 
// 4. Code snippet
_geometry.position.xy = sincos(u_time);
_geometry.position.z = intensity;
```

1.  You can provide your own inputs to a shader modifier by declaring custom variables. Because the syntax differs between Metal and OpenGL shaders, you must include both declarations for your shader modifier to be usable with both rendering technologies. To pass values into custom variables at render time, see [`Providing Custom Inputs to a Shader Modifier`](scnshadable#Providing-Custom-Inputs-to-a-Shader-Modifier.md).
2.  If your shader modifier benefits from factoring common code into functions, place their definitions here. If you include custom functions in your snippet, you must place the `#pragma body` directive between your function definitions and the main body of the snippet.
3.  As noted above, the `#pragma body` directive separates custom function definitions from the main body of the snippet. If the snippet contains no function definitions, you may omit this directive.

By default, SceneKit automatically uses material properties to determine whether an object should be rendered with partial transparency and uses this information to optimize rendering performance. Use the `#pragma transparent` or `#pragma opaque` directive to override SceneKit’s setting. 4.  Place the main body of your shader modifier code at the end of the code snippet.

One shader modifier snippet affects both Metal and OpenGL (or OpenGL ES) rendering—SceneKit automatically translates GLSL syntax to Metal shader syntax before inserting your code snippet into its own shader program. (For some simple shader modifiers, SceneKit can insert the same code snippet into either shader language without translation.)

###### Providing Custom Inputs to a Shader Modifier

You can also declare custom uniform variables in your shader modifier snippet. You provide values for custom uniform variables using [`Key-value coding`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KeyValueCoding.html#//apple_ref/doc/uid/TP40008195-CH25). For each uniform variable you declare in a shader modifier attached to an [`SCNMaterial`](scnmaterial.md) or [`SCNGeometry`](scngeometry.md) object, SceneKit observes a key with the same name on that object. When you set a new value, SceneKit automatically binds that value to the corresponding uniform location in the shader program. If you animate a change to the value implicitly (with the [`SCNTransaction`](scntransaction.md) class) or explicitly (with the [`SCNAnimatable`](scnanimatable.md) protocol), SceneKit interpolates intermediate values and binds them to the uniform for each frame of the animation. For example, the following code animates the fading of a material from full color to grayscale:

```objc
// Set up the shader modifier with a custom uniform.
myMaterial.shaderModifiers = @{ SCNShaderModifierEntryPointFragment :
    @"uniform float mixLevel = 0.0;"
    "vec3 gray = vec3(dot(vec3(0.3, 0.59, 0.11), _output.color.rgb));"
    "_output.color = mix(_output.color, vec4(gray, 1.0), mixLevel);" };
 
// Later, animate a change to the uniform.
[SCNTransaction begin];
{
    [myMaterial setValue:@1.0 forKeyPath:@"mixLevel"];
}
[SCNTransaction commit];
```

Because SceneKit binds values to shader variables using [`Key-value observing`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KVO.html#//apple_ref/doc/uid/TP40008195-CH16), you can provide values in several ways. If you set a value using the [`setValue(_:forKey:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/setValue(_:forKey:)) or [`setValue(_:forKeyPath:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/setValue(_:forKeyPath:)) method, or set a target value for a keypath animation, the value must be contained in an Objective-C object. For uniforms of scalar types, you can assign an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object as a value. Assigning a uniform of a vector or matrix type requires an [`NSValue`](https://developer.apple.com/documentation/Foundation/NSValue) object containing data of the appropriate type. You can also bind textures to texture samplers using [`SCNMaterialProperty`](scnmaterialproperty.md) objects.

Alternatively, you can create an [`SCNMaterial`](scnmaterial.md) or [`SCNGeometry`](scngeometry.md) subclass for your custom shadable object and declare properties whose names match those of the uniform variables in your shader. When you assign a value to the property, SceneKit automatically binds it to the corresponding uniform in the shader program. In this case, your properties can use primitive or structure types appropriate to the corresponding Metal or GLSL variables.

The table below lists the Objective-C types for each shading language data type:

| GLSL data types | Metal data types | Objective-C type |
| --- | --- | --- |
| `int` | `int` | [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber), [`NSValue`](https://developer.apple.com/documentation/Foundation/NSValue) ([`NSInteger`](https://developer.apple.com/documentation/ObjectiveC/NSInteger), `int`) |
| `float` | `float` | [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber), [`NSValue`](https://developer.apple.com/documentation/Foundation/NSValue) ([`CGFloat`](https://developer.apple.com/documentation/CoreFoundation/CGFloat-swift.struct), `float`, `double`) |
| `vec2` | `float2` | [`NSValue`](https://developer.apple.com/documentation/Foundation/NSValue) ([`CGPoint`](https://developer.apple.com/documentation/CoreFoundation/CGPoint)) |
| `vec3` | `float3` | [`NSValue`](https://developer.apple.com/documentation/Foundation/NSValue) ([`SCNVector3`](scnvector3.md)) |
| `vec4` | `float4` | [`NSValue`](https://developer.apple.com/documentation/Foundation/NSValue) ([`SCNVector4`](scnvector4.md)) |
| `mat4` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `mat4x4` | `float4x4` | [`NSValue`](https://developer.apple.com/documentation/Foundation/NSValue) ([`CATransform3D`](https://developer.apple.com/documentation/QuartzCore/CATransform3D)) |
| `sampler2D` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `samplerCube` | `sampler` | [`SCNMaterialProperty`](scnmaterialproperty.md) |

###### Using Inputs Provided By Scenekit

SceneKit declares the following uniform variables containing global rendering parameters:

| Identifier | GLSL Type | Description |
| --- | --- | --- |
| `u_time` | `float` | The current system time (in seconds) since SceneKit started rendering with the shader. |
| `u_boundingBox` | `mat32` | The bounding box of the geometry being rendered, in model space. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `u_boundingBox[0].xyz` is the minimum corner of the bounding box and `u_boundingBox[1].xyz` is the maximum corner. |
| `u_modelTransform` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `u_viewTransform` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `u_projectionTransform` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `u_normalTransform` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `u_modelViewTransform` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `u_modelViewProjectionTransform` | `mat4` | The transform matrices used for converting vertex positions and normals between model, world, view, and clip coordinate spaces. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) For detailed definitions, see Rendering Transform Keys. |
| `u_inverseModelTransform` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `u_inverseViewTransform` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `u_inverseProjectionTransform` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `u_inverseModelViewTransform` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `u_inverseModelViewProjectionTransform` | `mat4` | The inverse matrices corresponding to each transform. |
| `u_diffuseTexture` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `u_ambientTexture` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `u_specularTexture` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `u_normalTexture` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `u_reflectiveTexture` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `u_emissionTexture` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `u_transparentTexture` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `u_multiplyTexture` | `sampler2D` or `samplerCube` | The texture contents of the corresponding material property. Declared only if the material property’s [`contents`](scnmaterialproperty/contents.md) object provides a texture image. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) The GLSL type of the uniform variable depends on whether the contents are a 2D image or cube map. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) For details on materials, see [`SCNMaterial`](scnmaterial.md). |

Shader modifiers may contain any legal Metal shader or GLSL code, with the exception that SceneKit reserves for its own use all identifier names with the `u_`, `a_`, and `v_` prefixes.

## Topics

### Assigning a Custom Shader Program
- [var program: SCNProgram?](scnshadable/program.md)
  A program used when rendering the object.
### Customizing SceneKit’s Shader Programs
- [var shaderModifiers: [SCNShaderModifierEntryPoint : String]?](scnshadable/shadermodifiers.md)
  A dictionary of GLSL source code snippets for customizing the shader programs provided by SceneKit.
### Handling Parameters in Custom OpenGL Shader Programs
- [func handleBinding(ofSymbol: String, handler: SCNBindingBlock?)](scnshadable/handlebinding(ofsymbol:handler:).md)
  Specifies a block to be called before rendering with programs with the specified GLSL uniform variable or attribute name.
- [func handleUnbinding(ofSymbol: String, handler: SCNBindingBlock?)](scnshadable/handleunbinding(ofsymbol:handler:).md)
  Specifies a block to be called after rendering with programs with the specified GLSL uniform variable or attribute name.
### Constants
- [typealias SCNBindingBlock](scnbindingblock.md)
  The signature for a block called for binding or unbinding a GLSL symbol in a custom program.
- [struct SCNShaderModifierEntryPoint](scnshadermodifierentrypoint.md)
  Keys for the [`shaderModifiers`](scnshadable/shadermodifiers.md) dictionary, each corresponding to an entry point in SceneKit’s shader programs where you can attach a custom GPU shader code snippet.
### Instance Properties
- [var minimumLanguageVersion: NSNumber?](scnshadable/minimumlanguageversion.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [SCNBox](scnbox.md)
- [SCNCapsule](scncapsule.md)
- [SCNCone](scncone.md)
- [SCNCylinder](scncylinder.md)
- [SCNFloor](scnfloor.md)
- [SCNGeometry](scngeometry.md)
- [SCNMaterial](scnmaterial.md)
- [SCNPlane](scnplane.md)
- [SCNPyramid](scnpyramid.md)
- [SCNShape](scnshape.md)
- [SCNSphere](scnsphere.md)
- [SCNText](scntext.md)
- [SCNTorus](scntorus.md)
- [SCNTube](scntube.md)

## See Also

- [class SCNProgram](scnprogram.md)
  A complete Metal or OpenGL shader program that replaces SceneKit’s rendering of a geometry or material.
- [protocol SCNBufferStream](scnbufferstream.md)
  An object that manages a Metal buffer used by a custom shader program.
- [class SCNTechnique](scntechnique.md)
  A specification for augmenting or postprocessing SceneKit’s rendering of a scene using additional drawing passes with custom Metal or OpenGL shaders.
- [protocol SCNTechniqueSupport](scntechniquesupport.md)
  The common interface for SceneKit objects that support multipass rendering using [`SCNTechnique`](scntechnique.md) objects.
- [protocol SCNNodeRendererDelegate](scnnoderendererdelegate.md)
  Methods you can implement to use your own custom Metal or OpenGL drawing code to render content for a node.
- [Postprocessing a Scene With Custom Symbols](postprocessing-a-scene-with-custom-symbols.md)
  Create visual effects in a scene by defining a rendering technique with custom symbols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnshadable)*