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

When the skybox shader is bound, the following state variables are altered:

- `GL_CURRENT_PROGRAM`
- `GL_TEXTURE_BINDING_CUBE_MAP`
- `GL_VERTEX_ARRAY_BINDING_OES`
- `GL_VERTEX_ATTRIB_ARRAY_ENABLED`

Your application is responsible for saving and restoring these variables, if necessary for it to execute correctly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkskyboxeffect/preparetodraw())*