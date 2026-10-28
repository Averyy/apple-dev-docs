# SCNMatrix4FromGLKMatrix4(_:)

**Framework**: SceneKit  
**Kind**: func  
**Role**: Function

Returns a SceneKit matrix corresponding to a GLKit matrix.

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
func SCNMatrix4FromGLKMatrix4(_ mat: GLKMatrix4) -> SCNMatrix4
```

```c
extern SCNMatrix4 SCNMatrix4FromGLKMatrix4(GLKMatrix4 mat);
```

## Return Value

A SceneKit matrix representing the same 3D transformation.

## Parameters

- `mat`: A GLKit matrix.

## See Also

### Converting Matrix Types
- [func SCNMatrix4ToGLKMatrix4(SCNMatrix4) -> GLKMatrix4](./scnmatrix4toglkmatrix4%28_%29.md)
  Returns a GLKit matrix corresponding to a SceneKit matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmatrix4fromglkmatrix4(_:))*