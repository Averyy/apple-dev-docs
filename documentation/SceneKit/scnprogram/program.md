# program

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates a new program object.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```objc
+ (instancetype) program;
```

#### Return Value

The initialized `SCNProgram` object, or `nil` if initialization is not successful.

#### Discussion

You cannot use the newly created program object for rendering until you provide shader source code for its [`vertexShader`](./vertexshader.md) and [`fragmentShader`](./fragmentshader.md) properties.

To use a shader for rendering, assign it to the [`program`](./program.md) property of a geometry or material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnprogram/program)*