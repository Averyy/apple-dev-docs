# vertexShader

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

GLSL source code for the program’s vertex shader.

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
var vertexShader: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * vertexShader;
```

#### Discussion

A program’s vertex shader executes once for each vertex in the geometry it renders. It takes as input the attributes of each vertex (such as position in model space, normal vectors, and texture coordinates). The vertex shader then outputs a clip-space position for the vertex, as well as values that the GPU interpolates across a surface and sends to the fragment shader.

SceneKit compiles and links your shader program only when it is needed for rendering. To be notified of program compilation errors, provide a [`delegate`](./delegate.md) object for the program.

## See Also

### Working with OpenGL Shader Source Code
- [var fragmentShader: String?](./fragmentshader.md)
  GLSL source code for the program’s fragment shader.
- [var geometryShader: String?](./geometryshader.md)
  GLSL source code for the program’s optional geometry shader.
- [var tessellationControlShader: String?](./tessellationcontrolshader.md)
  GLSL source code for the program’s optional tessellation control shader.
- [var tessellationEvaluationShader: String?](./tessellationevaluationshader.md)
  GLSL source code for the program’s optional tessellation evaluation shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnprogram/vertexshader)*