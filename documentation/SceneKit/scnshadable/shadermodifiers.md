# shaderModifiers

**Framework**: SceneKit  
**Kind**: property

A dictionary of GLSL source code snippets for customizing the shader programs provided by SceneKit.

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
optional var shaderModifiers: [SCNShaderModifierEntryPoint : String]? { get set }
```

#### Discussion

The dictionary’s keys must be from the set of constants described in `Shader Modifier Entry Point Keys`. Each key represents a possible entry point in SceneKit’s shader programs, whose corresponding value is an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) object containing a shader source code snippet to be included in the shader program at that entry point.

See [`Use Shader Modifiers to Extend SceneKit Shading`](scnshadable#Use-Shader-Modifiers-to-Extend-SceneKit-Shading.md) in the protocol overview for a complete discussion of shader modifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnshadable/shadermodifiers)*