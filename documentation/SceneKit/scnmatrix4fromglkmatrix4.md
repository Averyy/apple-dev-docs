# SCNMatrix4FromGLKMatrix4(_:)

**Framework**: SceneKit  
**Kind**: func

Returns a SceneKit matrix corresponding to a GLKit matrix.

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
func SCNMatrix4FromGLKMatrix4(_ mat: GLKMatrix4) -> SCNMatrix4
```

#### Return Value

A SceneKit matrix representing the same 3D transformation.

## Parameters

- `mat`: A GLKit matrix.

## See Also

- [func SCNMatrix4ToGLKMatrix4(SCNMatrix4) -> GLKMatrix4](scnmatrix4toglkmatrix4(_:).md)
  Returns a GLKit matrix corresponding to a SceneKit matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmatrix4fromglkmatrix4(_:))*