# leftProjectionMatrix

**Framework**: Model I/O  
**Kind**: property

The transformation matrix that determines the extent of a scene visible to the camera’s left viewpoint.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var leftProjectionMatrix: matrix_float4x4 { get }
```

#### Discussion

Model I/O  automatically generates this matrix from the same properties that produce the [`projectionMatrix`](mdlcamera/projectionmatrix.md) property of a monocular camera, additionally using the [`interPupillaryDistance`](mdlstereoscopiccamera/interpupillarydistance.md) and [`leftVergence`](mdlstereoscopiccamera/leftvergence.md) properties to account for the offset and angle of a stereoscopic camera’s left viewpoint.

A renderer uses this matrix, along with the [`leftViewMatrix`](mdlstereoscopiccamera/leftviewmatrix.md) property and model matrices derived from the camera’s position and orientation (the [`transform`](mdlobject/transform.md) property) and the content to be rendered, to transform vertex data to the renderer’s 2D screen space at render time.

## See Also

- [var leftViewMatrix: matrix_float4x4](mdlstereoscopiccamera/leftviewmatrix.md)
  The transformation matrix that determines the position and orientation of the camera’s left viewpoint relative to a scene.
- [var rightViewMatrix: matrix_float4x4](mdlstereoscopiccamera/rightviewmatrix.md)
  The transformation matrix that determines the position and orientation of the camera’s right viewpoint relative to a scene.
- [var rightProjectionMatrix: matrix_float4x4](mdlstereoscopiccamera/rightprojectionmatrix.md)
  The transformation matrix that determines the extent of a scene visible to the camera’s right viewpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlstereoscopiccamera/leftprojectionmatrix)*