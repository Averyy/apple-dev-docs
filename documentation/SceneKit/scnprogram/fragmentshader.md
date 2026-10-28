# fragmentShader

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

GLSL source code for the program’s fragment shader.

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
var fragmentShader: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * fragmentShader;
```

## Discussion

A program’s fragment shader (sometimes called a *pixel shader*) executes at least once for each pixel in rendered output. The fragment shader takes as input the values output by the vertex shader (after those values have been interpolated by the GPU), and uses them to compute a final color for each pixel.

SceneKit compiles and links your shader program only when it is needed for rendering. To be notified of program compilation errors, provide a [`delegate`](./delegate.md) object for the program.

## See Also

### Working with OpenGL Shader Source Code
- [var vertexShader: String?](./vertexshader.md)
  GLSL source code for the program’s vertex shader.
- [var geometryShader: String?](./geometryshader.md)
  GLSL source code for the program’s optional geometry shader.
- [var tessellationControlShader: String?](./tessellationcontrolshader.md)
  GLSL source code for the program’s optional tessellation control shader.
- [var tessellationEvaluationShader: String?](./tessellationevaluationshader.md)
  GLSL source code for the program’s optional tessellation evaluation shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnprogram/fragmentshader)*