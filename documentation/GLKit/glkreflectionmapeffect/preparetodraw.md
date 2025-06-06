# prepareToDraw()

**Framework**: GLKit  
**Kind**: method

Prepares an effect for rendering.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func prepareToDraw()
```

#### Discussion

An effect must be prepared after it is configured and again when your application wants to use the effect to render any primitives. When your application prepares an effect, some OpenGL state is altered to allow the effect to operate:

- The `GL_CURRENT_PROGRAM` state is always changed to point to the shader provided by the effect object.
- When texturing is enabled, the `GL_TEXTURE_BINDING_2D` state and `GL_TEXTURE_BINDING_CUBE_MAP` state may also change.

If your application requires the previous state to be saved before the effect alters them, it must explicitly save and restore the values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkreflectionmapeffect/preparetodraw())*