# fragmentShader

**Framework**: SceneKit  
**Kind**: property

GLSL source code for the program’s fragment shader.

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
var fragmentShader: String? { get set }
```

#### Discussion

A program’s fragment shader (sometimes called a ) executes at least once for each pixel in rendered output. The fragment shader takes as input the values output by the vertex shader (after those values have been interpolated by the GPU), and uses them to compute a final color for each pixel.

SceneKit compiles and links your shader program only when it is needed for rendering. To be notified of program compilation errors, provide a [`delegate`](scnprogram/delegate.md) object for the program.

## See Also

- [var vertexShader: String?](scnprogram/vertexshader.md)
  GLSL source code for the program’s vertex shader.
- [var geometryShader: String?](scnprogram/geometryshader.md)
  GLSL source code for the program’s optional geometry shader.
- [var tessellationControlShader: String?](scnprogram/tessellationcontrolshader.md)
  GLSL source code for the program’s optional tessellation control shader.
- [var tessellationEvaluationShader: String?](scnprogram/tessellationevaluationshader.md)
  GLSL source code for the program’s optional tessellation evaluation shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnprogram/fragmentshader)*