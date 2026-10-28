# SCNBindingBlock

**Framework**: SceneKit  
**Kind**: typealias  
**Role**: Type Alias

The signature for a block called for binding or unbinding a GLSL symbol in a custom program.

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
typealias SCNBindingBlock = (UInt32, UInt32, SCNNode?, SCNRenderer) -> Void
```

```c
typedef void (^)(unsigned int, unsigned int, SCNNode *, SCNRenderer *) SCNBindingBlock;
```

## Discussion

The block takes the following parameters:

- **`programID`**: The OpenGL program identifier for the current [`SCNProgram`](./scnprogram.md) instance, as used by OpenGL functions such as `glValidateProgram`.
- **`location`**: The OpenGL location index for the symbol to be bound or unbound, as used by OpenGL functions such as `glUniform`.
- **`renderedNode`**: The [`SCNNode`](./scnnode.md) object being rendered.
- **`renderer`**: The [`SCNRenderer`](./scnrenderer.md) object responsible for rendering.

Call [`handleBinding(ofSymbol:handler:)`](./scnshadable/handlebinding%28ofsymbol,handler%29.md) or [`handleUnbinding(ofSymbol:handler:)`](./scnshadable/handleunbinding%28ofsymbol,handler%29.md) to associate a handler block with a GLSL symbol for a SceneKit geometry or material.

## See Also

### Constants
- [struct SCNShaderModifierEntryPoint](./scnshadermodifierentrypoint.md)
  Keys for the [`shaderModifiers`](./scnshadable/shadermodifiers.md) dictionary, each corresponding to an entry point in SceneKit’s shader programs where you can attach a custom GPU shader code snippet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnbindingblock)*