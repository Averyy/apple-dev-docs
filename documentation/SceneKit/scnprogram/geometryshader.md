# geometryShader

**Framework**: SceneKit  
**Kind**: property

GLSL source code for the program’s optional geometry shader.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var geometryShader: String? { get set }
```

#### Discussion

A program’s geometry shader executes once for each geometric primitive (line or triangle) to be rendered. The geometry shader takes as input the vertex positions output by the vertex shader (or by the tessellation shader, if one is in use), and outputs new geometric primitives for rendering.

Geometry shaders require macOS and OpenGL Core Profile. To use OpenGL Core Profile in a SceneKit view, set the view’s [`pixelFormat`](scnview/pixelformat.md) property. Geometry shading is optional—to render without a geometry shader, set this property’s value to `nil` (the default).

SceneKit compiles and links your shader program only when it is needed for rendering. To be notified of program compilation errors, provide a [`delegate`](scnprogram/delegate.md) object for the program.

## See Also

- [var vertexShader: String?](scnprogram/vertexshader.md)
  GLSL source code for the program’s vertex shader.
- [var fragmentShader: String?](scnprogram/fragmentshader.md)
  GLSL source code for the program’s fragment shader.
- [var tessellationControlShader: String?](scnprogram/tessellationcontrolshader.md)
  GLSL source code for the program’s optional tessellation control shader.
- [var tessellationEvaluationShader: String?](scnprogram/tessellationevaluationshader.md)
  GLSL source code for the program’s optional tessellation evaluation shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnprogram/geometryshader)*