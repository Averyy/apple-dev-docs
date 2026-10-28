# tessellationControlShader

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

GLSL source code for the program’s optional tessellation control shader.

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
var tessellationControlShader: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * tessellationControlShader;
```

## Discussion

A program’s tessellation control shader executes once for each vertex in the geometry it renders. The tessellation control shader takes as input the vertex positions output by the vertex shader, and outputs tessellation-level information to be used by the hardware tessellator for subdividing polygons and edges. The tessellator then provides input to your tessellation evaluation shader.

Tessellation shaders require macOS and OpenGL Core Profile. To use OpenGL Core Profile in a SceneKit view, set the view’s [`pixelFormat`](../scnview/pixelformat.md) property. Tessellation shading is optional—to render without a tessellation shader, set this property’s value to `nil` (the default). However, if you specify a tessellation control shader, a tessellation evaluation shader is also required.

SceneKit compiles and links your shader program only when it is needed for rendering. To be notified of program compilation errors, provide a [`delegate`](./delegate.md) object for the program.

## See Also

### Working with OpenGL Shader Source Code
- [var vertexShader: String?](./vertexshader.md)
  GLSL source code for the program’s vertex shader.
- [var fragmentShader: String?](./fragmentshader.md)
  GLSL source code for the program’s fragment shader.
- [var geometryShader: String?](./geometryshader.md)
  GLSL source code for the program’s optional geometry shader.
- [var tessellationEvaluationShader: String?](./tessellationevaluationshader.md)
  GLSL source code for the program’s optional tessellation evaluation shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnprogram/tessellationcontrolshader)*