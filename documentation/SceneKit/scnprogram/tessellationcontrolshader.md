# tessellationControlShader

**Framework**: SceneKit  
**Kind**: property

GLSL source code for the program’s optional tessellation control shader.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var tessellationControlShader: String? { get set }
```

#### Discussion

A program’s tessellation control shader executes once for each vertex in the geometry it renders. The tessellation control shader takes as input the vertex positions output by the vertex shader, and outputs tessellation-level information to be used by the hardware tessellator for subdividing polygons and edges. The tessellator then provides input to your tessellation evaluation shader.

Tessellation shaders require macOS and OpenGL Core Profile. To use OpenGL Core Profile in a SceneKit view, set the view’s [`pixelFormat`](scnview/pixelformat.md) property. Tessellation shading is optional—to render without a tessellation shader, set this property’s value to `nil` (the default). However, if you specify a tessellation control shader, a tessellation evaluation shader is also required.

SceneKit compiles and links your shader program only when it is needed for rendering. To be notified of program compilation errors, provide a [`delegate`](scnprogram/delegate.md) object for the program.

## See Also

- [var vertexShader: String?](scnprogram/vertexshader.md)
  GLSL source code for the program’s vertex shader.
- [var fragmentShader: String?](scnprogram/fragmentshader.md)
  GLSL source code for the program’s fragment shader.
- [var geometryShader: String?](scnprogram/geometryshader.md)
  GLSL source code for the program’s optional geometry shader.
- [var tessellationEvaluationShader: String?](scnprogram/tessellationevaluationshader.md)
  GLSL source code for the program’s optional tessellation evaluation shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnprogram/tessellationcontrolshader)*